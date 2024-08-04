# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double, integer
from .validators.cloudfront import (
    cloudfront_access_control_allow_methods,
    cloudfront_cache_cookie_behavior,
    cloudfront_cache_header_behavior,
    cloudfront_cache_query_string_behavior,
    cloudfront_event_type,
    cloudfront_forward_type,
    cloudfront_frame_option,
    cloudfront_origin_request_cookie_behavior,
    cloudfront_origin_request_header_behavior,
    cloudfront_origin_request_query_string_behavior,
    cloudfront_referrer_policy,
    cloudfront_restriction_type,
    cloudfront_viewer_protocol_policy,
    priceclass_type,
    validate_network_port,
    validate_tags_or_list,
)


class CacheCookiesConfig(AWSProperty):
    """
    `CacheCookiesConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html>`__
    """

    props: PropsDictType = {
        "CookieBehavior": (cloudfront_cache_cookie_behavior, True),
        "Cookies": ([str], False),
    }


class CacheHeadersConfig(AWSProperty):
    """
    `CacheHeadersConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html>`__
    """

    props: PropsDictType = {
        "HeaderBehavior": (cloudfront_cache_header_behavior, True),
        "Headers": ([str], False),
    }


class CacheQueryStringsConfig(AWSProperty):
    """
    `CacheQueryStringsConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html>`__
    """

    props: PropsDictType = {
        "QueryStringBehavior": (cloudfront_cache_query_string_behavior, True),
        "QueryStrings": ([str], False),
    }


class ParametersInCacheKeyAndForwardedToOrigin(AWSProperty):
    """
    `ParametersInCacheKeyAndForwardedToOrigin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html>`__
    """

    props: PropsDictType = {
        "CookiesConfig": (CacheCookiesConfig, True),
        "EnableAcceptEncodingBrotli": (boolean, False),
        "EnableAcceptEncodingGzip": (boolean, True),
        "HeadersConfig": (CacheHeadersConfig, True),
        "QueryStringsConfig": (CacheQueryStringsConfig, True),
    }


class CachePolicyConfig(AWSProperty):
    """
    `CachePolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html>`__
    """

    props: PropsDictType = {
        "Comment": (str, False),
        "DefaultTTL": (double, True),
        "MaxTTL": (double, True),
        "MinTTL": (double, True),
        "Name": (str, True),
        "ParametersInCacheKeyAndForwardedToOrigin": (
            ParametersInCacheKeyAndForwardedToOrigin,
            True,
        ),
    }


class CachePolicy(AWSObject):
    """
    `CachePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html>`__
    """

    resource_type = "AWS::CloudFront::CachePolicy"

    props: PropsDictType = {
        "CachePolicyConfig": (CachePolicyConfig, True),
    }


class CloudFrontOriginAccessIdentityConfig(AWSProperty):
    """
    `CloudFrontOriginAccessIdentityConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html>`__
    """

    props: PropsDictType = {
        "Comment": (str, True),
    }


class CloudFrontOriginAccessIdentity(AWSObject):
    """
    `CloudFrontOriginAccessIdentity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html>`__
    """

    resource_type = "AWS::CloudFront::CloudFrontOriginAccessIdentity"

    props: PropsDictType = {
        "CloudFrontOriginAccessIdentityConfig": (
            CloudFrontOriginAccessIdentityConfig,
            True,
        ),
    }


class SingleHeaderPolicyConfig(AWSProperty):
    """
    `SingleHeaderPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig.html>`__
    """

    props: PropsDictType = {
        "Header": (str, True),
        "Value": (str, True),
    }


class SessionStickinessConfig(AWSProperty):
    """
    `SessionStickinessConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig.html>`__
    """

    props: PropsDictType = {
        "IdleTTL": (integer, True),
        "MaximumTTL": (integer, True),
    }


class SingleWeightPolicyConfig(AWSProperty):
    """
    `SingleWeightPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig.html>`__
    """

    props: PropsDictType = {
        "SessionStickinessConfig": (SessionStickinessConfig, False),
        "Weight": (double, True),
    }


