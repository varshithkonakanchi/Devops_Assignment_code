# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.acmpca import (
    validate_certificateauthority_type,
    validate_key_algorithm,
    validate_signing_algorithm,
    validate_validity_type,
)


class CustomExtension(AWSProperty):
    """
    `CustomExtension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customextension.html>`__
    """

    props: PropsDictType = {
        "Critical": (boolean, False),
        "ObjectIdentifier": (str, True),
        "Value": (str, True),
    }


class ExtendedKeyUsage(AWSProperty):
    """
    `ExtendedKeyUsage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html>`__
    """

    props: PropsDictType = {
        "ExtendedKeyUsageObjectIdentifier": (str, False),
        "ExtendedKeyUsageType": (str, False),
    }


class EdiPartyName(AWSProperty):
    """
    `EdiPartyName <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html>`__
    """

    props: PropsDictType = {
        "NameAssigner": (str, False),
        "PartyName": (str, True),
    }


class OtherName(AWSProperty):
    """
    `OtherName <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html>`__
    """

    props: PropsDictType = {
        "TypeId": (str, True),
        "Value": (str, True),
    }


class CustomAttribute(AWSProperty):
    """
    `CustomAttribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-customattribute.html>`__
    """

    props: PropsDictType = {
        "ObjectIdentifier": (str, True),
        "Value": (str, True),
    }


class Subject(AWSProperty):
    """
    `Subject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html>`__
    """

    props: PropsDictType = {
        "CommonName": (str, False),
        "Country": (str, False),
        "CustomAttributes": ([CustomAttribute], False),
        "DistinguishedNameQualifier": (str, False),
        "GenerationQualifier": (str, False),
        "GivenName": (str, False),
        "Initials": (str, False),
        "Locality": (str, False),
        "Organization": (str, False),
        "OrganizationalUnit": (str, False),
        "Pseudonym": (str, False),
        "SerialNumber": (str, False),
        "State": (str, False),
        "Surname": (str, False),
        "Title": (str, False),
    }


class GeneralName(AWSProperty):
    """
    `GeneralName <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html>`__
    """

    props: PropsDictType = {
        "DirectoryName": (Subject, False),
        "DnsName": (str, False),
        "EdiPartyName": (EdiPartyName, False),
        "IpAddress": (str, False),
        "OtherName": (OtherName, False),
        "RegisteredId": (str, False),
        "Rfc822Name": (str, False),
        "UniformResourceIdentifier": (str, False),
    }


class KeyUsage(AWSProperty):
    """
    `KeyUsage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html>`__
    """

    props: PropsDictType = {
        "CRLSign": (boolean, False),
        "DataEncipherment": (boolean, False),
        "DecipherOnly": (boolean, False),
        "DigitalSignature": (boolean, False),
        "EncipherOnly": (boolean, False),
        "KeyAgreement": (boolean, False),
        "KeyCertSign": (boolean, False),
        "KeyEncipherment": (boolean, False),
        "NonRepudiation": (boolean, False),
    }


class Qualifier(AWSProperty):
    """
    `Qualifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-qualifier.html>`__
    """

    props: PropsDictType = {
        "CpsUri": (str, True),
    }


class PolicyQualifierInfo(AWSProperty):
    """
    `PolicyQualifierInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html>`__
    """

    props: PropsDictType = {
        "PolicyQualifierId": (str, True),
        "Qualifier": (Qualifier, True),
    }


class PolicyInformation(AWSProperty):
    """
    `PolicyInformation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html>`__
    """

    props: PropsDictType = {
        "CertPolicyId": (str, True),
        "PolicyQualifiers": ([PolicyQualifierInfo], False),
    }


class Extensions(AWSProperty):
    """
    `Extensions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html>`__
    """

    props: PropsDictType = {
        "CertificatePolicies": ([PolicyInformation], False),
        "CustomExtensions": ([CustomExtension], False),
        "ExtendedKeyUsage": ([ExtendedKeyUsage], False),
        "KeyUsage": (KeyUsage, False),
        "SubjectAlternativeNames": ([GeneralName], False),
    }


