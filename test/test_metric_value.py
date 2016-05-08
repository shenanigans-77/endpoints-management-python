# Copyright 2016, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import absolute_import

import datetime
import hashlib

import unittest2
from expects import equal, expect, raise_error

from apitools.base.py import encoding
from google.scc import distribution, timestamp, MetricKind
from google.scc.aggregators import metric_value
from google.apigen.servicecontrol_v1_messages import (MetricValue, Money)


class TestUpdateHash(unittest2.TestCase):
    NOTHING_ADDED = hashlib.md5().digest()

    def make_hash(self, mv):
        md5 = hashlib.md5()
        metric_value.update_hash(md5, mv)
        return md5.digest()

    def test_should_add_nothing_without_labels_or_currency(self):
        expect(self.make_hash(MetricValue())).to(equal(self.NOTHING_ADDED))

    def test_should_add_matching_hashes_for_matching_labels(self):
        a_dict = {'test': 'dict'}
        mv1 = metric_value.create(labels=a_dict)
        mv2 = metric_value.create(labels=a_dict)
        want = self.make_hash(mv1)
        got = self.make_hash(mv2)
        expect(got).to(equal(want))

    def test_should_update_hash_for_when_currency_is_added(self):
        a_dict = {'test': 'dict'}
        mv1 = metric_value.create(labels=a_dict)
        mv2 = metric_value.create(labels=a_dict)
        mv2.moneyValue = Money(currencyCode='JPY')
        want = self.make_hash(mv1)
        got = self.make_hash(mv2)
        expect(got).to_not(equal(want))


class TestSign(TestUpdateHash):

    def make_hash(self, mv):
        return metric_value.sign(mv)


class TestMerge(unittest2.TestCase):
    A_FLOAT_VALUE = 1.0
    EARLY = timestamp.to_rfc3339(datetime.datetime(1970, 1, 1, 10, 0, 0))
    LATER = timestamp.to_rfc3339(datetime.datetime(1990, 1, 1, 10, 0, 0))
    TEST_LABELS = {
        'key1': 'value1',
        'key2': 'value2',
    }

    def setUp(self):
        self.test_value = metric_value.create(
            labels=self.TEST_LABELS,
            doubleValue=self.A_FLOAT_VALUE)
        self.early_ending = metric_value.create(
            labels=self.TEST_LABELS,
            doubleValue=self.A_FLOAT_VALUE,
            endTime=self.EARLY)
        self.late_ending = metric_value.create(
            labels=self.TEST_LABELS,
            doubleValue=self.A_FLOAT_VALUE,
            endTime=self.LATER)
        self.test_value_with_money = metric_value.create(
            labels=self.TEST_LABELS,
            moneyValue=Money(currencyCode='JPY', units=100, nanos=0))

    def test_should_fail_for_metric_values_with_different_types(self):
        changed = metric_value.create(labels=self.TEST_LABELS, int64Value=1)
        for kind in (MetricKind.GAUGE, MetricKind.CUMULATIVE, MetricKind.DELTA):
            testf = lambda: metric_value.merge(kind, self.test_value, changed)
            expect(testf).to(raise_error(ValueError))

    def test_should_fail_for_uninitialized_metric_values(self):
        no_init = metric_value.create()
        for kind in (MetricKind.GAUGE, MetricKind.CUMULATIVE, MetricKind.DELTA):
            testf = lambda: metric_value.merge(kind, no_init, no_init)
            expect(testf).to(raise_error(ValueError))

    def test_should_fail_for_delta_metrics_with_unmergable_types(self):
        no_init = metric_value.create()
        unmergeables = [
            metric_value.create(stringValue='a test string'),
            metric_value.create(boolValue=False),
        ]
        for mv in unmergeables:
            testf = lambda: metric_value.merge(MetricKind.DELTA, mv, mv)
            expect(testf).to(raise_error(ValueError))

    def test_should_succeed_for_delta_metrics_with_the_money_type(self):
        v = self.test_value_with_money
        want = 2 * v.moneyValue.units
        got = metric_value.merge(MetricKind.DELTA, v, v)
        expect(got.moneyValue.units).to(equal(want))

    def test_should_succeed_for_delta_metrics_with_the_double_type(self):
        v = self.test_value
        want = 2 * v.doubleValue
        got = metric_value.merge(MetricKind.DELTA, v, v)
        expect(got.doubleValue).to(equal(want))

    def test_should_succeed_for_delta_metrics_with_the_int64_type(self):
        test_int = 4
        v = metric_value.create(labels=self.TEST_LABELS, int64Value=test_int)
        want = 2 * test_int
        got = metric_value.merge(MetricKind.DELTA, v, v)
        expect(got.int64Value).to(equal(want))

    def test_should_succeed_for_delta_metrics_with_the_distribution_type(self):
        test_distribution = distribution.create_explicit([0.1, 0.3, 0.5])
        distribution.add_sample(0.4, test_distribution)
        v = metric_value.create(labels=self.TEST_LABELS,
                                distributionValue=test_distribution)
        want = 2 * test_distribution.count
        got = metric_value.merge(MetricKind.DELTA, v, v)
        expect(got.distributionValue.count).to(equal(want))

    def test_should_return_metric_value_with_latest_end_time_for_non_deltas(self):
        for kind in (MetricKind.GAUGE, MetricKind.CUMULATIVE):
            got = metric_value.merge(kind, self.early_ending, self.late_ending)
            expect(got).to(equal(self.late_ending))
            got = metric_value.merge(kind, self.late_ending, self.early_ending)
            expect(got).to(equal(self.late_ending))

    def test_should_use_the_latest_end_time_delta_merges(self):
        got = metric_value.merge(MetricKind.DELTA,
                                 self.early_ending,
                                 self.late_ending)
        expect(got.endTime).to(equal(self.late_ending.endTime))
        got = metric_value.merge(MetricKind.DELTA,
                                 self.late_ending,
                                 self.early_ending)
        expect(got.endTime).to(equal(self.late_ending.endTime))

    def test_should_use_the_earliest_start_time_in_delta_merges(self):
        early_starting = metric_value.create(
            labels=self.TEST_LABELS,
            doubleValue=self.A_FLOAT_VALUE,
            startTime=self.EARLY)
        late_starting = metric_value.create(
            labels=self.TEST_LABELS,
            doubleValue=self.A_FLOAT_VALUE,
            startTime=self.LATER)
        got = metric_value.merge(MetricKind.DELTA, early_starting,
                                 late_starting)
        expect(got.startTime).to(equal(early_starting.startTime))
        got = metric_value.merge(MetricKind.DELTA, late_starting,
                                 early_starting)
        expect(got.startTime).to(equal(early_starting.startTime))