class SingleHeaderConfig(AWSProperty):
    """
    `SingleHeaderConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig.html>`__
    """

    props: PropsDictType = {
        "Header": (str, True),
        "Value": (str, True),
    }


class SingleWeightConfig(AWSProperty):
    """
    `SingleWeightConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig.html>`__
    """

    props: PropsDictType = {
        "SessionStickinessConfig": (SessionStickinessConfig, False),
        "Weight": (double, True),
    }


class TrafficConfig(AWSProperty):
    """
    `TrafficConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html>`__
    """

    props: PropsDictType = {
        "SingleHeaderConfig": (SingleHeaderConfig, False),
        "SingleWeightConfig": (SingleWeightConfig, False),
        "Type": (str, True),
    }


class ContinuousDeploymentPolicyConfig(AWSProperty):
    """
    `ContinuousDeploymentPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
        "SingleHeaderPolicyConfig": (SingleHeaderPolicyConfig, False),
        "SingleWeightPolicyConfig": (SingleWeightPolicyConfig, False),
        "StagingDistributionDnsNames": ([str], True),
        "TrafficConfig": (TrafficConfig, False),
        "Type": (str, False),
    }


class ContinuousDeploymentPolicy(AWSObject):
    """
    `ContinuousDeploymentPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-continuousdeploymentpolicy.html>`__
    """

    resource_type = "AWS::CloudFront::ContinuousDeploymentPolicy"

    props: PropsDictType = {
        "ContinuousDeploymentPolicyConfig": (ContinuousDeploymentPolicyConfig, True),
    }


class Cookies(AWSProperty):
    """
    `Cookies <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html>`__
    """

    props: PropsDictType = {
        "Forward": (cloudfront_forward_type, True),
        "WhitelistedNames": ([str], False),
    }


class ForwardedValues(AWSProperty):
    """
    `ForwardedValues <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html>`__
    """

    props: PropsDictType = {
        "Cookies": (Cookies, False),
        "Headers": ([str], False),
        "QueryString": (boolean, True),
        "QueryStringCacheKeys": ([str], False),
    }


class FunctionAssociation(AWSProperty):
    """
    `FunctionAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html>`__
    """

    props: PropsDictType = {
        "EventType": (str, False),
        "FunctionARN": (str, False),
    }


class LambdaFunctionAssociation(AWSProperty):
    """
    `LambdaFunctionAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html>`__
    """

    props: PropsDictType = {
        "EventType": (cloudfront_event_type, False),
        "IncludeBody": (boolean, False),
        "LambdaFunctionARN": (str, False),
    }


class CacheBehavior(AWSProperty):
    """
    `CacheBehavior <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html>`__
    """

    props: PropsDictType = {
        "AllowedMethods": ([str], False),
        "CachePolicyId": (str, False),
        "CachedMethods": ([str], False),
        "Compress": (boolean, False),
        "DefaultTTL": (double, False),
        "FieldLevelEncryptionId": (str, False),
        "ForwardedValues": (ForwardedValues, False),
        "FunctionAssociations": ([FunctionAssociation], False),
        "LambdaFunctionAssociations": ([LambdaFunctionAssociation], False),
        "MaxTTL": (double, False),
        "MinTTL": (double, False),
        "OriginRequestPolicyId": (str, False),
        "PathPattern": (str, True),
        "RealtimeLogConfigArn": (str, False),
        "ResponseHeadersPolicyId": (str, False),
        "SmoothStreaming": (boolean, False),
        "TargetOriginId": (str, True),
        "TrustedKeyGroups": ([str], False),
        "TrustedSigners": ([str], False),
        "ViewerProtocolPolicy": (cloudfront_viewer_protocol_policy, True),
    }


class CustomErrorResponse(AWSProperty):
    """
    `CustomErrorResponse <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html>`__
    """

    props: PropsDictType = {
        "ErrorCachingMinTTL": (double, False),
        "ErrorCode": (integer, True),
        "ResponseCode": (integer, False),
        "ResponsePagePath": (str, False),
    }


class DefaultCacheBehavior(AWSProperty):
    """
    `DefaultCacheBehavior <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html>`__
    """

    props: PropsDictType = {
        "AllowedMethods": ([str], False),
        "CachePolicyId": (str, False),
        "CachedMethods": ([str], False),
        "Compress": (boolean, False),
        "DefaultTTL": (double, False),
        "FieldLevelEncryptionId": (str, False),
        "ForwardedValues": (ForwardedValues, False),
        "FunctionAssociations": ([FunctionAssociation], False),
        "LambdaFunctionAssociations": ([LambdaFunctionAssociation], False),
        "MaxTTL": (double, False),
        "MinTTL": (double, False),
        "OriginRequestPolicyId": (str, False),
        "RealtimeLogConfigArn": (str, False),
        "ResponseHeadersPolicyId": (str, False),
        "SmoothStreaming": (boolean, False),
        "TargetOriginId": (str, True),
        "TrustedKeyGroups": ([str], False),
        "TrustedSigners": ([str], False),
        "ViewerProtocolPolicy": (cloudfront_viewer_protocol_policy, True),
    }


class LegacyCustomOrigin(AWSProperty):
    """
    `LegacyCustomOrigin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html>`__
    """

    props: PropsDictType = {
        "DNSName": (str, True),
        "HTTPPort": (integer, False),
        "HTTPSPort": (integer, False),
        "OriginProtocolPolicy": (str, True),
        "OriginSSLProtocols": ([str], True),
    }


class LegacyS3Origin(AWSProperty):
    """
    `LegacyS3Origin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html>`__
    """

    props: PropsDictType = {
        "DNSName": (str, True),
        "OriginAccessIdentity": (str, False),
    }


class Logging(AWSProperty):
    """
    `Logging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "IncludeCookies": (boolean, False),
        "Prefix": (str, False),
    }


class CustomOriginConfig(AWSProperty):
    """
    `CustomOriginConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html>`__
    """

    props: PropsDictType = {
        "HTTPPort": (validate_network_port, False),
        "HTTPSPort": (validate_network_port, False),
        "OriginKeepaliveTimeout": (integer, False),
        "OriginProtocolPolicy": (str, True),
        "OriginReadTimeout": (integer, False),
        "OriginSSLProtocols": ([str], False),
    }


class OriginCustomHeader(AWSProperty):
    """
    `OriginCustomHeader <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html>`__
    """

    props: PropsDictType = {
        "HeaderName": (str, True),
        "HeaderValue": (str, True),
    }


class OriginShield(AWSProperty):
    """
    `OriginShield <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "OriginShieldRegion": (str, False),
    }


