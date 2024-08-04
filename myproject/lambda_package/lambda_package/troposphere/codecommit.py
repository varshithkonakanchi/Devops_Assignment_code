# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators.codecommit import validate_trigger


class S3(AWSProperty):
    """
    `S3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "Key": (str, True),
        "ObjectVersion": (str, False),
    }


class Code(AWSProperty):
    """
    `Code <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html>`__
    """

    props: PropsDictType = {
        "BranchName": (str, False),
        "S3": (S3, True),
    }


class Trigger(AWSProperty):
    """
    `Trigger <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html>`__
    """

    props: PropsDictType = {
        "Branches": ([str], False),
        "CustomData": (str, False),
        "DestinationArn": (str, True),
        "Events": ([str], True),
        "Name": (str, True),
    }

    def validate(self):
        validate_trigger(self)


class Repository(AWSObject):
    """
    `Repository <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html>`__
    """

    resource_type = "AWS::CodeCommit::Repository"

    props: PropsDictType = {
        "Code": (Code, False),
        "KmsKeyId": (str, False),
        "RepositoryDescription": (str, False),
        "RepositoryName": (str, True),
        "Tags": (Tags, False),
        "Triggers": ([Trigger], False),
    }