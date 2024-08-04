# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class ConnectionAlias(AWSObject):
    """
    `ConnectionAlias <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html>`__
    """

    resource_type = "AWS::WorkSpaces::ConnectionAlias"

    props: PropsDictType = {
        "ConnectionString": (str, True),
        "Tags": (Tags, False),
    }


class WorkspaceProperties(AWSProperty):
    """
    `WorkspaceProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html>`__
    """

    props: PropsDictType = {
        "ComputeTypeName": (str, False),
        "RootVolumeSizeGib": (integer, False),
        "RunningMode": (str, False),
        "RunningModeAutoStopTimeoutInMinutes": (integer, False),
        "UserVolumeSizeGib": (integer, False),
    }


class Workspace(AWSObject):
    """
    `Workspace <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html>`__
    """

    resource_type = "AWS::WorkSpaces::Workspace"

    props: PropsDictType = {
        "BundleId": (str, True),
        "DirectoryId": (str, True),
        "RootVolumeEncryptionEnabled": (boolean, False),
        "Tags": (Tags, False),
        "UserName": (str, True),
        "UserVolumeEncryptionEnabled": (boolean, False),
        "VolumeEncryptionKey": (str, False),
        "WorkspaceProperties": (WorkspaceProperties, False),
    }


class ApplicationSettings(AWSProperty):
    """
    `ApplicationSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspacespool-applicationsettings.html>`__
    """

    props: PropsDictType = {
        "SettingsGroup": (str, False),
        "Status": (str, True),
    }


class Capacity(AWSProperty):
    """
    `Capacity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspacespool-capacity.html>`__
    """

    props: PropsDictType = {
        "DesiredUserSessions": (integer, True),
    }


class TimeoutSettings(AWSProperty):
    """
    `TimeoutSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspacespool-timeoutsettings.html>`__
    """

    props: PropsDictType = {
        "DisconnectTimeoutInSeconds": (integer, False),
        "IdleDisconnectTimeoutInSeconds": (integer, False),
        "MaxUserDurationInSeconds": (integer, False),
    }


class WorkspacesPool(AWSObject):
    """
    `WorkspacesPool <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspacespool.html>`__
    """

    resource_type = "AWS::WorkSpaces::WorkspacesPool"

    props: PropsDictType = {
        "ApplicationSettings": (ApplicationSettings, False),
        "BundleId": (str, True),
        "Capacity": (Capacity, True),
        "Description": (str, False),
        "DirectoryId": (str, True),
        "PoolName": (str, True),
        "Tags": (Tags, False),
        "TimeoutSettings": (TimeoutSettings, False),
    }