class S3OriginConfig(AWSProperty):
    """
    `S3OriginConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html>`__
    """

    props: PropsDictType = {
        "OriginAccessIdentity": (str, False),
    }


class Origin(AWSProperty):
    """
    `Origin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html>`__
    """

    props: PropsDictType = {
        "ConnectionAttempts": (integer, False),
        "ConnectionTimeout": (integer, False),
        "CustomOriginConfig": (CustomOriginConfig, False),
        "DomainName": (str, True),
        "Id": (str, True),
        "OriginAccessControlId": (str, False),
        "OriginCustomHeaders": ([OriginCustomHeader], False),
        "OriginPath": (str, False),
        "OriginShield": (OriginShield, False),
        "S3OriginConfig": (S3OriginConfig, False),
    }


class StatusCodes(AWSProperty):
    """
    `StatusCodes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html>`__
    """

    props: PropsDictType = {
        "Items": ([integer], True),
        "Quantity": (integer, True),
    }


class OriginGroupFailoverCriteria(AWSProperty):
    """
    `OriginGroupFailoverCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html>`__
    """

    props: PropsDictType = {
        "StatusCodes": (StatusCodes, True),
    }


class OriginGroupMember(AWSProperty):
    """
    `OriginGroupMember <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html>`__
    """

    props: PropsDictType = {
        "OriginId": (str, True),
    }


