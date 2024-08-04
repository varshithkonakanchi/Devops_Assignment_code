# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class Endpoint(AWSProperty):
    """
    `Endpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html>`__
    """

    props: PropsDictType = {
        "Address": (str, False),
        "Port": (str, False),
    }


class LoggingProperties(AWSProperty):
    """
    `LoggingProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, False),
        "S3KeyPrefix": (str, False),
    }


class Cluster(AWSObject):
    """
    `Cluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html>`__
    """

    resource_type = "AWS::Redshift::Cluster"

    props: PropsDictType = {
        "AllowVersionUpgrade": (boolean, False),
        "AquaConfigurationStatus": (str, False),
        "AutomatedSnapshotRetentionPeriod": (integer, False),
        "AvailabilityZone": (str, False),
        "AvailabilityZoneRelocation": (boolean, False),
        "AvailabilityZoneRelocationStatus": (str, False),
        "Classic": (boolean, False),
        "ClusterIdentifier": (str, False),
        "ClusterParameterGroupName": (str, False),
        "ClusterSecurityGroups": ([str], False),
        "ClusterSubnetGroupName": (str, False),
        "ClusterType": (str, True),
        "ClusterVersion": (str, False),
        "DBName": (str, True),
        "DeferMaintenance": (boolean, False),
        "DeferMaintenanceDuration": (integer, False),
        "DeferMaintenanceEndTime": (str, False),
        "DeferMaintenanceStartTime": (str, False),
        "DestinationRegion": (str, False),
        "ElasticIp": (str, False),
        "Encrypted": (boolean, False),
        "Endpoint": (Endpoint, False),
        "EnhancedVpcRouting": (boolean, False),
        "HsmClientCertificateIdentifier": (str, False),
        "HsmConfigurationIdentifier": (str, False),
        "IamRoles": ([str], False),
        "KmsKeyId": (str, False),
        "LoggingProperties": (LoggingProperties, False),
        "MaintenanceTrackName": (str, False),
        "ManageMasterPassword": (boolean, False),
        "ManualSnapshotRetentionPeriod": (integer, False),
        "MasterPasswordSecretKmsKeyId": (str, False),
        "MasterUserPassword": (str, False),
        "MasterUsername": (str, True),
        "MultiAZ": (boolean, False),
        "NamespaceResourcePolicy": (dict, False),
        "NodeType": (str, True),
        "NumberOfNodes": (integer, False),
        "OwnerAccount": (str, False),
        "Port": (integer, False),
        "PreferredMaintenanceWindow": (str, False),
        "PubliclyAccessible": (boolean, False),
        "ResourceAction": (str, False),
        "RevisionTarget": (str, False),
        "RotateEncryptionKey": (boolean, False),
        "SnapshotClusterIdentifier": (str, False),
        "SnapshotCopyGrantName": (str, False),
        "SnapshotCopyManual": (boolean, False),
        "SnapshotCopyRetentionPeriod": (integer, False),
        "SnapshotIdentifier": (str, False),
        "Tags": (Tags, False),
        "VpcSecurityGroupIds": ([str], False),
    }


class AmazonRedshiftParameter(AWSProperty):
    """
    `AmazonRedshiftParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html>`__
    """

    props: PropsDictType = {
        "ParameterName": (str, True),
        "ParameterValue": (str, True),
    }


class ClusterParameterGroup(AWSObject):
    """
    `ClusterParameterGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html>`__
    """

    resource_type = "AWS::Redshift::ClusterParameterGroup"

    props: PropsDictType = {
        "Description": (str, True),
        "ParameterGroupFamily": (str, True),
        "ParameterGroupName": (str, False),
        "Parameters": ([AmazonRedshiftParameter], False),
        "Tags": (Tags, False),
    }


class ClusterSecurityGroup(AWSObject):
    """
    `ClusterSecurityGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html>`__
    """

    resource_type = "AWS::Redshift::ClusterSecurityGroup"

    props: PropsDictType = {
        "Description": (str, True),
        "Tags": (Tags, False),
    }


class ClusterSecurityGroupIngress(AWSObject):
    """
    `ClusterSecurityGroupIngress <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html>`__
    """

    resource_type = "AWS::Redshift::ClusterSecurityGroupIngress"

    props: PropsDictType = {
        "CIDRIP": (str, False),
        "ClusterSecurityGroupName": (str, True),
        "EC2SecurityGroupName": (str, False),
        "EC2SecurityGroupOwnerId": (str, False),
    }


class ClusterSubnetGroup(AWSObject):
    """
    `ClusterSubnetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html>`__
    """

    resource_type = "AWS::Redshift::ClusterSubnetGroup"

    props: PropsDictType = {
        "Description": (str, True),
        "SubnetIds": ([str], True),
        "Tags": (Tags, False),
    }


class EndpointAccess(AWSObject):
    """
    `EndpointAccess <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html>`__
    """

    resource_type = "AWS::Redshift::EndpointAccess"

    props: PropsDictType = {
        "ClusterIdentifier": (str, True),
        "EndpointName": (str, True),
        "ResourceOwner": (str, False),
        "SubnetGroupName": (str, True),
        "VpcSecurityGroupIds": ([str], True),
    }


class EndpointAuthorization(AWSObject):
    """
    `EndpointAuthorization <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html>`__
    """

    resource_type = "AWS::Redshift::EndpointAuthorization"

    props: PropsDictType = {
        "Account": (str, True),
        "ClusterIdentifier": (str, True),
        "Force": (boolean, False),
        "VpcIds": ([str], False),
    }


class EventSubscription(AWSObject):
    """
    `EventSubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html>`__
    """

    resource_type = "AWS::Redshift::EventSubscription"

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "EventCategories": ([str], False),
        "Severity": (str, False),
        "SnsTopicArn": (str, False),
        "SourceIds": ([str], False),
        "SourceType": (str, False),
        "SubscriptionName": (str, True),
        "Tags": (Tags, False),
    }


class PauseClusterMessage(AWSProperty):
    """
    `PauseClusterMessage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-pauseclustermessage.html>`__
    """

    props: PropsDictType = {
        "ClusterIdentifier": (str, True),
    }


class ResizeClusterMessage(AWSProperty):
    """
    `ResizeClusterMessage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html>`__
    """

    props: PropsDictType = {
        "Classic": (boolean, False),
        "ClusterIdentifier": (str, True),
        "ClusterType": (str, False),
        "NodeType": (str, False),
        "NumberOfNodes": (integer, False),
    }


class ResumeClusterMessage(AWSProperty):
    """
    `ResumeClusterMessage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resumeclustermessage.html>`__
    """

    props: PropsDictType = {
        "ClusterIdentifier": (str, True),
    }


class ScheduledActionType(AWSProperty):
    """
    `ScheduledActionType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-scheduledactiontype.html>`__
    """

    props: PropsDictType = {
        "PauseCluster": (PauseClusterMessage, False),
        "ResizeCluster": (ResizeClusterMessage, False),
        "ResumeCluster": (ResumeClusterMessage, False),
    }


class ScheduledAction(AWSObject):
    """
    `ScheduledAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html>`__
    """

    resource_type = "AWS::Redshift::ScheduledAction"

    props: PropsDictType = {
        "Enable": (boolean, False),
        "EndTime": (str, False),
        "IamRole": (str, False),
        "Schedule": (str, False),
        "ScheduledActionDescription": (str, False),
        "ScheduledActionName": (str, True),
        "StartTime": (str, False),
        "TargetAction": (ScheduledActionType, False),
    }


class NetworkInterface(AWSProperty):
    """
    `NetworkInterface <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html>`__
    """

    props: PropsDictType = {
        "AvailabilityZone": (str, False),
        "NetworkInterfaceId": (str, False),
        "PrivateIpAddress": (str, False),
        "SubnetId": (str, False),
    }


class VpcEndpoint(AWSProperty):
    """
    `VpcEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcendpoint.html>`__
    """

    props: PropsDictType = {
        "NetworkInterfaces": ([NetworkInterface], False),
        "VpcEndpointId": (str, False),
        "VpcId": (str, False),
    }


class VpcSecurityGroup(AWSProperty):
    """
    `VpcSecurityGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html>`__
    """

    props: PropsDictType = {
        "Status": (str, False),
        "VpcSecurityGroupId": (str, False),
    }