class ApiPassthrough(AWSProperty):
    """
    `ApiPassthrough <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html>`__
    """

    props: PropsDictType = {
        "Extensions": (Extensions, False),
        "Subject": (Subject, False),
    }


class Validity(AWSProperty):
    """
    `Validity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html>`__
    """

    props: PropsDictType = {
        "Type": (validate_validity_type, True),
        "Value": (double, True),
    }


class Certificate(AWSObject):
    """
    `Certificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html>`__
    """

    resource_type = "AWS::ACMPCA::Certificate"

    props: PropsDictType = {
        "ApiPassthrough": (ApiPassthrough, False),
        "CertificateAuthorityArn": (str, True),
        "CertificateSigningRequest": (str, True),
        "SigningAlgorithm": (validate_signing_algorithm, True),
        "TemplateArn": (str, False),
        "Validity": (Validity, True),
        "ValidityNotBefore": (Validity, False),
    }


class AccessMethod(AWSProperty):
    """
    `AccessMethod <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html>`__
    """

    props: PropsDictType = {
        "AccessMethodType": (str, False),
        "CustomObjectIdentifier": (str, False),
    }


class AccessDescription(AWSProperty):
    """
    `AccessDescription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html>`__
    """

    props: PropsDictType = {
        "AccessLocation": (GeneralName, True),
        "AccessMethod": (AccessMethod, True),
    }


class CsrExtensions(AWSProperty):
    """
    `CsrExtensions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html>`__
    """

    props: PropsDictType = {
        "KeyUsage": (KeyUsage, False),
        "SubjectInformationAccess": ([AccessDescription], False),
    }


class CrlDistributionPointExtensionConfiguration(AWSProperty):
    """
    `CrlDistributionPointExtensionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crldistributionpointextensionconfiguration.html>`__
    """

    props: PropsDictType = {
        "OmitExtension": (boolean, True),
    }


class CrlConfiguration(AWSProperty):
    """
    `CrlConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html>`__
    """

    props: PropsDictType = {
        "CrlDistributionPointExtensionConfiguration": (
            CrlDistributionPointExtensionConfiguration,
            False,
        ),
        "CustomCname": (str, False),
        "Enabled": (boolean, True),
        "ExpirationInDays": (integer, False),
        "S3BucketName": (str, False),
        "S3ObjectAcl": (str, False),
    }


class OcspConfiguration(AWSProperty):
    """
    `OcspConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
        "OcspCustomCname": (str, False),
    }


class RevocationConfiguration(AWSProperty):
    """
    `RevocationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html>`__
    """

    props: PropsDictType = {
        "CrlConfiguration": (CrlConfiguration, False),
        "OcspConfiguration": (OcspConfiguration, False),
    }


class CertificateAuthority(AWSObject):
    """
    `CertificateAuthority <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html>`__
    """

    resource_type = "AWS::ACMPCA::CertificateAuthority"

    props: PropsDictType = {
        "CsrExtensions": (CsrExtensions, False),
        "KeyAlgorithm": (validate_key_algorithm, True),
        "KeyStorageSecurityStandard": (str, False),
        "RevocationConfiguration": (RevocationConfiguration, False),
        "SigningAlgorithm": (validate_signing_algorithm, True),
        "Subject": (Subject, True),
        "Tags": (Tags, False),
        "Type": (validate_certificateauthority_type, True),
        "UsageMode": (str, False),
    }


class CertificateAuthorityActivation(AWSObject):
    """
    `CertificateAuthorityActivation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html>`__
    """

    resource_type = "AWS::ACMPCA::CertificateAuthorityActivation"

    props: PropsDictType = {
        "Certificate": (str, True),
        "CertificateAuthorityArn": (str, True),
        "CertificateChain": (str, False),
        "Status": (str, False),
    }


class Permission(AWSObject):
    """
    `Permission <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html>`__
    """

    resource_type = "AWS::ACMPCA::Permission"

    props: PropsDictType = {
        "Actions": ([str], True),
        "CertificateAuthorityArn": (str, True),
        "Principal": (str, True),
        "SourceAccount": (str, False),
    }