class OriginGroupMembers(AWSProperty):
    """
    `OriginGroupMembers <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html>`__
    """

    props: PropsDictType = {
        "Items": ([OriginGroupMember], True),
        "Quantity": (integer, True),
    }


class OriginGroup(AWSProperty):
    """
    `OriginGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html>`__
    """

    props: PropsDictType = {
        "FailoverCriteria": (OriginGroupFailoverCriteria, True),
        "Id": (str, True),
        "Members": (OriginGroupMembers, True),
    }


class OriginGroups(AWSProperty):
    """
    `OriginGroups <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html>`__
    """

    props: PropsDictType = {
        "Items": ([OriginGroup], False),
        "Quantity": (integer, True),
    }


class GeoRestriction(AWSProperty):
    """
    `GeoRestriction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html>`__
    """

    props: PropsDictType = {
        "Locations": ([str], False),
        "RestrictionType": (cloudfront_restriction_type, True),
    }


class Restrictions(AWSProperty):
    """
    `Restrictions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html>`__
    """

    props: PropsDictType = {
        "GeoRestriction": (GeoRestriction, True),
    }


class ViewerCertificate(AWSProperty):
    """
    `ViewerCertificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html>`__
    """

    props: PropsDictType = {
        "AcmCertificateArn": (str, False),
        "CloudFrontDefaultCertificate": (boolean, False),
        "IamCertificateId": (str, False),
        "MinimumProtocolVersion": (str, False),
        "SslSupportMethod": (str, False),
    }


class DistributionConfig(AWSProperty):
    """
    `DistributionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html>`__
    """

    props: PropsDictType = {
        "Aliases": ([str], False),
        "CNAMEs": ([str], False),
        "CacheBehaviors": ([CacheBehavior], False),
        "Comment": (str, False),
        "ContinuousDeploymentPolicyId": (str, False),
        "CustomErrorResponses": ([CustomErrorResponse], False),
        "CustomOrigin": (LegacyCustomOrigin, False),
        "DefaultCacheBehavior": (DefaultCacheBehavior, True),
        "DefaultRootObject": (str, False),
        "Enabled": (boolean, True),
        "HttpVersion": (str, False),
        "IPV6Enabled": (boolean, False),
        "Logging": (Logging, False),
        "OriginGroups": (OriginGroups, False),
        "Origins": ([Origin], False),
        "PriceClass": (priceclass_type, False),
        "Restrictions": (Restrictions, False),
        "S3Origin": (LegacyS3Origin, False),
        "Staging": (boolean, False),
        "ViewerCertificate": (ViewerCertificate, False),
        "WebACLId": (str, False),
    }


class Distribution(AWSObject):
    """
    `Distribution <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html>`__
    """

    resource_type = "AWS::CloudFront::Distribution"

    props: PropsDictType = {
        "DistributionConfig": (DistributionConfig, True),
        "Tags": (validate_tags_or_list, False),
    }


class KeyValueStoreAssociation(AWSProperty):
    """
    `KeyValueStoreAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-keyvaluestoreassociation.html>`__
    """

    props: PropsDictType = {
        "KeyValueStoreARN": (str, True),
    }


class FunctionConfig(AWSProperty):
    """
    `FunctionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html>`__
    """

    props: PropsDictType = {
        "Comment": (str, True),
        "KeyValueStoreAssociations": ([KeyValueStoreAssociation], False),
        "Runtime": (str, True),
    }


class FunctionMetadata(AWSProperty):
    """
    `FunctionMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionmetadata.html>`__
    """

    props: PropsDictType = {
        "FunctionARN": (str, False),
    }


class Function(AWSObject):
    """
    `Function <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html>`__
    """

    resource_type = "AWS::CloudFront::Function"

    props: PropsDictType = {
        "AutoPublish": (boolean, False),
        "FunctionCode": (str, True),
        "FunctionConfig": (FunctionConfig, True),
        "FunctionMetadata": (FunctionMetadata, False),
        "Name": (str, True),
    }


