# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags


class AugmentedManifestsListItem(AWSProperty):
    """
    `AugmentedManifestsListItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-augmentedmanifestslistitem.html>`__
    """

    props: PropsDictType = {
        "AttributeNames": ([str], True),
        "S3Uri": (str, True),
        "Split": (str, False),
    }


class DocumentClassifierDocuments(AWSProperty):
    """
    `DocumentClassifierDocuments <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierdocuments.html>`__
    """

    props: PropsDictType = {
        "S3Uri": (str, True),
        "TestS3Uri": (str, False),
    }


class DocumentReaderConfig(AWSProperty):
    """
    `DocumentReaderConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentreaderconfig.html>`__
    """

    props: PropsDictType = {
        "DocumentReadAction": (str, True),
        "DocumentReadMode": (str, False),
        "FeatureTypes": ([str], False),
    }


class DocumentClassifierInputDataConfig(AWSProperty):
    """
    `DocumentClassifierInputDataConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html>`__
    """

    props: PropsDictType = {
        "AugmentedManifests": ([AugmentedManifestsListItem], False),
        "DataFormat": (str, False),
        "DocumentReaderConfig": (DocumentReaderConfig, False),
        "DocumentType": (str, False),
        "Documents": (DocumentClassifierDocuments, False),
        "LabelDelimiter": (str, False),
        "S3Uri": (str, False),
        "TestS3Uri": (str, False),
    }


class DocumentClassifierOutputDataConfig(AWSProperty):
    """
    `DocumentClassifierOutputDataConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "S3Uri": (str, False),
    }


class VpcConfig(AWSProperty):
    """
    `VpcConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], True),
        "Subnets": ([str], True),
    }


class DocumentClassifier(AWSObject):
    """
    `DocumentClassifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html>`__
    """

    resource_type = "AWS::Comprehend::DocumentClassifier"

    props: PropsDictType = {
        "DataAccessRoleArn": (str, True),
        "DocumentClassifierName": (str, True),
        "InputDataConfig": (DocumentClassifierInputDataConfig, True),
        "LanguageCode": (str, True),
        "Mode": (str, False),
        "ModelKmsKeyId": (str, False),
        "ModelPolicy": (str, False),
        "OutputDataConfig": (DocumentClassifierOutputDataConfig, False),
        "Tags": (Tags, False),
        "VersionName": (str, False),
        "VolumeKmsKeyId": (str, False),
        "VpcConfig": (VpcConfig, False),
    }


class DataSecurityConfig(AWSProperty):
    """
    `DataSecurityConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html>`__
    """

    props: PropsDictType = {
        "DataLakeKmsKeyId": (str, False),
        "ModelKmsKeyId": (str, False),
        "VolumeKmsKeyId": (str, False),
        "VpcConfig": (VpcConfig, False),
    }


class DocumentClassificationConfig(AWSProperty):
    """
    `DocumentClassificationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html>`__
    """

    props: PropsDictType = {
        "Labels": ([str], False),
        "Mode": (str, True),
    }


class EntityTypesListItem(AWSProperty):
    """
    `EntityTypesListItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entitytypeslistitem.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
    }


class EntityRecognitionConfig(AWSProperty):
    """
    `EntityRecognitionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entityrecognitionconfig.html>`__
    """

    props: PropsDictType = {
        "EntityTypes": ([EntityTypesListItem], False),
    }


class TaskConfig(AWSProperty):
    """
    `TaskConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html>`__
    """

    props: PropsDictType = {
        "DocumentClassificationConfig": (DocumentClassificationConfig, False),
        "EntityRecognitionConfig": (EntityRecognitionConfig, False),
        "LanguageCode": (str, True),
    }


class Flywheel(AWSObject):
    """
    `Flywheel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html>`__
    """

    resource_type = "AWS::Comprehend::Flywheel"

    props: PropsDictType = {
        "ActiveModelArn": (str, False),
        "DataAccessRoleArn": (str, True),
        "DataLakeS3Uri": (str, True),
        "DataSecurityConfig": (DataSecurityConfig, False),
        "FlywheelName": (str, True),
        "ModelType": (str, False),
        "Tags": (Tags, False),
        "TaskConfig": (TaskConfig, False),
    }
