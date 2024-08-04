# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double, integer


class ADMChannel(AWSObject):
    """
    `ADMChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html>`__
    """

    resource_type = "AWS::Pinpoint::ADMChannel"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "ClientId": (str, True),
        "ClientSecret": (str, True),
        "Enabled": (boolean, False),
    }


class APNSChannel(AWSObject):
    """
    `APNSChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html>`__
    """

    resource_type = "AWS::Pinpoint::APNSChannel"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "BundleId": (str, False),
        "Certificate": (str, False),
        "DefaultAuthenticationMethod": (str, False),
        "Enabled": (boolean, False),
        "PrivateKey": (str, False),
        "TeamId": (str, False),
        "TokenKey": (str, False),
        "TokenKeyId": (str, False),
    }


class APNSSandboxChannel(AWSObject):
    """
    `APNSSandboxChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html>`__
    """

    resource_type = "AWS::Pinpoint::APNSSandboxChannel"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "BundleId": (str, False),
        "Certificate": (str, False),
        "DefaultAuthenticationMethod": (str, False),
        "Enabled": (boolean, False),
        "PrivateKey": (str, False),
        "TeamId": (str, False),
        "TokenKey": (str, False),
        "TokenKeyId": (str, False),
    }


class APNSVoipChannel(AWSObject):
    """
    `APNSVoipChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html>`__
    """

    resource_type = "AWS::Pinpoint::APNSVoipChannel"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "BundleId": (str, False),
        "Certificate": (str, False),
        "DefaultAuthenticationMethod": (str, False),
        "Enabled": (boolean, False),
        "PrivateKey": (str, False),
        "TeamId": (str, False),
        "TokenKey": (str, False),
        "TokenKeyId": (str, False),
    }


class APNSVoipSandboxChannel(AWSObject):
    """
    `APNSVoipSandboxChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html>`__
    """

    resource_type = "AWS::Pinpoint::APNSVoipSandboxChannel"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "BundleId": (str, False),
        "Certificate": (str, False),
        "DefaultAuthenticationMethod": (str, False),
        "Enabled": (boolean, False),
        "PrivateKey": (str, False),
        "TeamId": (str, False),
        "TokenKey": (str, False),
        "TokenKeyId": (str, False),
    }


class App(AWSObject):
    """
    `App <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html>`__
    """

    resource_type = "AWS::Pinpoint::App"

    props: PropsDictType = {
        "Name": (str, True),
        "Tags": (dict, False),
    }


class CampaignHook(AWSProperty):
    """
    `CampaignHook <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html>`__
    """

    props: PropsDictType = {
        "LambdaFunctionName": (str, False),
        "Mode": (str, False),
        "WebUrl": (str, False),
    }


class Limits(AWSProperty):
    """
    `Limits <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html>`__
    """

    props: PropsDictType = {
        "Daily": (integer, False),
        "MaximumDuration": (integer, False),
        "MessagesPerSecond": (integer, False),
        "Session": (integer, False),
        "Total": (integer, False),
    }


class QuietTime(AWSProperty):
    """
    `QuietTime <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html>`__
    """

    props: PropsDictType = {
        "End": (str, True),
        "Start": (str, True),
    }


class ApplicationSettings(AWSObject):
    """
    `ApplicationSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html>`__
    """

    resource_type = "AWS::Pinpoint::ApplicationSettings"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "CampaignHook": (CampaignHook, False),
        "CloudWatchMetricsEnabled": (boolean, False),
        "Limits": (Limits, False),
        "QuietTime": (QuietTime, False),
    }


class BaiduChannel(AWSObject):
    """
    `BaiduChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html>`__
    """

    resource_type = "AWS::Pinpoint::BaiduChannel"

    props: PropsDictType = {
        "ApiKey": (str, True),
        "ApplicationId": (str, True),
        "Enabled": (boolean, False),
        "SecretKey": (str, True),
    }