class KeyGroupConfig(AWSProperty):
    """
    `KeyGroupConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html>`__
    """

    props: PropsDictType = {
        "Comment": (str, False),
        "Items": ([str], True),
        "Name": (str, True),
    }


class KeyGroup(AWSObject):
    """
    `KeyGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html>`__
    """

    resource_type = "AWS::CloudFront::KeyGroup"

    props: PropsDictType = {
        "KeyGroupConfig": (KeyGroupConfig, True),
    }


class ImportSource(AWSProperty):
    """
    `ImportSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keyvaluestore-importsource.html>`__
    """

    props: PropsDictType = {
        "SourceArn": (str, True),
        "SourceType": (str, True),
    }


class KeyValueStore(AWSObject):
    """
    `KeyValueStore <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keyvaluestore.html>`__
    """

    resource_type = "AWS::CloudFront::KeyValueStore"

    props: PropsDictType = {
        "Comment": (str, False),
        "ImportSource": (ImportSource, False),
        "Name": (str, True),
    }


class RealtimeMetricsSubscriptionConfig(AWSProperty):
    """
    `RealtimeMetricsSubscriptionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig.html>`__
    """

    props: PropsDictType = {
        "RealtimeMetricsSubscriptionStatus": (str, True),
    }


class MonitoringSubscriptionProperty(AWSProperty):
    """
    `MonitoringSubscriptionProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-monitoringsubscription-monitoringsubscription.html>`__
    """

    props: PropsDictType = {
        "RealtimeMetricsSubscriptionConfig": (RealtimeMetricsSubscriptionConfig, False),
    }


class MonitoringSubscription(AWSObject):
    """
    `MonitoringSubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-monitoringsubscription.html>`__
    """

    resource_type = "AWS::CloudFront::MonitoringSubscription"

    props: PropsDictType = {
        "DistributionId": (str, True),
        "MonitoringSubscription": (MonitoringSubscriptionProperty, True),
    }


