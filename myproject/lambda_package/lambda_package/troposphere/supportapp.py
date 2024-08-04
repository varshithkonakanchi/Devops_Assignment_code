# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, PropsDictType
from .validators import boolean


class AccountAlias(AWSObject):
    """
    `AccountAlias <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-accountalias.html>`__
    """

    resource_type = "AWS::SupportApp::AccountAlias"

    props: PropsDictType = {
        "AccountAlias": (str, True),
    }


class SlackChannelConfiguration(AWSObject):
    """
    `SlackChannelConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html>`__
    """

    resource_type = "AWS::SupportApp::SlackChannelConfiguration"

    props: PropsDictType = {
        "ChannelId": (str, True),
        "ChannelName": (str, False),
        "ChannelRoleArn": (str, True),
        "NotifyOnAddCorrespondenceToCase": (boolean, False),
        "NotifyOnCaseSeverity": (str, True),
        "NotifyOnCreateOrReopenCase": (boolean, False),
        "NotifyOnResolveCase": (boolean, False),
        "TeamId": (str, True),
    }


class SlackWorkspaceConfiguration(AWSObject):
    """
    `SlackWorkspaceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.html>`__
    """

    resource_type = "AWS::SupportApp::SlackWorkspaceConfiguration"

    props: PropsDictType = {
        "TeamId": (str, True),
        "VersionId": (str, False),
    }