class CustomDeliveryConfiguration(AWSProperty):
    """
    `CustomDeliveryConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-customdeliveryconfiguration.html>`__
    """

    props: PropsDictType = {
        "DeliveryUri": (str, False),
        "EndpointTypes": ([str], False),
    }


class CampaignCustomMessage(AWSProperty):
    """
    `CampaignCustomMessage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigncustommessage.html>`__
    """

    props: PropsDictType = {
        "Data": (str, False),
    }


class CampaignEmailMessage(AWSProperty):
    """
    `CampaignEmailMessage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html>`__
    """

    props: PropsDictType = {
        "Body": (str, False),
        "FromAddress": (str, False),
        "HtmlBody": (str, False),
        "Title": (str, False),
    }


class BodyConfig(AWSProperty):
    """
    `BodyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html>`__
    """

    props: PropsDictType = {
        "Alignment": (str, False),
        "Body": (str, False),
        "TextColor": (str, False),
    }


class DefaultButtonConfiguration(AWSProperty):
    """
    `DefaultButtonConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html>`__
    """

    props: PropsDictType = {
        "BackgroundColor": (str, False),
        "BorderRadius": (integer, False),
        "ButtonAction": (str, False),
        "Link": (str, False),
        "Text": (str, False),
        "TextColor": (str, False),
    }


class OverrideButtonConfiguration(AWSProperty):
    """
    `OverrideButtonConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html>`__
    """

    props: PropsDictType = {
        "ButtonAction": (str, False),
        "Link": (str, False),
    }


class ButtonConfig(AWSProperty):
    """
    `ButtonConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html>`__
    """

    props: PropsDictType = {
        "Android": (OverrideButtonConfiguration, False),
        "DefaultConfig": (DefaultButtonConfiguration, False),
        "IOS": (OverrideButtonConfiguration, False),
        "Web": (OverrideButtonConfiguration, False),
    }


class HeaderConfig(AWSProperty):
    """
    `HeaderConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html>`__
    """

    props: PropsDictType = {
        "Alignment": (str, False),
        "Header": (str, False),
        "TextColor": (str, False),
    }


class InAppMessageContent(AWSProperty):
    """
    `InAppMessageContent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html>`__
    """

    props: PropsDictType = {
        "BackgroundColor": (str, False),
        "BodyConfig": (BodyConfig, False),
        "HeaderConfig": (HeaderConfig, False),
        "ImageUrl": (str, False),
        "PrimaryBtn": (ButtonConfig, False),
        "SecondaryBtn": (ButtonConfig, False),
    }


class CampaignInAppMessage(AWSProperty):
    """
    `CampaignInAppMessage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html>`__
    """

    props: PropsDictType = {
        "Content": ([InAppMessageContent], False),
        "CustomConfig": (dict, False),
        "Layout": (str, False),
    }


class CampaignSmsMessage(AWSProperty):
    """
    `CampaignSmsMessage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html>`__
    """

    props: PropsDictType = {
        "Body": (str, False),
        "EntityId": (str, False),
        "MessageType": (str, False),
        "OriginationNumber": (str, False),
        "SenderId": (str, False),
        "TemplateId": (str, False),
    }


class Message(AWSProperty):
    """
    `Message <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html>`__
    """

    props: PropsDictType = {
        "Action": (str, False),
        "Body": (str, False),
        "ImageIconUrl": (str, False),
        "ImageSmallIconUrl": (str, False),
        "ImageUrl": (str, False),
        "JsonBody": (str, False),
        "MediaUrl": (str, False),
        "RawContent": (str, False),
        "SilentPush": (boolean, False),
        "TimeToLive": (integer, False),
        "Title": (str, False),
        "Url": (str, False),
    }