class OriginAccessControlConfig(AWSProperty):
    """
    `OriginAccessControlConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originaccesscontrol-originaccesscontrolconfig.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "OriginAccessControlOriginType": (str, True),
        "SigningBehavior": (str, True),
        "SigningProtocol": (str, True),
    }


class OriginAccessControl(AWSObject):
    """
    `OriginAccessControl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.html>`__
    """

    resource_type = "AWS::CloudFront::OriginAccessControl"

    props: PropsDictType = {
        "OriginAccessControlConfig": (OriginAccessControlConfig, True),
    }


class OriginRequestCookiesConfig(AWSProperty):
    """
    `OriginRequestCookiesConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html>`__
    """

    props: PropsDictType = {
        "CookieBehavior": (cloudfront_origin_request_cookie_behavior, True),
        "Cookies": ([str], False),
    }


class OriginRequestHeadersConfig(AWSProperty):
    """
    `OriginRequestHeadersConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html>`__
    """

    props: PropsDictType = {
        "HeaderBehavior": (cloudfront_origin_request_header_behavior, True),
        "Headers": ([str], False),
    }


class OriginRequestQueryStringsConfig(AWSProperty):
    """
    `OriginRequestQueryStringsConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html>`__
    """

    props: PropsDictType = {
        "QueryStringBehavior": (cloudfront_origin_request_query_string_behavior, True),
        "QueryStrings": ([str], False),
    }


class OriginRequestPolicyConfig(AWSProperty):
    """
    `OriginRequestPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html>`__
    """

    props: PropsDictType = {
        "Comment": (str, False),
        "CookiesConfig": (OriginRequestCookiesConfig, True),
        "HeadersConfig": (OriginRequestHeadersConfig, True),
        "Name": (str, True),
        "QueryStringsConfig": (OriginRequestQueryStringsConfig, True),
    }


class OriginRequestPolicy(AWSObject):
    """
    `OriginRequestPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html>`__
    """

    resource_type = "AWS::CloudFront::OriginRequestPolicy"

    props: PropsDictType = {
        "OriginRequestPolicyConfig": (OriginRequestPolicyConfig, True),
    }


class PublicKeyConfig(AWSProperty):
    """
    `PublicKeyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html>`__
    """

    props: PropsDictType = {
        "CallerReference": (str, True),
        "Comment": (str, False),
        "EncodedKey": (str, True),
        "Name": (str, True),
    }


class PublicKey(AWSObject):
    """
    `PublicKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html>`__
    """

    resource_type = "AWS::CloudFront::PublicKey"

    props: PropsDictType = {
        "PublicKeyConfig": (PublicKeyConfig, True),
    }


class KinesisStreamConfig(AWSProperty):
    """
    `KinesisStreamConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, True),
        "StreamArn": (str, True),
    }


class EndPoint(AWSProperty):
    """
    `EndPoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html>`__
    """

    props: PropsDictType = {
        "KinesisStreamConfig": (KinesisStreamConfig, True),
        "StreamType": (str, True),
    }


class RealtimeLogConfig(AWSObject):
    """
    `RealtimeLogConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html>`__
    """

    resource_type = "AWS::CloudFront::RealtimeLogConfig"

    props: PropsDictType = {
        "EndPoints": ([EndPoint], True),
        "Fields": ([str], True),
        "Name": (str, True),
        "SamplingRate": (double, True),
    }


class AccessControlAllowHeaders(AWSProperty):
    """
    `AccessControlAllowHeaders <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowheaders.html>`__
    """

    props: PropsDictType = {
        "Items": ([str], True),
    }


class AccessControlAllowMethods(AWSProperty):
    """
    `AccessControlAllowMethods <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods.html>`__
    """

    props: PropsDictType = {
        "Items": (cloudfront_access_control_allow_methods, True),
    }


class AccessControlAllowOrigins(AWSProperty):
    """
    `AccessControlAllowOrigins <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins.html>`__
    """

    props: PropsDictType = {
        "Items": ([str], True),
    }


class AccessControlExposeHeaders(AWSProperty):
    """
    `AccessControlExposeHeaders <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolexposeheaders.html>`__
    """

    props: PropsDictType = {
        "Items": ([str], True),
    }


class CorsConfig(AWSProperty):
    """
    `CorsConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html>`__
    """

    props: PropsDictType = {
        "AccessControlAllowCredentials": (boolean, True),
        "AccessControlAllowHeaders": (AccessControlAllowHeaders, True),
        "AccessControlAllowMethods": (AccessControlAllowMethods, True),
        "AccessControlAllowOrigins": (AccessControlAllowOrigins, True),
        "AccessControlExposeHeaders": (AccessControlExposeHeaders, False),
        "AccessControlMaxAgeSec": (integer, False),
        "OriginOverride": (boolean, True),
    }


class CustomHeader(AWSProperty):
    """
    `CustomHeader <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html>`__
    """

    props: PropsDictType = {
        "Header": (str, True),
        "Override": (boolean, True),
        "Value": (str, True),
    }


class CustomHeadersConfig(AWSProperty):
    """
    `CustomHeadersConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheadersconfig.html>`__
    """

    props: PropsDictType = {
        "Items": ([CustomHeader], True),
    }


class RemoveHeader(AWSProperty):
    """
    `RemoveHeader <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-removeheader.html>`__
    """

    props: PropsDictType = {
        "Header": (str, True),
    }


class RemoveHeadersConfig(AWSProperty):
    """
    `RemoveHeadersConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-removeheadersconfig.html>`__
    """

    props: PropsDictType = {
        "Items": ([RemoveHeader], True),
    }


class ContentSecurityPolicy(AWSProperty):
    """
    `ContentSecurityPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html>`__
    """

    props: PropsDictType = {
        "ContentSecurityPolicy": (str, True),
        "Override": (boolean, True),
    }


class ContentTypeOptions(AWSProperty):
    """
    `ContentTypeOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions.html>`__
    """

    props: PropsDictType = {
        "Override": (boolean, True),
    }


class FrameOptions(AWSProperty):
    """
    `FrameOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html>`__
    """

    props: PropsDictType = {
        "FrameOption": (cloudfront_frame_option, True),
        "Override": (boolean, True),
    }


class ReferrerPolicy(AWSProperty):
    """
    `ReferrerPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html>`__
    """

    props: PropsDictType = {
        "Override": (boolean, True),
        "ReferrerPolicy": (cloudfront_referrer_policy, True),
    }


class StrictTransportSecurity(AWSProperty):
    """
    `StrictTransportSecurity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html>`__
    """

    props: PropsDictType = {
        "AccessControlMaxAgeSec": (integer, True),
        "IncludeSubdomains": (boolean, False),
        "Override": (boolean, True),
        "Preload": (boolean, False),
    }


class XSSProtection(AWSProperty):
    """
    `XSSProtection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html>`__
    """

    props: PropsDictType = {
        "ModeBlock": (boolean, False),
        "Override": (boolean, True),
        "Protection": (boolean, True),
        "ReportUri": (str, False),
    }


class SecurityHeadersConfig(AWSProperty):
    """
    `SecurityHeadersConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html>`__
    """

    props: PropsDictType = {
        "ContentSecurityPolicy": (ContentSecurityPolicy, False),
        "ContentTypeOptions": (ContentTypeOptions, False),
        "FrameOptions": (FrameOptions, False),
        "ReferrerPolicy": (ReferrerPolicy, False),
        "StrictTransportSecurity": (StrictTransportSecurity, False),
        "XSSProtection": (XSSProtection, False),
    }


class ServerTimingHeadersConfig(AWSProperty):
    """
    `ServerTimingHeadersConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-servertimingheadersconfig.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
        "SamplingRate": (double, False),
    }


