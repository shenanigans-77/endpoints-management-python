# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Generated message classes for servicecontrol version v1.

Google Service Control provides control plane functionality to managed
services, such as logging, monitoring, and status checks.
"""
# NOTE: This file is originally auto-generated using google-apitools then
# style-correcting hand edits were applied.  New behaviour should not provided
# by hand, please re-generate and restyle.
from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'servicecontrol'


class AllocateQuotaRequest(_messages.Message):
    """Request message for the AllocateQuota method.

    Enums:
      AllocationModeValueValuesEnum: Allocation mode for this operation.
        Deprecated: use QuotaMode inside the QuotaOperation.

    Fields:
      allocateOperation: Operation that describes the quota allocation.
      allocationMode: Allocation mode for this operation. Deprecated: use
        QuotaMode inside the QuotaOperation.
      serviceConfigId: Specifies which version of service configuration should
        be used to process the request. If unspecified or no matching version
        can be found, the latest one will be used.
    """

    class AllocationModeValueValuesEnum(_messages.Enum):
        """Allocation mode for this operation. Deprecated: use QuotaMode
        inside the QuotaOperation.

        Values:
          UNSPECIFIED: <no description>
          NORMAL: Allocates quota for the amount specified in the service
            configuration or specified using the quota_metrics. If the amount
            is higher than the available quota, allocation error will be
            returned and no quota will be allocated.
          BEST_EFFORT: Allocates quota for the amount specified in the service
            configuration or specified using the quota_metrics. If the amount
            is higher than the available quota, request does not fail but all
            available quota will be allocated.
          CHECK_ONLY: Only checks if there is enough quota available and does
            not change the available quota. No lock is placed on the available
            quota either.
        """
        UNSPECIFIED = 0
        NORMAL = 1
        BEST_EFFORT = 2
        CHECK_ONLY = 3

    allocateOperation = _messages.MessageField('QuotaOperation', 1)
    allocationMode = _messages.EnumField('AllocationModeValueValuesEnum', 2)
    serviceConfigId = _messages.StringField(3)


class AllocateQuotaResponse(_messages.Message):
    """Response message for the AllocateQuota method.

    Fields:
      allocateErrors: Indicates the decision of the allocate.
      operationId: The same operation_id value used in the
        AllocateQuotaRequest. Used for logging and diagnostics purposes.
      quotaMetrics: Quota metrics to indicate the result of allocation.
        Depending on the request, one or more of the following metrics will be
        included:  1. For rate quota, per quota group or per quota metric
        incremental usage will be specified using the following delta metric:
        "serviceruntime.googleapis.com/api/consumer/quota_used_count"  2. For
        allocation quota, per quota metric total usage will be specified using
        the following gauge metric:
        "serviceruntime.googleapis.com/allocation/consumer/quota_used_count"
        3. For both rate quota and allocation quota, the quota limit reached
        condition will be specified using the following boolean metric:
        "serviceruntime.googleapis.com/quota/exceeded"  4. For allocation
        quota, value for each quota limit associated with the metrics will be
        specified using the following gauge metric:
        "serviceruntime.googleapis.com/quota/limit"
      serviceConfigId: ID of the actual config used to process the request.
    """

    allocateErrors = _messages.MessageField('QuotaError', 1, repeated=True)
    operationId = _messages.StringField(2)
    quotaMetrics = _messages.MessageField('MetricValueSet', 3, repeated=True)
    serviceConfigId = _messages.StringField(4)


class AuditLog(_messages.Message):
    """Common audit log format for Google Cloud Platform API operations.

    Messages:
      RequestValue: The operation request. This may not include all request
        parameters, such as those that are too large, privacy-sensitive, or
        duplicated elsewhere in the log record. It should never include user-
        generated data, such as file contents. When the JSON object
        represented here has a proto equivalent, the proto name will be
        indicated in the `@type` property.
      ResponseValue: The operation response. This may not include all response
        elements, such as those that are too large, privacy-sensitive, or
        duplicated elsewhere in the log record. It should never include user-
        generated data, such as file contents. When the JSON object
        represented here has a proto equivalent, the proto name will be
        indicated in the `@type` property.
      ServiceDataValue: Other service-specific data about the request,
        response, and other activities.

    Fields:
      authenticationInfo: Authentication information.
      authorizationInfo: Authorization information. If there are multiple
        resources or permissions involved, then there is one AuthorizationInfo
        element for each {resource, permission} tuple.
      methodName: The name of the service method or operation. For API calls,
        this should be the name of the API method. For example,
        "google.datastore.v1.Datastore.RunQuery"
        "google.logging.v1.LoggingService.DeleteLog"
      numResponseItems: The number of items returned from a List or Query API
        method, if applicable.
      request: The operation request. This may not include all request
        parameters, such as those that are too large, privacy-sensitive, or
        duplicated elsewhere in the log record. It should never include user-
        generated data, such as file contents. When the JSON object
        represented here has a proto equivalent, the proto name will be
        indicated in the `@type` property.
      requestMetadata: Metadata about the operation.
      resourceName: The resource or collection that is the target of the
        operation. The name is a scheme-less URI, not including the API
        service name. For example:      "shelves/SHELF_ID/books"
        "shelves/SHELF_ID/books/BOOK_ID"
      response: The operation response. This may not include all response
        elements, such as those that are too large, privacy-sensitive, or
        duplicated elsewhere in the log record. It should never include user-
        generated data, such as file contents. When the JSON object
        represented here has a proto equivalent, the proto name will be
        indicated in the `@type` property.
      serviceData: Other service-specific data about the request, response,
        and other activities.
      serviceName: The name of the API service performing the operation. For
        example, `"datastore.googleapis.com"`.
      status: The status of the overall operation.
    """

    @encoding.MapUnrecognizedFields('additionalProperties')
    class RequestValue(_messages.Message):
        """The operation request. This may not include all request parameters,
        such as those that are too large, privacy-sensitive, or duplicated
        elsewhere in the log record. It should never include user-generated
        data, such as file contents. When the JSON object represented here has
        a proto equivalent, the proto name will be indicated in the `@type`
        property.

        Messages:
          AdditionalProperty: An additional property for a RequestValue
            object.

        Fields:
          additionalProperties: Properties of the object.
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a RequestValue object.

            Fields:
              key: Name of the additional property.
              value: A extra_types.JsonValue attribute.
            """

            key = _messages.StringField(1)
            value = _messages.MessageField('extra_types.JsonValue', 2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    @encoding.MapUnrecognizedFields('additionalProperties')
    class ResponseValue(_messages.Message):
        """The operation response. This may not include all response elements,
        such as those that are too large, privacy-sensitive, or duplicated
        elsewhere in the log record. It should never include user-generated
        data, such as file contents. When the JSON object represented here has
        a proto equivalent, the proto name will be indicated in the `@type`
        property.

        Messages:
          AdditionalProperty: An additional property for a ResponseValue
            object.

        Fields:
          additionalProperties: Properties of the object.
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a ResponseValue object.

            Fields:
              key: Name of the additional property.
              value: A extra_types.JsonValue attribute.
            """

            key = _messages.StringField(1)
            value = _messages.MessageField('extra_types.JsonValue', 2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    @encoding.MapUnrecognizedFields('additionalProperties')
    class ServiceDataValue(_messages.Message):
        """Other service-specific data about the request, response, and other
        activities.

        Messages:
          AdditionalProperty: An additional property for a ServiceDataValue
            object.

        Fields:
          additionalProperties: Properties of the object. Contains field @type
            with type URL.
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a ServiceDataValue object.

            Fields:
              key: Name of the additional property.
              value: A extra_types.JsonValue attribute.
            """

            key = _messages.StringField(1)
            value = _messages.MessageField('extra_types.JsonValue', 2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    authenticationInfo = _messages.MessageField('AuthenticationInfo', 1)
    authorizationInfo = _messages.MessageField('AuthorizationInfo', 2, repeated=True)
    methodName = _messages.StringField(3)
    numResponseItems = _messages.IntegerField(4)
    request = _messages.MessageField('RequestValue', 5)
    requestMetadata = _messages.MessageField('RequestMetadata', 6)
    resourceName = _messages.StringField(7)
    response = _messages.MessageField('ResponseValue', 8)
    serviceData = _messages.MessageField('ServiceDataValue', 9)
    serviceName = _messages.StringField(10)
    status = _messages.MessageField('Status', 11)


class AuthenticationInfo(_messages.Message):
    """Authentication information for the operation.

    Fields:
      authoritySelector: The authority selector specified by the requestor, if
        any. It is not guaranteed that the principal was allowed to use this
        authority.
      principalEmail: The email address of the authenticated user making the
        request.
    """

    authoritySelector = _messages.StringField(1)
    principalEmail = _messages.StringField(2)


class AuthorizationInfo(_messages.Message):
    """Authorization information for the operation.

    Fields:
      granted: Whether or not authorization for `resource` and `permission`
        was granted.
      permission: The required IAM permission.
      resource: The resource being accessed, as a REST-style string. For
        example:
        bigquery.googlapis.com/projects/PROJECTID/datasets/DATASETID
    """

    granted = _messages.BooleanField(1)
    permission = _messages.StringField(2)
    resource = _messages.StringField(3)


class CheckError(_messages.Message):
    """Defines the errors to be returned in
    google.api.servicecontrol.v1.CheckResponse.check_errors.

    Enums:
      CodeValueValuesEnum: The error code.

    Fields:
      code: The error code.
      detail: Free-form text providing details on the error cause of the
        error.
    """

    class CodeValueValuesEnum(_messages.Enum):
        """The error code.

        Values:
          ERROR_CODE_UNSPECIFIED: This is never used in `CheckResponse`.
          NOT_FOUND: The consumer's project id was not found. Same as
            google.rpc.Code.NOT_FOUND.
          PERMISSION_DENIED: The consumer doesn't have access to the specified
            resource. Same as google.rpc.Code.PERMISSION_DENIED.
          RESOURCE_EXHAUSTED: Quota check failed. Same as
            google.rpc.Code.RESOURCE_EXHAUSTED.
          BUDGET_EXCEEDED: Budget check failed.
          DENIAL_OF_SERVICE_DETECTED: The consumer's request has been flagged
            as a DoS attack.
          LOAD_SHEDDING: The consumer's request should be rejected in order to
            protect the service from being overloaded.
          ABUSER_DETECTED: The consumer has been flagged as an abuser.
          SERVICE_NOT_ACTIVATED: The consumer hasn't activated the service.
          VISIBILITY_DENIED: The consumer cannot access the service due to
            visibility configuration.
          BILLING_DISABLED: The consumer cannot access the service because
            billing is disabled.
          PROJECT_DELETED: The consumer's project has been marked as deleted
            (soft deletion).
          PROJECT_INVALID: The consumer's project number or id does not
            represent a valid project.
          IP_ADDRESS_BLOCKED: The IP address of the consumer is invalid for
            the specific consumer project.
          REFERER_BLOCKED: The referer address of the consumer request is
            invalid for the specific consumer project.
          CLIENT_APP_BLOCKED: The client application of the consumer request
            is invalid for the specific consumer project.
          API_TARGET_BLOCKED: The API targeted by this request is invalid for
            the specified consumer project.
          API_KEY_INVALID: The consumer's API key is invalid.
          API_KEY_EXPIRED: The consumer's API Key has expired.
          API_KEY_NOT_FOUND: The consumer's API Key was not found in config
            record.
          SPATULA_HEADER_INVALID: The consumer's spatula header is invalid.
          LOAS_ROLE_INVALID: The consumer's LOAS role is invalid.
          NO_LOAS_PROJECT: The consumer's LOAS role has no associated project.
          LOAS_PROJECT_DISABLED: The consumer's LOAS project is not `ACTIVE`
            in LoquatV2.
          SECURITY_POLICY_VIOLATED: Request is not allowed as per security
            policies defined in Org Policy.
          NAMESPACE_LOOKUP_UNAVAILABLE: The backend server for looking up
            project id/number is unavailable.
          SERVICE_STATUS_UNAVAILABLE: The backend server for checking service
            status is unavailable.
          BILLING_STATUS_UNAVAILABLE: The backend server for checking billing
            status is unavailable.
          QUOTA_CHECK_UNAVAILABLE: The backend server for checking quota
            limits is unavailable.
          LOAS_PROJECT_LOOKUP_UNAVAILABLE: The Spanner for looking up LOAS
            project is unavailable.
          CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE: Cloud Resource Manager
            backend server is unavailable.
          SECURITY_POLICY_BACKEND_UNAVAILABLE: Backend server for evaluating
            security policy is unavailable.
        """
        ERROR_CODE_UNSPECIFIED = 0
        NOT_FOUND = 1
        PERMISSION_DENIED = 2
        RESOURCE_EXHAUSTED = 3
        BUDGET_EXCEEDED = 4
        DENIAL_OF_SERVICE_DETECTED = 5
        LOAD_SHEDDING = 6
        ABUSER_DETECTED = 7
        SERVICE_NOT_ACTIVATED = 8
        VISIBILITY_DENIED = 9
        BILLING_DISABLED = 10
        PROJECT_DELETED = 11
        PROJECT_INVALID = 12
        IP_ADDRESS_BLOCKED = 13
        REFERER_BLOCKED = 14
        CLIENT_APP_BLOCKED = 15
        API_TARGET_BLOCKED = 16
        API_KEY_INVALID = 17
        API_KEY_EXPIRED = 18
        API_KEY_NOT_FOUND = 19
        SPATULA_HEADER_INVALID = 20
        LOAS_ROLE_INVALID = 21
        NO_LOAS_PROJECT = 22
        LOAS_PROJECT_DISABLED = 23
        SECURITY_POLICY_VIOLATED = 24
        NAMESPACE_LOOKUP_UNAVAILABLE = 25
        SERVICE_STATUS_UNAVAILABLE = 26
        BILLING_STATUS_UNAVAILABLE = 27
        QUOTA_CHECK_UNAVAILABLE = 28
        LOAS_PROJECT_LOOKUP_UNAVAILABLE = 29
        CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE = 30
        SECURITY_POLICY_BACKEND_UNAVAILABLE = 31

    code = _messages.EnumField('CodeValueValuesEnum', 1)
    detail = _messages.StringField(2)


class CheckInfo(_messages.Message):
    """A CheckInfo object.

    Fields:
      unusedArguments: A list of fields and label keys that are ignored by the
        server. The client doesn't need to send them for following requests to
        improve performance and allow better aggregation.
    """

    unusedArguments = _messages.StringField(1, repeated=True)


class CheckRequest(_messages.Message):
    """Request message for the Check method.

    Fields:
      operation: The operation to be checked.
      requestProjectSettings: Requests the project settings to be returned as
        part of the check response.
      serviceConfigId: Specifies which version of service configuration should
        be used to process the request.  If unspecified or no matching version
        can be found, the latest one will be used.
      skipActivationCheck: Indicates if service activation check should be
        skipped for this request. Default behavior is to perform the check and
        apply relevant quota.
    """

    operation = _messages.MessageField('Operation', 1)
    requestProjectSettings = _messages.BooleanField(2)
    serviceConfigId = _messages.StringField(3)
    skipActivationCheck = _messages.BooleanField(4)


class CheckResponse(_messages.Message):
    """Response message for the Check method.

    Fields:
      checkErrors: Indicate the decision of the check.  If no check errors are
        present, the service should process the operation. Otherwise the
        service should use the list of errors to determine the appropriate
        action.
      checkInfo: Feedback data returned from the server during processing a
        Check request.
      operationId: The same operation_id value used in the CheckRequest. Used
        for logging and diagnostics purposes.
      quotaInfo: Quota information for the check request associated with this
        response.
      serviceConfigId: The actual config id used to process the request.
    """

    checkErrors = _messages.MessageField('CheckError', 1, repeated=True)
    checkInfo = _messages.MessageField('CheckInfo', 2)
    operationId = _messages.StringField(3)
    quotaInfo = _messages.MessageField('QuotaInfo', 4)
    serviceConfigId = _messages.StringField(5)


class Distribution(_messages.Message):
    """Distribution represents a frequency distribution of double-valued
    sample points. It contains the size of the population of sample points
    plus additional optional information:    - the arithmetic mean of the
    samples   - the minimum and maximum of the samples   - the sum-squared-
    deviation of the samples, used to compute variance   - a histogram of the
    values of the sample points

    Fields:
      bucketCounts: The number of samples in each histogram bucket.
        `bucket_counts` are optional. If present, they must sum to the `count`
        value.  The buckets are defined below in `bucket_option`. There are N
        buckets. `bucket_counts[0]` is the number of samples in the underflow
        bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of
        samples in each of the finite buckets. And `bucket_counts[N] is the
        number of samples in the overflow bucket. See the comments of
        `bucket_option` below for more details.  Any suffix of trailing zeros
        may be omitted.
      count: The total number of samples in the distribution. Must be >= 0.
      explicitBuckets: Buckets with arbitrary user-provided width.
      exponentialBuckets: Buckets with exponentially growing width.
      linearBuckets: Buckets with constant width.
      maximum: The maximum of the population of values. Ignored if `count` is
        zero.
      mean: The arithmetic mean of the samples in the distribution. If `count`
        is zero then this field must be zero.
      minimum: The minimum of the population of values. Ignored if `count` is
        zero.
      sumOfSquaredDeviation: The sum of squared deviations from the mean:
        Sum[i=1..count]((x_i - mean)^2) where each x_i is a sample values. If
        `count` is zero then this field must be zero, otherwise validation of
        the request fails.
    """

    bucketCounts = _messages.IntegerField(1, repeated=True)
    count = _messages.IntegerField(2)
    explicitBuckets = _messages.MessageField('ExplicitBuckets', 3)
    exponentialBuckets = _messages.MessageField('ExponentialBuckets', 4)
    linearBuckets = _messages.MessageField('LinearBuckets', 5)
    maximum = _messages.FloatField(6)
    mean = _messages.FloatField(7)
    minimum = _messages.FloatField(8)
    sumOfSquaredDeviation = _messages.FloatField(9)


class EndReconciliationRequest(_messages.Message):
    """A EndReconciliationRequest object.

    Fields:
      reconciliationOperation: Operation that describes the quota
        reconciliation.
      serviceConfigId: Specifies which version of service configuration should
        be used to process the request. If unspecified or no matching version
        can be found, the latest one will be used.
    """

    reconciliationOperation = _messages.MessageField('QuotaOperation', 1)
    serviceConfigId = _messages.StringField(2)


class EndReconciliationResponse(_messages.Message):
    """A EndReconciliationResponse object.

    Fields:
      operationId: The same operation_id value used in the
        EndReconciliationRequest. Used for logging and diagnostics purposes.
      quotaMetrics: Metric values as tracked by One Platform before the
        adjustment was made. The following metrics will be included:  1. Per
        quota metric total usage will be specified using the following gauge
        metric:
        "serviceruntime.googleapis.com/allocation/consumer/quota_used_count"
        2. Value for each quota limit associated with the metrics will be
        specified using the following gauge metric:
        "serviceruntime.googleapis.com/quota/limit"  3. Delta value of the
        usage after the reconciliation for limits associated with the metrics
        will be specified using the following metric:
        "serviceruntime.googleapis.com/allocation/reconciliation_delta" The
        delta value is defined as:   new_usage_from_client -
        existing_value_in_spanner. This metric is not defined in
        serviceruntime.yaml or in Cloud Monarch. This metric is meant for
        callers' use only. Since this metric is not defined in the monitoring
        backend, reporting on this metric will result in an error.
      reconciliationErrors: Indicates the decision of the reconciliation end.
      serviceConfigId: ID of the actual config used to process the request.
    """

    operationId = _messages.StringField(1)
    quotaMetrics = _messages.MessageField('MetricValueSet', 2, repeated=True)
    reconciliationErrors = _messages.MessageField('QuotaError', 3, repeated=True)
    serviceConfigId = _messages.StringField(4)


class ExplicitBuckets(_messages.Message):
    """Describing buckets with arbitrary user-provided width.

    Fields:
      bounds: 'bound' is a list of strictly increasing boundaries between
        buckets. Note that a list of length N-1 defines N buckets because of
        fenceposting. See comments on `bucket_options` for details.  The i'th
        finite bucket covers the interval   [bound[i-1], bound[i]) where i
        ranges from 1 to bound_size() - 1. Note that there are no finite
        buckets at all if 'bound' only contains a single element; in that
        special case the single bound defines the boundary between the
        underflow and overflow buckets.  bucket number                   lower
        bound    upper bound  i == 0 (underflow)              -inf
        bound[i]  0 < i < bound_size()            bound[i-1]     bound[i]  i
        == bound_size() (overflow)    bound[i-1]     +inf
    """

    bounds = _messages.FloatField(1, repeated=True)


class ExponentialBuckets(_messages.Message):
    """Describing buckets with exponentially growing width.

    Fields:
      growthFactor: The i'th exponential bucket covers the interval   [scale *
        growth_factor^(i-1), scale * growth_factor^i) where i ranges from 1 to
        num_finite_buckets inclusive. Must be larger than 1.0.
      numFiniteBuckets: The number of finite buckets. With the underflow and
        overflow buckets, the total number of buckets is `num_finite_buckets`
        + 2. See comments on `bucket_options` for details.
      scale: The i'th exponential bucket covers the interval   [scale *
        growth_factor^(i-1), scale * growth_factor^i) where i ranges from 1 to
        num_finite_buckets inclusive. Must be > 0.
    """

    growthFactor = _messages.FloatField(1)
    numFiniteBuckets = _messages.IntegerField(2, variant=_messages.Variant.INT32)
    scale = _messages.FloatField(3)


class LinearBuckets(_messages.Message):
    """Describing buckets with constant width.

    Fields:
      numFiniteBuckets: The number of finite buckets. With the underflow and
        overflow buckets, the total number of buckets is `num_finite_buckets`
        + 2. See comments on `bucket_options` for details.
      offset: The i'th linear bucket covers the interval   [offset + (i-1) *
        width, offset + i * width) where i ranges from 1 to
        num_finite_buckets, inclusive.
      width: The i'th linear bucket covers the interval   [offset + (i-1) *
        width, offset + i * width) where i ranges from 1 to
        num_finite_buckets, inclusive. Must be strictly positive.
    """

    numFiniteBuckets = _messages.IntegerField(1, variant=_messages.Variant.INT32)
    offset = _messages.FloatField(2)
    width = _messages.FloatField(3)


class LogEntry(_messages.Message):
    """An individual log entry.

    Enums:
      SeverityValueValuesEnum: The severity of the log entry. The default
        value is `LogSeverity.DEFAULT`.

    Messages:
      LabelsValue: A set of user-defined (key, value) data that provides
        additional information about the log entry.
      ProtoPayloadValue: The log entry payload, represented as a protocol
        buffer that is expressed as a JSON object. You can only pass
        `protoPayload` values that belong to a set of approved types.
      StructPayloadValue: The log entry payload, represented as a structure
        that is expressed as a JSON object.

    Fields:
      insertId: A unique ID for the log entry used for deduplication. If
        omitted, the implementation will generate one based on operation_id.
      labels: A set of user-defined (key, value) data that provides additional
        information about the log entry.
      name: Required. The log to which this log entry belongs. Examples:
        `"syslog"`, `"book_log"`.
      protoPayload: The log entry payload, represented as a protocol buffer
        that is expressed as a JSON object. You can only pass `protoPayload`
        values that belong to a set of approved types.
      severity: The severity of the log entry. The default value is
        `LogSeverity.DEFAULT`.
      structPayload: The log entry payload, represented as a structure that is
        expressed as a JSON object.
      textPayload: The log entry payload, represented as a Unicode string
        (UTF-8).
      timestamp: The time the event described by the log entry occurred. If
        omitted, defaults to operation start time.
    """

    class SeverityValueValuesEnum(_messages.Enum):
        """The severity of the log entry. The default value is
        `LogSeverity.DEFAULT`.

        Values:
          DEFAULT: (0) The log entry has no assigned severity level.
          DEBUG: (100) Debug or trace information.
          INFO: (200) Routine information, such as ongoing status or
            performance.
          NOTICE: (300) Normal but significant events, such as start up, shut
            down, or a configuration change.
          WARNING: (400) Warning events might cause problems.
          ERROR: (500) Error events are likely to cause problems.
          CRITICAL: (600) Critical events cause more severe problems or
            outages.
          ALERT: (700) A person must take an action immediately.
          EMERGENCY: (800) One or more systems are unusable.
        """
        DEFAULT = 0
        DEBUG = 1
        INFO = 2
        NOTICE = 3
        WARNING = 4
        ERROR = 5
        CRITICAL = 6
        ALERT = 7
        EMERGENCY = 8

    @encoding.MapUnrecognizedFields('additionalProperties')
    class LabelsValue(_messages.Message):
        """A set of user-defined (key, value) data that provides additional
        information about the log entry.

        Messages:
          AdditionalProperty: An additional property for a LabelsValue object.

        Fields:
          additionalProperties: Additional properties of type LabelsValue
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a LabelsValue object.

            Fields:
              key: Name of the additional property.
              value: A string attribute.
            """

            key = _messages.StringField(1)
            value = _messages.StringField(2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    @encoding.MapUnrecognizedFields('additionalProperties')
    class ProtoPayloadValue(_messages.Message):
        """The log entry payload, represented as a protocol buffer that is
        expressed as a JSON object. You can only pass `protoPayload` values
        that belong to a set of approved types.

        Messages:
          AdditionalProperty: An additional property for a ProtoPayloadValue
            object.

        Fields:
          additionalProperties: Properties of the object. Contains field @type
            with type URL.
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a ProtoPayloadValue object.

            Fields:
              key: Name of the additional property.
              value: A extra_types.JsonValue attribute.
            """

            key = _messages.StringField(1)
            value = _messages.MessageField('extra_types.JsonValue', 2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    @encoding.MapUnrecognizedFields('additionalProperties')
    class StructPayloadValue(_messages.Message):
        """The log entry payload, represented as a structure that is expressed
        as a JSON object.

        Messages:
          AdditionalProperty: An additional property for a StructPayloadValue
            object.

        Fields:
          additionalProperties: Properties of the object.
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a StructPayloadValue object.

            Fields:
              key: Name of the additional property.
              value: A extra_types.JsonValue attribute.
            """

            key = _messages.StringField(1)
            value = _messages.MessageField('extra_types.JsonValue', 2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    insertId = _messages.StringField(1)
    labels = _messages.MessageField('LabelsValue', 2)
    name = _messages.StringField(3)
    protoPayload = _messages.MessageField('ProtoPayloadValue', 4)
    severity = _messages.EnumField('SeverityValueValuesEnum', 5)
    structPayload = _messages.MessageField('StructPayloadValue', 6)
    textPayload = _messages.StringField(7)
    timestamp = _messages.StringField(8)


class MetricValue(_messages.Message):
    """Represents a single metric value.

    Messages:
      LabelsValue: The labels describing the metric value. See comments on
        google.api.servicecontrol.v1.Operation.labels for the overriding
        relationship.

    Fields:
      boolValue: A boolean value.
      distributionValue: A distribution value.
      doubleValue: A double precision floating point value.
      endTime: The end of the time period over which this metric value's
        measurement applies.
      int64Value: A signed 64-bit integer value.
      labels: The labels describing the metric value. See comments on
        google.api.servicecontrol.v1.Operation.labels for the overriding
        relationship.
      moneyValue: A money value.
      startTime: The start of the time period over which this metric value's
        measurement applies. The time period has different semantics for
        different metric types (cumulative, delta, and gauge). See the metric
        definition documentation in the service configuration for details.
      stringValue: A text string value.
    """

    @encoding.MapUnrecognizedFields('additionalProperties')
    class LabelsValue(_messages.Message):
        """The labels describing the metric value. See comments on
        google.api.servicecontrol.v1.Operation.labels for the overriding
        relationship.

        Messages:
          AdditionalProperty: An additional property for a LabelsValue object.

        Fields:
          additionalProperties: Additional properties of type LabelsValue
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a LabelsValue object.

            Fields:
              key: Name of the additional property.
              value: A string attribute.
            """

            key = _messages.StringField(1)
            value = _messages.StringField(2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    boolValue = _messages.BooleanField(1)
    distributionValue = _messages.MessageField('Distribution', 2)
    doubleValue = _messages.FloatField(3)
    endTime = _messages.StringField(4)
    int64Value = _messages.IntegerField(5)
    labels = _messages.MessageField('LabelsValue', 6)
    moneyValue = _messages.MessageField('Money', 7)
    startTime = _messages.StringField(8)
    stringValue = _messages.StringField(9)


class MetricValueSet(_messages.Message):
    """Represents a set of metric values in the same metric. Each metric value
    in the set should have a unique combination of start time, end time, and
    label values.

    Fields:
      metricName: The metric name defined in the service configuration.
      metricValues: The values in this metric.
    """

    metricName = _messages.StringField(1)
    metricValues = _messages.MessageField('MetricValue', 2, repeated=True)


class Money(_messages.Message):
    """Represents an amount of money with its currency type.

    Fields:
      currencyCode: The 3-letter currency code defined in ISO 4217.
      nanos: Number of nano (10^-9) units of the amount. The value must be
        between -999,999,999 and +999,999,999 inclusive. If `units` is
        positive, `nanos` must be positive or zero. If `units` is zero,
        `nanos` can be positive, zero, or negative. If `units` is negative,
        `nanos` must be negative or zero. For example $-1.75 is represented as
        `units`=-1 and `nanos`=-750,000,000.
      units: The whole units of the amount. For example if `currencyCode` is
        `"USD"`, then 1 unit is one US dollar.
    """

    currencyCode = _messages.StringField(1)
    nanos = _messages.IntegerField(2, variant=_messages.Variant.INT32)
    units = _messages.IntegerField(3)


class Operation(_messages.Message):
    """Represents information regarding an operation.

    Enums:
      ImportanceValueValuesEnum: DO NOT USE. This is an experimental field.

    Messages:
      LabelsValue: Labels describing the operation. Only the following labels
        are allowed:  - Labels describing monitored resources as defined in
        the service configuration. - Default labels of metric values. When
        specified, labels defined in the   metric value override these
        default. - The following labels defined by Google Cloud Platform:
        - `cloud.googleapis.com/location` describing the location where the
        operation happened,     - `servicecontrol.googleapis.com/user_agent`
        describing the user agent        of the API request,     -
        `servicecontrol.googleapis.com/service_agent` describing the service
        used to handle the API request (e.g. ESP),     -
        `servicecontrol.googleapis.com/platform` describing the platform
        where the API is served (e.g. GAE, GCE, GKE).
      UserLabelsValue: User defined labels for the resource that this
        operation is associated with.

    Fields:
      consumerId: Identity of the consumer who is using the service. This
        field should be filled in for the operations initiated by a consumer,
        but not for service-initiated operations that are not related to a
        specific consumer.  This can be in one of the following formats:
        project:<project_id>,   project_number:<project_number>,
        api_key:<api_key>.
      endTime: End time of the operation. Required when the operation is used
        in ServiceController.Report, but optional when the operation is used
        in ServiceController.Check.
      importance: DO NOT USE. This is an experimental field.
      labels: Labels describing the operation. Only the following labels are
        allowed:  - Labels describing monitored resources as defined in   the
        service configuration. - Default labels of metric values. When
        specified, labels defined in the   metric value override these
        default. - The following labels defined by Google Cloud Platform:
        - `cloud.googleapis.com/location` describing the location where the
        operation happened,     - `servicecontrol.googleapis.com/user_agent`
        describing the user agent        of the API request,     -
        `servicecontrol.googleapis.com/service_agent` describing the service
        used to handle the API request (e.g. ESP),     -
        `servicecontrol.googleapis.com/platform` describing the platform
        where the API is served (e.g. GAE, GCE, GKE).
      logEntries: Represents information to be logged.
      metricValueSets: Represents information about this operation. Each
        MetricValueSet corresponds to a metric defined in the service
        configuration. The data type used in the MetricValueSet must agree
        with the data type specified in the metric definition.  Within a
        single operation, it is not allowed to have more than one MetricValue
        instances that have the same metric names and identical label value
        combinations. If a request has such duplicated MetricValue instances,
        the entire request is rejected with an invalid argument error.
      operationId: Identity of the operation. This must be unique within the
        scope of the service that generated the operation. If the service
        calls Check() and Report() on the same operation, the two calls should
        carry the same id.  UUID version 4 is recommended, though not
        required. In scenarios where an operation is computed from existing
        information and an idempotent id is desirable for deduplication
        purpose, UUID version 5 is recommended. See RFC 4122 for details.
      operationName: Fully qualified name of the operation. Reserved for
        future use.
      quotaProperties: Represents the properties needed for quota check.
        Applicable only if this operation is for a quota check request.
      resourceContainer: The resource name of the parent of a resource in the
        resource hierarchy.  This can be in one of the following formats:
        - \u201cprojects/<project-id or project-number>\u201d     - \u201cfolders/<folder-
        id>\u201d     - \u201corganizations/<organization-id>\u201d
      startTime: Required. Start time of the operation.
      userLabels: User defined labels for the resource that this operation is
        associated with.
    """

    class ImportanceValueValuesEnum(_messages.Enum):
        """DO NOT USE. This is an experimental field.

        Values:
          LOW: The API implementation may cache and aggregate the data. The
            data may be lost when rare and unexpected system failures occur.
          HIGH: The API implementation doesn't cache and aggregate the data.
            If the method returns successfully, it's guaranteed that the data
            has been persisted in durable storage.
          DEBUG: In addition to the behavior described in HIGH, DEBUG enables
            additional validation logic that is only useful during the
            onboarding process. This is only available to Google internal
            services and the service must be whitelisted by chemist-
            dev@google.com in order to use this level.
        """
        LOW = 0
        HIGH = 1
        DEBUG = 2

    @encoding.MapUnrecognizedFields('additionalProperties')
    class LabelsValue(_messages.Message):
        """Labels describing the operation. Only the following labels are
        allowed:  - Labels describing monitored resources as defined in   the
        service configuration. - Default labels of metric values. When
        specified, labels defined in the   metric value override these
        default. - The following labels defined by Google Cloud Platform:
        - `cloud.googleapis.com/location` describing the location where the
        operation happened,     - `servicecontrol.googleapis.com/user_agent`
        describing the user agent        of the API request,     -
        `servicecontrol.googleapis.com/service_agent` describing the service
        used to handle the API request (e.g. ESP),     -
        `servicecontrol.googleapis.com/platform` describing the platform
        where the API is served (e.g. GAE, GCE, GKE).

        Messages:
          AdditionalProperty: An additional property for a LabelsValue object.

        Fields:
          additionalProperties: Additional properties of type LabelsValue
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a LabelsValue object.

            Fields:
              key: Name of the additional property.
              value: A string attribute.
            """

            key = _messages.StringField(1)
            value = _messages.StringField(2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    @encoding.MapUnrecognizedFields('additionalProperties')
    class UserLabelsValue(_messages.Message):
        """User defined labels for the resource that this operation is
        associated with.

        Messages:
          AdditionalProperty: An additional property for a UserLabelsValue
            object.

        Fields:
          additionalProperties: Additional properties of type UserLabelsValue
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a UserLabelsValue object.

            Fields:
              key: Name of the additional property.
              value: A string attribute.
            """

            key = _messages.StringField(1)
            value = _messages.StringField(2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    consumerId = _messages.StringField(1)
    endTime = _messages.StringField(2)
    importance = _messages.EnumField('ImportanceValueValuesEnum', 3)
    labels = _messages.MessageField('LabelsValue', 4)
    logEntries = _messages.MessageField('LogEntry', 5, repeated=True)
    metricValueSets = _messages.MessageField('MetricValueSet', 6, repeated=True)
    operationId = _messages.StringField(7)
    operationName = _messages.StringField(8)
    quotaProperties = _messages.MessageField('QuotaProperties', 9)
    resourceContainer = _messages.StringField(10)
    startTime = _messages.StringField(11)
    userLabels = _messages.MessageField('UserLabelsValue', 12)


class QuotaError(_messages.Message):
    """A QuotaError object.

    Enums:
      CodeValueValuesEnum: Error code.

    Fields:
      code: Error code.
      description: Free-form text that provides details on the cause of the
        error.
      subject: Subject to whom this error applies. See the specific enum for
        more details on this field. For example, "clientip:<ip address of
        client>" or "project:<Google developer project id>".
    """

    class CodeValueValuesEnum(_messages.Enum):
        """Error code.

        Values:
          UNSPECIFIED: This is never used.
          RESOURCE_EXHAUSTED: Quota allocation failed. Same as
            google.rpc.Code.RESOURCE_EXHAUSTED.
          PROJECT_SUSPENDED: Consumer project has been suspended.
          SERVICE_NOT_ENABLED: Consumer has not enabled the service.
          BILLING_NOT_ACTIVE: Consumer cannot access the service because
            billing is disabled.
          PROJECT_DELETED: Consumer's project has been marked as deleted (soft
            deletion).
          PROJECT_INVALID: Consumer's project number or ID does not represent
            a valid project.
          IP_ADDRESS_BLOCKED: IP address of the consumer is invalid for the
            specific consumer project.
          REFERER_BLOCKED: Referer address of the consumer request is invalid
            for the specific consumer project.
          CLIENT_APP_BLOCKED: Client application of the consumer request is
            invalid for the specific consumer project.
          API_KEY_INVALID: Specified API key is invalid.
          API_KEY_EXPIRED: Specified API Key has expired.
          SPATULA_HEADER_INVALID: Consumer's spatula header is invalid.
          LOAS_ROLE_INVALID: The consumer's LOAS role is invalid.
          NO_LOAS_PROJECT: The consumer's LOAS role has no associated project.
          PROJECT_STATUS_UNAVAILABLE: The backend server for looking up
            project id/number is unavailable.
          SERVICE_STATUS_UNAVAILABLE: The backend server for checking service
            status is unavailable.
          BILLING_STATUS_UNAVAILABLE: The backend server for checking billing
            status is unavailable.
          QUOTA_SYSTEM_UNAVAILABLE: The backend server for checking quota
            limits is unavailable.
        """
        UNSPECIFIED = 0
        RESOURCE_EXHAUSTED = 1
        PROJECT_SUSPENDED = 2
        SERVICE_NOT_ENABLED = 3
        BILLING_NOT_ACTIVE = 4
        PROJECT_DELETED = 5
        PROJECT_INVALID = 6
        IP_ADDRESS_BLOCKED = 7
        REFERER_BLOCKED = 8
        CLIENT_APP_BLOCKED = 9
        API_KEY_INVALID = 10
        API_KEY_EXPIRED = 11
        SPATULA_HEADER_INVALID = 12
        LOAS_ROLE_INVALID = 13
        NO_LOAS_PROJECT = 14
        PROJECT_STATUS_UNAVAILABLE = 15
        SERVICE_STATUS_UNAVAILABLE = 16
        BILLING_STATUS_UNAVAILABLE = 17
        QUOTA_SYSTEM_UNAVAILABLE = 18

    code = _messages.EnumField('CodeValueValuesEnum', 1)
    description = _messages.StringField(2)
    subject = _messages.StringField(3)


class QuotaInfo(_messages.Message):
    """Contains the quota information for a quota check response.

    Messages:
      QuotaConsumedValue: Map of quota group name to the actual number of
        tokens consumed. If the quota check was not successful, then this will
        not be populated due to no quota consumption. Deprecated: Use
        quota_metrics to get per quota group usage.

    Fields:
      limitExceeded: Quota Metrics that have exceeded quota limits. For
        QuotaGroup-based quota, this is QuotaGroup.name For QuotaLimit-based
        quota, this is QuotaLimit.name See: google.api.Quota Deprecated: Use
        quota_metrics to get per quota group limit exceeded status.
      quotaConsumed: Map of quota group name to the actual number of tokens
        consumed. If the quota check was not successful, then this will not be
        populated due to no quota consumption. Deprecated: Use quota_metrics
        to get per quota group usage.
      quotaMetrics: Quota metrics to indicate the usage. Depending on the
        check request, one or more of the following metrics will be included:
        1. For rate quota, per quota group or per quota metric incremental
        usage will be specified using the following delta metric:
        "serviceruntime.googleapis.com/api/consumer/quota_used_count"  2. For
        allocation quota, per quota metric total usage will be specified using
        the following gauge metric:
        "serviceruntime.googleapis.com/allocation/consumer/quota_used_count"
        3. For both rate quota and allocation quota, the quota limit reached
        condition will be specified using the following boolean metric:
        "serviceruntime.googleapis.com/quota/exceeded"
    """

    @encoding.MapUnrecognizedFields('additionalProperties')
    class QuotaConsumedValue(_messages.Message):
        """Map of quota group name to the actual number of tokens consumed. If
        the quota check was not successful, then this will not be populated
        due to no quota consumption. Deprecated: Use quota_metrics to get per
        quota group usage.

        Messages:
          AdditionalProperty: An additional property for a QuotaConsumedValue
            object.

        Fields:
          additionalProperties: Additional properties of type
            QuotaConsumedValue
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a QuotaConsumedValue object.

            Fields:
              key: Name of the additional property.
              value: A integer attribute.
            """

            key = _messages.StringField(1)
            value = _messages.IntegerField(2, variant=_messages.Variant.INT32)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    limitExceeded = _messages.StringField(1, repeated=True)
    quotaConsumed = _messages.MessageField('QuotaConsumedValue', 2)
    quotaMetrics = _messages.MessageField('MetricValueSet', 3, repeated=True)


class QuotaOperation(_messages.Message):
    """Represents information regarding a quota operation.

    Enums:
      QuotaModeValueValuesEnum: Quota mode for this operation.

    Messages:
      LabelsValue: Labels describing the operation.

    Fields:
      consumerId: Identity of the consumer for whom this quota operation is
        being performed.  This can be in one of the following formats:
        project:<project_id>,   project_number:<project_number>,
        api_key:<api_key>.
      labels: Labels describing the operation.
      methodName: Fully qualified name of the API method for which this quota
        operation is requested. This name is used for matching quota rules or
        metric rules and billing status rules defined in service
        configuration. This field is not required if the quota operation is
        performed on non-API resources.  Example of an RPC method name:
        google.example.library.v1.LibraryService.CreateShelf
      operationId: Identity of the operation. This must be unique within the
        scope of the service that generated the operation. If the service
        calls AllocateQuota and ReleaseQuota on the same operation, the two
        calls should carry the same ID.  UUID version 4 is recommended, though
        not required. In scenarios where an operation is computed from
        existing information and an idempotent id is desirable for
        deduplication purpose, UUID version 5 is recommended. See RFC 4122 for
        details.
      quotaMetrics: Represents information about this operation. Each
        MetricValueSet corresponds to a metric defined in the service
        configuration. The data type used in the MetricValueSet must agree
        with the data type specified in the metric definition.  Within a
        single operation, it is not allowed to have more than one MetricValue
        instances that have the same metric names and identical label value
        combinations. If a request has such duplicated MetricValue instances,
        the entire request is rejected with an invalid argument error.
      quotaMode: Quota mode for this operation.
    """

    class QuotaModeValueValuesEnum(_messages.Enum):
        """Quota mode for this operation.

        Values:
          UNSPECIFIED: <no description>
          NORMAL: For AllocateQuota request, allocates quota for the amount
            specified in the service configuration or specified using the
            quota metrics. If the amount is higher than the available quota,
            allocation error will be returned and no quota will be allocated.
            For ReleaseQuota request, this mode is supported only for precise
            quota limits. In this case, this operation releases quota for the
            amount specified in the service configuration or specified using
            the quota metrics. If the release can make used quota negative,
            release error will be returned and no quota will be released.
          BEST_EFFORT: For AllocateQuota request, this mode is supported only
            for imprecise quota limits. In this case, the operation allocates
            quota for the amount specified in the service configuration or
            specified using the quota metrics. If the amount is higher than
            the available quota, request does not fail but all available quota
            will be allocated. For ReleaseQuota request, this mode is
            supported for both precise quota limits and imprecise quota
            limits. In this case, this operation releases quota for the amount
            specified in the service configuration or specified using the
            quota metrics. If the release can make used quota negative,
            request does not fail but only the used quota will be released.
            After the ReleaseQuota request completes, the used quota will be
            0, and never goes to negative.
          CHECK_ONLY: For AllocateQuota request, only checks if there is
            enough quota available and does not change the available quota. No
            lock is placed on the available quota either. Not supported for
            ReleaseQuota request.
        """
        UNSPECIFIED = 0
        NORMAL = 1
        BEST_EFFORT = 2
        CHECK_ONLY = 3

    @encoding.MapUnrecognizedFields('additionalProperties')
    class LabelsValue(_messages.Message):
        """Labels describing the operation.

        Messages:
          AdditionalProperty: An additional property for a LabelsValue object.

        Fields:
          additionalProperties: Additional properties of type LabelsValue
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a LabelsValue object.

            Fields:
              key: Name of the additional property.
              value: A string attribute.
            """

            key = _messages.StringField(1)
            value = _messages.StringField(2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    consumerId = _messages.StringField(1)
    labels = _messages.MessageField('LabelsValue', 2)
    methodName = _messages.StringField(3)
    operationId = _messages.StringField(4)
    quotaMetrics = _messages.MessageField('MetricValueSet', 5, repeated=True)
    quotaMode = _messages.EnumField('QuotaModeValueValuesEnum', 6)


class QuotaProperties(_messages.Message):
    """Represents the properties needed for quota operations.

    Enums:
      QuotaModeValueValuesEnum: Quota mode for this operation.

    Messages:
      LimitByIdsValue: LimitType IDs that should be used for checking quota.
        Key in this map should be a valid LimitType string, and the value is
        the ID to be used. For example, an entry <USER, 123> will cause all
        user quota limits to use 123 as the user ID. See
        google/api/quota.proto for the definition of LimitType.
        CLIENT_PROJECT: Not supported. USER: Value of this entry will be used
        for enforcing user-level quota       limits. If none specified, caller
        IP passed in the       servicecontrol.googleapis.com/caller_ip label
        will be used instead.       If the server cannot resolve a value for
        this LimitType, an error       will be thrown. No validation will be
        performed on this ID. Deprecated: use
        servicecontrol.googleapis.com/user label to send user ID.

    Fields:
      limitByIds: LimitType IDs that should be used for checking quota. Key in
        this map should be a valid LimitType string, and the value is the ID
        to be used. For example, an entry <USER, 123> will cause all user
        quota limits to use 123 as the user ID. See google/api/quota.proto for
        the definition of LimitType. CLIENT_PROJECT: Not supported. USER:
        Value of this entry will be used for enforcing user-level quota
        limits. If none specified, caller IP passed in the
        servicecontrol.googleapis.com/caller_ip label will be used instead.
        If the server cannot resolve a value for this LimitType, an error
        will be thrown. No validation will be performed on this ID.
        Deprecated: use servicecontrol.googleapis.com/user label to send user
        ID.
      quotaMode: Quota mode for this operation.
    """

    class QuotaModeValueValuesEnum(_messages.Enum):
        """Quota mode for this operation.

        Values:
          ACQUIRE: Decreases available quota by the cost specified for the
            operation. If cost is higher than available quota, operation fails
            and returns error.
          ACQUIRE_BEST_EFFORT: Decreases available quota by the cost specified
            for the operation. If cost is higher than available quota,
            operation does not fail and available quota goes down to zero but
            it returns error.
          CHECK: Does not change any available quota. Only checks if there is
            enough quota. No lock is placed on the checked tokens neither.
          RELEASE: Increases available quota by the operation cost specified
            for the operation.
        """
        ACQUIRE = 0
        ACQUIRE_BEST_EFFORT = 1
        CHECK = 2
        RELEASE = 3

    @encoding.MapUnrecognizedFields('additionalProperties')
    class LimitByIdsValue(_messages.Message):
        """LimitType IDs that should be used for checking quota. Key in this
        map should be a valid LimitType string, and the value is the ID to be
        used. For example, an entry <USER, 123> will cause all user quota
        limits to use 123 as the user ID. See google/api/quota.proto for the
        definition of LimitType. CLIENT_PROJECT: Not supported. USER: Value of
        this entry will be used for enforcing user-level quota       limits.
        If none specified, caller IP passed in the
        servicecontrol.googleapis.com/caller_ip label will be used instead.
        If the server cannot resolve a value for this LimitType, an error
        will be thrown. No validation will be performed on this ID.
        Deprecated: use servicecontrol.googleapis.com/user label to send user
        ID.

        Messages:
          AdditionalProperty: An additional property for a LimitByIdsValue
            object.

        Fields:
          additionalProperties: Additional properties of type LimitByIdsValue
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a LimitByIdsValue object.

            Fields:
              key: Name of the additional property.
              value: A string attribute.
            """

            key = _messages.StringField(1)
            value = _messages.StringField(2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    limitByIds = _messages.MessageField('LimitByIdsValue', 1)
    quotaMode = _messages.EnumField('QuotaModeValueValuesEnum', 2)


class ReleaseQuotaRequest(_messages.Message):
    """Request message for the ReleaseQuota method.

    Fields:
      releaseOperation: Operation that describes the quota release.
      serviceConfigId: Specifies which version of service configuration should
        be used to process the request. If unspecified or no matching version
        can be found, the latest one will be used.
    """

    releaseOperation = _messages.MessageField('QuotaOperation', 1)
    serviceConfigId = _messages.StringField(2)


class ReleaseQuotaResponse(_messages.Message):
    """Response message for the ReleaseQuota method.

    Fields:
      operationId: The same operation_id value used in the
        ReleaseQuotaRequest. Used for logging and diagnostics purposes.
      quotaMetrics: Quota metrics to indicate the result of release. Depending
        on the request, one or more of the following metrics will be included:
        1. For rate quota, per quota group or per quota metric released amount
        will be specified using the following delta metric:
        "serviceruntime.googleapis.com/api/consumer/quota_refund_count"  2.
        For allocation quota, per quota metric total usage will be specified
        using the following gauge metric:
        "serviceruntime.googleapis.com/allocation/consumer/quota_used_count"
        3. For allocation quota, value for each quota limit associated with
        the metrics will be specified using the following gauge metric:
        "serviceruntime.googleapis.com/quota/limit"
      releaseErrors: Indicates the decision of the release.
      serviceConfigId: ID of the actual config used to process the request.
    """

    operationId = _messages.StringField(1)
    quotaMetrics = _messages.MessageField('MetricValueSet', 2, repeated=True)
    releaseErrors = _messages.MessageField('QuotaError', 3, repeated=True)
    serviceConfigId = _messages.StringField(4)


class ReportError(_messages.Message):
    """Represents the processing error of one `Operation` in the request.

    Fields:
      operationId: The Operation.operation_id value from the request.
      status: Details of the error when processing the `Operation`.
    """

    operationId = _messages.StringField(1)
    status = _messages.MessageField('Status', 2)


class ReportInfo(_messages.Message):
    """A ReportInfo object.

    Fields:
      operationId: The Operation.operation_id value from the request.
      quotaInfo: Quota usage info when processing the `Operation`.
    """

    operationId = _messages.StringField(1)
    quotaInfo = _messages.MessageField('QuotaInfo', 2)


class ReportRequest(_messages.Message):
    """Request message for the Report method.

    Fields:
      operations: Operations to be reported.  Typically the service should
        report one operation per request. Putting multiple operations into a
        single request is allowed, but should be used only when multiple
        operations are natually available at the time of the report.  If
        multiple operations are in a single request, the total request size
        should be no larger than 1MB. See ReportResponse.report_errors for
        partial failure behavior.
      serviceConfigId: Specifies which version of service config should be
        used to process the request.  If unspecified or no matching version
        can be found, the latest one will be used.
    """

    operations = _messages.MessageField('Operation', 1, repeated=True)
    serviceConfigId = _messages.StringField(2)


class ReportResponse(_messages.Message):
    """Response message for the Report method.

    Fields:
      reportErrors: Partial failures, one for each `Operation` in the request
        that failed processing. There are three possible combinations of the
        RPC status:  1. The combination of a successful RPC status and an
        empty `report_errors`    list indicates a complete success where all
        `Operations` in the    request are processed successfully. 2. The
        combination of a successful RPC status and a non-empty
        `report_errors` list indicates a partial success where some
        `Operations` in the request succeeded. Each    `Operation` that failed
        processing has a corresponding item    in this list. 3. A failed RPC
        status indicates a general non-deterministic failure.    When this
        happens, it's impossible to know which of the    'Operations' in the
        request succeeded or failed.
      reportInfos: Quota usage for each quota release `Operation` request.
        Fully or partially failed quota release request may or may not be
        present in `report_quota_info`. For example, a failed quota release
        request will have the current quota usage info when precise quota
        library returns the info. A deadline exceeded quota request will not
        have quota usage info.  If there is no quota release request,
        report_quota_info will be empty.
      serviceConfigId: The actual config id used to process the request.
    """

    reportErrors = _messages.MessageField('ReportError', 1, repeated=True)
    reportInfos = _messages.MessageField('ReportInfo', 2, repeated=True)
    serviceConfigId = _messages.StringField(3)


class RequestMetadata(_messages.Message):
    """Metadata about the request.

    Fields:
      callerIp: The IP address of the caller.
      callerSuppliedUserAgent: The user agent of the caller. This information
        is not authenticated and should be treated accordingly. For example:
        +   `google-api-python-client/1.4.0`:     The request was made by the
        Google API client for Python. +   `Cloud SDK Command Line Tool
        apitools-client/1.0 gcloud/0.9.62`:     The request was made by the
        Google Cloud SDK CLI (gcloud). +   `AppEngine-Google;
        (+http://code.google.com/appengine; appid: s~my-project`:     The
        request was made from the `my-project` App Engine app.
    """

    callerIp = _messages.StringField(1)
    callerSuppliedUserAgent = _messages.StringField(2)


class ServicecontrolServicesAllocateQuotaRequest(_messages.Message):
    """A ServicecontrolServicesAllocateQuotaRequest object.

    Fields:
      allocateQuotaRequest: A AllocateQuotaRequest resource to be passed as
        the request body.
      serviceName: Name of the service as specified in the service
        configuration. For example, `"pubsub.googleapis.com"`.  See
        google.api.Service for the definition of a service name.
    """

    allocateQuotaRequest = _messages.MessageField('AllocateQuotaRequest', 1)
    serviceName = _messages.StringField(2, required=True)


class ServicecontrolServicesCheckRequest(_messages.Message):
    """A ServicecontrolServicesCheckRequest object.

    Fields:
      checkRequest: A CheckRequest resource to be passed as the request body.
      serviceName: The service name as specified in its service configuration.
        For example, `"pubsub.googleapis.com"`.  See google.api.Service for
        the definition of a service name.
    """

    checkRequest = _messages.MessageField('CheckRequest', 1)
    serviceName = _messages.StringField(2, required=True)


class ServicecontrolServicesEndReconciliationRequest(_messages.Message):
    """A ServicecontrolServicesEndReconciliationRequest object.

    Fields:
      endReconciliationRequest: A EndReconciliationRequest resource to be
        passed as the request body.
      serviceName: Name of the service as specified in the service
        configuration. For example, `"pubsub.googleapis.com"`.  See
        google.api.Service for the definition of a service name.
    """

    endReconciliationRequest = _messages.MessageField('EndReconciliationRequest', 1)
    serviceName = _messages.StringField(2, required=True)


class ServicecontrolServicesReleaseQuotaRequest(_messages.Message):
    """A ServicecontrolServicesReleaseQuotaRequest object.

    Fields:
      releaseQuotaRequest: A ReleaseQuotaRequest resource to be passed as the
        request body.
      serviceName: Name of the service as specified in the service
        configuration. For example, `"pubsub.googleapis.com"`.  See
        google.api.Service for the definition of a service name.
    """

    releaseQuotaRequest = _messages.MessageField('ReleaseQuotaRequest', 1)
    serviceName = _messages.StringField(2, required=True)


class ServicecontrolServicesReportRequest(_messages.Message):
    """A ServicecontrolServicesReportRequest object.

    Fields:
      reportRequest: A ReportRequest resource to be passed as the request
        body.
      serviceName: The service name as specified in its service configuration.
        For example, `"pubsub.googleapis.com"`.  See google.api.Service for
        the definition of a service name.
    """

    reportRequest = _messages.MessageField('ReportRequest', 1)
    serviceName = _messages.StringField(2, required=True)


class ServicecontrolServicesStartReconciliationRequest(_messages.Message):
    """A ServicecontrolServicesStartReconciliationRequest object.

    Fields:
      serviceName: Name of the service as specified in the service
        configuration. For example, `"pubsub.googleapis.com"`.  See
        google.api.Service for the definition of a service name.
      startReconciliationRequest: A StartReconciliationRequest resource to be
        passed as the request body.
    """

    serviceName = _messages.StringField(1, required=True)
    startReconciliationRequest = _messages.MessageField('StartReconciliationRequest', 2)


class StandardQueryParameters(_messages.Message):
    """Query parameters accepted by all methods.

    Enums:
      FXgafvValueValuesEnum: V1 error format.
      AltValueValuesEnum: Data format for response.

    Fields:
      f__xgafv: V1 error format.
      access_token: OAuth access token.
      alt: Data format for response.
      bearer_token: OAuth bearer token.
      callback: JSONP
      fields: Selector specifying which fields to include in a partial
        response.
      key: API key. Your API key identifies your project and provides you with
        API access, quota, and reports. Required unless you provide an OAuth
        2.0 token.
      oauth_token: OAuth 2.0 token for the current user.
      pp: Pretty-print response.
      prettyPrint: Returns response with indentations and line breaks.
      quotaUser: Available to use for quota purposes for server-side
        applications. Can be any arbitrary string assigned to a user, but
        should not exceed 40 characters.
      trace: A tracing token of the form "token:<tokenid>" to include in api
        requests.
      uploadType: Legacy upload protocol for media (e.g. "media",
        "multipart").
      upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
    """

    class AltValueValuesEnum(_messages.Enum):
        """Data format for response.

        Values:
          json: Responses with Content-Type of application/json
          media: Media download with context-dependent Content-Type
          proto: Responses with Content-Type of application/x-protobuf
        """
        json = 0
        media = 1
        proto = 2

    class FXgafvValueValuesEnum(_messages.Enum):
        """V1 error format.

        Values:
          _1: v1 error format
          _2: v2 error format
        """
        _1 = 0
        _2 = 1

    f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
    access_token = _messages.StringField(2)
    alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
    bearer_token = _messages.StringField(4)
    callback = _messages.StringField(5)
    fields = _messages.StringField(6)
    key = _messages.StringField(7)
    oauth_token = _messages.StringField(8)
    pp = _messages.BooleanField(9, default=True)
    prettyPrint = _messages.BooleanField(10, default=True)
    quotaUser = _messages.StringField(11)
    trace = _messages.StringField(12)
    uploadType = _messages.StringField(13)
    upload_protocol = _messages.StringField(14)


class StartReconciliationRequest(_messages.Message):
    """A StartReconciliationRequest object.

    Fields:
      reconciliationOperation: Operation that describes the quota
        reconciliation.
      serviceConfigId: Specifies which version of service configuration should
        be used to process the request. If unspecified or no matching version
        can be found, the latest one will be used.
    """

    reconciliationOperation = _messages.MessageField('QuotaOperation', 1)
    serviceConfigId = _messages.StringField(2)


class StartReconciliationResponse(_messages.Message):
    """A StartReconciliationResponse object.

    Fields:
      operationId: The same operation_id value used in the
        StartReconciliationRequest. Used for logging and diagnostics purposes.
      quotaMetrics: Metric values as tracked by One Platform before the start
        of reconciliation. The following metrics will be included:  1. Per
        quota metric total usage will be specified using the following gauge
        metric:
        "serviceruntime.googleapis.com/allocation/consumer/quota_used_count"
        2. Value for each quota limit associated with the metrics will be
        specified using the following gauge metric:
        "serviceruntime.googleapis.com/quota/limit"
      reconciliationErrors: Indicates the decision of the reconciliation
        start.
      serviceConfigId: ID of the actual config used to process the request.
    """

    operationId = _messages.StringField(1)
    quotaMetrics = _messages.MessageField('MetricValueSet', 2, repeated=True)
    reconciliationErrors = _messages.MessageField('QuotaError', 3, repeated=True)
    serviceConfigId = _messages.StringField(4)


class Status(_messages.Message):
    """The `Status` type defines a logical error model that is suitable for
    different programming environments, including REST APIs and RPC APIs. It
    is used by [gRPC](https://github.com/grpc). The error model is designed to
    be:  - Simple to use and understand for most users - Flexible enough to
    meet unexpected needs  # Overview  The `Status` message contains three
    pieces of data: error code, error message, and error details. The error
    code should be an enum value of google.rpc.Code, but it may accept
    additional error codes if needed.  The error message should be a
    developer-facing English message that helps developers *understand* and
    *resolve* the error. If a localized user-facing error message is needed,
    put the localized message in the error details or localize it in the
    client. The optional error details may contain arbitrary information about
    the error. There is a predefined set of error detail types in the package
    `google.rpc` which can be used for common error conditions.  # Language
    mapping  The `Status` message is the logical representation of the error
    model, but it is not necessarily the actual wire format. When the `Status`
    message is exposed in different client libraries and different wire
    protocols, it can be mapped differently. For example, it will likely be
    mapped to some exceptions in Java, but more likely mapped to some error
    codes in C.  # Other uses  The error model and the `Status` message can be
    used in a variety of environments, either with or without APIs, to provide
    a consistent developer experience across different environments.  Example
    uses of this error model include:  - Partial errors. If a service needs to
    return partial errors to the client,     it may embed the `Status` in the
    normal response to indicate the partial     errors.  - Workflow errors. A
    typical workflow has multiple steps. Each step may     have a `Status`
    message for error reporting purpose.  - Batch operations. If a client uses
    batch request and batch response, the     `Status` message should be used
    directly inside batch response, one for     each error sub-response.  -
    Asynchronous operations. If an API call embeds asynchronous operation
    results in its response, the status of those operations should be
    represented directly using the `Status` message.  - Logging. If some API
    errors are stored in logs, the message `Status` could     be used directly
    after any stripping needed for security/privacy reasons.

    Messages:
      DetailsValueListEntry: A DetailsValueListEntry object.

    Fields:
      code: The status code, which should be an enum value of google.rpc.Code.
      details: A list of messages that carry the error details.  There will be
        a common set of message types for APIs to use.
      message: A developer-facing error message, which should be in English.
        Any user-facing error message should be localized and sent in the
        google.rpc.Status.details field, or localized by the client.
    """

    @encoding.MapUnrecognizedFields('additionalProperties')
    class DetailsValueListEntry(_messages.Message):
        """A DetailsValueListEntry object.

        Messages:
          AdditionalProperty: An additional property for a
            DetailsValueListEntry object.

        Fields:
          additionalProperties: Properties of the object. Contains field @type
            with type URL.
        """

        class AdditionalProperty(_messages.Message):
            """An additional property for a DetailsValueListEntry object.

            Fields:
              key: Name of the additional property.
              value: A extra_types.JsonValue attribute.
            """

            key = _messages.StringField(1)
            value = _messages.MessageField('extra_types.JsonValue', 2)

        additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

    code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
    details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
    message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