class MessageConfiguration(AWSProperty):
    """
    `MessageConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html>`__
    """

    props: PropsDictType = {
        "ADMMessage": (Message, False),
        "APNSMessage": (Message, False),
        "BaiduMessage": (Message, False),
        "CustomMessage": (CampaignCustomMessage, False),
        "DefaultMessage": (Message, False),
        "EmailMessage": (CampaignEmailMessage, False),
        "GCMMessage": (Message, False),
        "InAppMessage": (CampaignInAppMessage, False),
        "SMSMessage": (CampaignSmsMessage, False),
    }


class SetDimension(AWSProperty):
    """
    `SetDimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html>`__
    """

    props: PropsDictType = {
        "DimensionType": (str, False),
        "Values": ([str], False),
    }


class EventDimensions(AWSProperty):
    """
    `EventDimensions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html>`__
    """

    props: PropsDictType = {
        "Attributes": (dict, False),
        "EventType": (SetDimension, False),
        "Metrics": (dict, False),
    }


class CampaignEventFilter(AWSProperty):
    """
    `CampaignEventFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html>`__
    """

    props: PropsDictType = {
        "Dimensions": (EventDimensions, False),
        "FilterType": (str, False),
    }


class Schedule(AWSProperty):
    """
    `Schedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html>`__
    """

    props: PropsDictType = {
        "EndTime": (str, False),
        "EventFilter": (CampaignEventFilter, False),
        "Frequency": (str, False),
        "IsLocalTime": (boolean, False),
        "QuietTime": (QuietTime, False),
        "StartTime": (str, False),
        "TimeZone": (str, False),
    }