class ResponseHeadersPolicyConfig(AWSProperty):
    """
    `ResponseHeadersPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html>`__
    """

    props: PropsDictType = {
        "Comment": (str, False),
        "CorsConfig": (CorsConfig, False),
        "CustomHeadersConfig": (CustomHeadersConfig, False),
        "Name": (str, True),
        "RemoveHeadersConfig": (RemoveHeadersConfig, False),
        "SecurityHeadersConfig": (SecurityHeadersConfig, False),
        "ServerTimingHeadersConfig": (ServerTimingHeadersConfig, False),
    }


class ResponseHeadersPolicy(AWSObject):
    """
    `ResponseHeadersPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html>`__
    """

    resource_type = "AWS::CloudFront::ResponseHeadersPolicy"

    props: PropsDictType = {
        "ResponseHeadersPolicyConfig": (ResponseHeadersPolicyConfig, True),
    }


class S3Origin(AWSProperty):
    """
    `S3Origin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html>`__
    """

    props: PropsDictType = {
        "DomainName": (str, True),
        "OriginAccessIdentity": (str, False),
    }


class StreamingDistributioniLogging(AWSProperty):
    """
    `StreamingDistributioniLogging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "Enabled": (boolean, True),
        "Prefix": (str, True),
    }


class TrustedSigners(AWSProperty):
    """
    `TrustedSigners <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html>`__
    """

    props: PropsDictType = {
        "AwsAccountNumbers": ([str], False),
        "Enabled": (boolean, True),
    }


class StreamingDistributionConfig(AWSProperty):
    """
    `StreamingDistributionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html>`__
    """

    props: PropsDictType = {
        "Aliases": ([str], False),
        "Comment": (str, True),
        "Enabled": (boolean, True),
        "Logging": (StreamingDistributioniLogging, False),
        "PriceClass": (priceclass_type, False),
        "S3Origin": (S3Origin, True),
        "TrustedSigners": (TrustedSigners, True),
    }


class StreamingDistribution(AWSObject):
    """
    `StreamingDistribution <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html>`__
    """

    resource_type = "AWS::CloudFront::StreamingDistribution"

    props: PropsDictType = {
        "StreamingDistributionConfig": (StreamingDistributionConfig, True),
        "Tags": (validate_tags_or_list, False),
    }