class Template(AWSProperty):
    """
    `Template <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-template.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Version": (str, False),
    }


class TemplateConfiguration(AWSProperty):
    """
    `TemplateConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html>`__
    """

    props: PropsDictType = {
        "EmailTemplate": (Template, False),
        "PushTemplate": (Template, False),
        "SMSTemplate": (Template, False),
        "VoiceTemplate": (Template, False),
    }


class WriteTreatmentResource(AWSProperty):
    """
    `WriteTreatmentResource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html>`__
    """

    props: PropsDictType = {
        "CustomDeliveryConfiguration": (CustomDeliveryConfiguration, False),
        "MessageConfiguration": (MessageConfiguration, False),
        "Schedule": (Schedule, False),
        "SizePercent": (integer, False),
        "TemplateConfiguration": (TemplateConfiguration, False),
        "TreatmentDescription": (str, False),
        "TreatmentName": (str, False),
    }


class Campaign(AWSObject):
    """
    `Campaign <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html>`__
    """

    resource_type = "AWS::Pinpoint::Campaign"

    props: PropsDictType = {
        "AdditionalTreatments": ([WriteTreatmentResource], False),
        "ApplicationId": (str, True),
        "CampaignHook": (CampaignHook, False),
        "CustomDeliveryConfiguration": (CustomDeliveryConfiguration, False),
        "Description": (str, False),
        "HoldoutPercent": (integer, False),
        "IsPaused": (boolean, False),
        "Limits": (Limits, False),
        "MessageConfiguration": (MessageConfiguration, False),
        "Name": (str, True),
        "Priority": (integer, False),
        "Schedule": (Schedule, True),
        "SegmentId": (str, True),
        "SegmentVersion": (integer, False),
        "Tags": (dict, False),
        "TemplateConfiguration": (TemplateConfiguration, False),
        "TreatmentDescription": (str, False),
        "TreatmentName": (str, False),
    }


class EmailChannel(AWSObject):
    """
    `EmailChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html>`__
    """

    resource_type = "AWS::Pinpoint::EmailChannel"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "ConfigurationSet": (str, False),
        "Enabled": (boolean, False),
        "FromAddress": (str, True),
        "Identity": (str, True),
        "OrchestrationSendingRoleArn": (str, False),
        "RoleArn": (str, False),
    }


class EmailTemplate(AWSObject):
    """
    `EmailTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html>`__
    """

    resource_type = "AWS::Pinpoint::EmailTemplate"

    props: PropsDictType = {
        "DefaultSubstitutions": (str, False),
        "HtmlPart": (str, False),
        "Subject": (str, True),
        "Tags": (dict, False),
        "TemplateDescription": (str, False),
        "TemplateName": (str, True),
        "TextPart": (str, False),
    }


class EventStream(AWSObject):
    """
    `EventStream <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html>`__
    """

    resource_type = "AWS::Pinpoint::EventStream"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "DestinationStreamArn": (str, True),
        "RoleArn": (str, True),
    }


class GCMChannel(AWSObject):
    """
    `GCMChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html>`__
    """

    resource_type = "AWS::Pinpoint::GCMChannel"

    props: PropsDictType = {
        "ApiKey": (str, False),
        "ApplicationId": (str, True),
        "DefaultAuthenticationMethod": (str, False),
        "Enabled": (boolean, False),
        "ServiceJson": (str, False),
    }


class InAppTemplate(AWSObject):
    """
    `InAppTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html>`__
    """

    resource_type = "AWS::Pinpoint::InAppTemplate"

    props: PropsDictType = {
        "Content": ([InAppMessageContent], False),
        "CustomConfig": (dict, False),
        "Layout": (str, False),
        "Tags": (dict, False),
        "TemplateDescription": (str, False),
        "TemplateName": (str, True),
    }


class APNSPushNotificationTemplate(AWSProperty):
    """
    `APNSPushNotificationTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html>`__
    """

    props: PropsDictType = {
        "Action": (str, False),
        "Body": (str, False),
        "MediaUrl": (str, False),
        "Sound": (str, False),
        "Title": (str, False),
        "Url": (str, False),
    }


class AndroidPushNotificationTemplate(AWSProperty):
    """
    `AndroidPushNotificationTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html>`__
    """

    props: PropsDictType = {
        "Action": (str, False),
        "Body": (str, False),
        "ImageIconUrl": (str, False),
        "ImageUrl": (str, False),
        "SmallImageIconUrl": (str, False),
        "Sound": (str, False),
        "Title": (str, False),
        "Url": (str, False),
    }


class DefaultPushNotificationTemplate(AWSProperty):
    """
    `DefaultPushNotificationTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html>`__
    """

    props: PropsDictType = {
        "Action": (str, False),
        "Body": (str, False),
        "Sound": (str, False),
        "Title": (str, False),
        "Url": (str, False),
    }


class PushTemplate(AWSObject):
    """
    `PushTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html>`__
    """

    resource_type = "AWS::Pinpoint::PushTemplate"

    props: PropsDictType = {
        "ADM": (AndroidPushNotificationTemplate, False),
        "APNS": (APNSPushNotificationTemplate, False),
        "Baidu": (AndroidPushNotificationTemplate, False),
        "Default": (DefaultPushNotificationTemplate, False),
        "DefaultSubstitutions": (str, False),
        "GCM": (AndroidPushNotificationTemplate, False),
        "Tags": (dict, False),
        "TemplateDescription": (str, False),
        "TemplateName": (str, True),
    }


class SMSChannel(AWSObject):
    """
    `SMSChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html>`__
    """

    resource_type = "AWS::Pinpoint::SMSChannel"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "Enabled": (boolean, False),
        "SenderId": (str, False),
        "ShortCode": (str, False),
    }


class Recency(AWSProperty):
    """
    `Recency <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html>`__
    """

    props: PropsDictType = {
        "Duration": (str, True),
        "RecencyType": (str, True),
    }


class Behavior(AWSProperty):
    """
    `Behavior <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html>`__
    """

    props: PropsDictType = {
        "Recency": (Recency, False),
    }


class Demographic(AWSProperty):
    """
    `Demographic <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html>`__
    """

    props: PropsDictType = {
        "AppVersion": (SetDimension, False),
        "Channel": (SetDimension, False),
        "DeviceType": (SetDimension, False),
        "Make": (SetDimension, False),
        "Model": (SetDimension, False),
        "Platform": (SetDimension, False),
    }


class Coordinates(AWSProperty):
    """
    `Coordinates <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html>`__
    """

    props: PropsDictType = {
        "Latitude": (double, True),
        "Longitude": (double, True),
    }


class GPSPoint(AWSProperty):
    """
    `GPSPoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html>`__
    """

    props: PropsDictType = {
        "Coordinates": (Coordinates, True),
        "RangeInKilometers": (double, True),
    }


class Location(AWSProperty):
    """
    `Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html>`__
    """

    props: PropsDictType = {
        "Country": (SetDimension, False),
        "GPSPoint": (GPSPoint, False),
    }


class SegmentDimensions(AWSProperty):
    """
    `SegmentDimensions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html>`__
    """

    props: PropsDictType = {
        "Attributes": (dict, False),
        "Behavior": (Behavior, False),
        "Demographic": (Demographic, False),
        "Location": (Location, False),
        "Metrics": (dict, False),
        "UserAttributes": (dict, False),
    }


class SourceSegments(AWSProperty):
    """
    `SourceSegments <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html>`__
    """

    props: PropsDictType = {
        "Id": (str, True),
        "Version": (integer, False),
    }


class Groups(AWSProperty):
    """
    `Groups <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html>`__
    """

    props: PropsDictType = {
        "Dimensions": ([SegmentDimensions], False),
        "SourceSegments": ([SourceSegments], False),
        "SourceType": (str, False),
        "Type": (str, False),
    }


class SegmentGroups(AWSProperty):
    """
    `SegmentGroups <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html>`__
    """

    props: PropsDictType = {
        "Groups": ([Groups], False),
        "Include": (str, False),
    }


class Segment(AWSObject):
    """
    `Segment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html>`__
    """

    resource_type = "AWS::Pinpoint::Segment"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "Dimensions": (SegmentDimensions, False),
        "Name": (str, True),
        "SegmentGroups": (SegmentGroups, False),
        "Tags": (dict, False),
    }


class SmsTemplate(AWSObject):
    """
    `SmsTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html>`__
    """

    resource_type = "AWS::Pinpoint::SmsTemplate"

    props: PropsDictType = {
        "Body": (str, True),
        "DefaultSubstitutions": (str, False),
        "Tags": (dict, False),
        "TemplateDescription": (str, False),
        "TemplateName": (str, True),
    }


class VoiceChannel(AWSObject):
    """
    `VoiceChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html>`__
    """

    resource_type = "AWS::Pinpoint::VoiceChannel"

    props: PropsDictType = {
        "ApplicationId": (str, True),
        "Enabled": (boolean, False),
    }


class AttributeDimension(AWSProperty):
    """
    `AttributeDimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html>`__
    """

    props: PropsDictType = {
        "AttributeType": (str, False),
        "Values": ([str], False),
    }


class InAppMessageBodyConfig(AWSProperty):
    """
    `InAppMessageBodyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html>`__
    """

    props: PropsDictType = {
        "Alignment": (str, False),
        "Body": (str, False),
        "TextColor": (str, False),
    }


class InAppMessageButton(AWSProperty):
    """
    `InAppMessageButton <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html>`__
    """

    props: PropsDictType = {
        "Android": (OverrideButtonConfiguration, False),
        "DefaultConfig": (DefaultButtonConfiguration, False),
        "IOS": (OverrideButtonConfiguration, False),
        "Web": (OverrideButtonConfiguration, False),
    }


class InAppMessageHeaderConfig(AWSProperty):
    """
    `InAppMessageHeaderConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html>`__
    """

    props: PropsDictType = {
        "Alignment": (str, False),
        "Header": (str, False),
        "TextColor": (str, False),
    }


class MetricDimension(AWSProperty):
    """
    `MetricDimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html>`__
    """

    props: PropsDictType = {
        "ComparisonOperator": (str, False),
        "Value": (double, False),
    }