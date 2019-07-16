# coding: utf-8
# fmt: off
from typing import List
from typing import Callable
from typing import Optional
from typing import IO
from datetime import datetime
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.waiter import Waiter
from typing import Dict
from botocore.paginate import Paginator
from typing import Union


class Client(BaseClient):
    def abort_multipart_upload(
        self,
        Bucket,  # type: str
        Key,  # type: str
        UploadId,  # type: str
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Aborts a multipart upload.
        To verify that all parts have been removed, so you don't get charged for the part storage, you should call the List Parts operation and ensure the parts list is empty.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/AbortMultipartUpload>`_
        
        **Request Syntax**
        ::
          response = client.abort_multipart_upload(
              Bucket='string',
              Key='string',
              UploadId='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          Name of the bucket to which the multipart upload was initiated.
        :type Key: string
        :param Key: **[REQUIRED]**
          Key of the object for which the multipart upload was initiated.
        :type UploadId: string
        :param UploadId: **[REQUIRED]**
          Upload ID that identifies the multipart upload.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass

    def can_paginate(
        self,
        operation_name=None,  # type: Optional[str]
    ):
        # type: (...) -> None
        """
        Check if an operation can be paginated.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def complete_multipart_upload(
        self,
        Bucket,  # type: str
        Key,  # type: str
        UploadId,  # type: str
        MultipartUpload=None,  # type: Optional[Dict]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Completes a multipart upload by assembling previously uploaded parts.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CompleteMultipartUpload>`_
        
        **Request Syntax**
        ::
          response = client.complete_multipart_upload(
              Bucket='string',
              Key='string',
              MultipartUpload={
                  'Parts': [
                      {
                          'ETag': 'string',
                          'PartNumber': 123
                      },
                  ]
              },
              UploadId='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'Location': 'string',
                'Bucket': 'string',
                'Key': 'string',
                'Expiration': 'string',
                'ETag': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'VersionId': 'string',
                'SSEKMSKeyId': 'string',
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Location** *(string) --* 
            - **Bucket** *(string) --* 
            - **Key** *(string) --* 
            - **Expiration** *(string) --* 
              If the object expiration is configured, this will contain the expiration date (expiry-date) and rule ID (rule-id). The value of rule-id is URL encoded.
            - **ETag** *(string) --* 
              Entity tag of the object.
            - **ServerSideEncryption** *(string) --* 
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
            - **VersionId** *(string) --* 
              Version of the object.
            - **SSEKMSKeyId** *(string) --* 
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Key: string
        :param Key: **[REQUIRED]**
        :type MultipartUpload: dict
        :param MultipartUpload:
          - **Parts** *(list) --*
            - *(dict) --*
              - **ETag** *(string) --*
                Entity tag returned when the part was uploaded.
              - **PartNumber** *(integer) --*
                Part number that identifies the part. This is a positive integer between 1 and 10,000.
        :type UploadId: string
        :param UploadId: **[REQUIRED]**
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass

    def copy(
        self,
        CopySource=None,  # type: Optional[Dict]
        Bucket=None,  # type: Optional[str]
        Key=None,  # type: Optional[str]
        ExtraArgs=None,  # type: Optional[Dict]
        Callback=None,  # type: Optional[Callable]
        SourceClient=None,  # type: Optional[BaseClient]
        Config=None,  # type: Optional[TransferConfig]
    ):
        # type: (...) -> None
        """
        Copy an object from one S3 location to another.
        This is a managed transfer which will perform a multipart copy in
        multiple threads if necessary.
        Usage::
            import boto3
            s3 = boto3.resource('s3')
            copy_source = {
                'Bucket': 'mybucket',
                'Key': 'mykey'
            }
            s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')
        :type CopySource: dict
        :param CopySource: The name of the source bucket, key name of the
            source object, and optional version ID of the source object. The
            dictionary format is:
            ``{\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}``. Note
            that the ``VersionId`` key is optional and may be omitted.
        :type Bucket: str
        :param Bucket: The name of the bucket to copy to
        :type Key: str
        :param Key: The name of the key to copy to
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the copy.
        :type SourceClient: botocore or boto3 Client
        :param SourceClient: The client to be used for operation that
            may happen at the source object. For example, this client is
            used for the head_object that determines the size of the copy.
            If no client is provided, the current client is used as the client
            for the source object.
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            copy.
        """
        pass

    def copy_object(
        self,
        Bucket,  # type: str
        CopySource,  # type: Union[str, Dict]
        Key,  # type: str
        ACL=None,  # type: Optional[str]
        CacheControl=None,  # type: Optional[str]
        ContentDisposition=None,  # type: Optional[str]
        ContentEncoding=None,  # type: Optional[str]
        ContentLanguage=None,  # type: Optional[str]
        ContentType=None,  # type: Optional[str]
        CopySourceIfMatch=None,  # type: Optional[str]
        CopySourceIfModifiedSince=None,  # type: Optional[datetime]
        CopySourceIfNoneMatch=None,  # type: Optional[str]
        CopySourceIfUnmodifiedSince=None,  # type: Optional[datetime]
        Expires=None,  # type: Optional[datetime]
        GrantFullControl=None,  # type: Optional[str]
        GrantRead=None,  # type: Optional[str]
        GrantReadACP=None,  # type: Optional[str]
        GrantWriteACP=None,  # type: Optional[str]
        Metadata=None,  # type: Optional[Dict]
        MetadataDirective=None,  # type: Optional[str]
        TaggingDirective=None,  # type: Optional[str]
        ServerSideEncryption=None,  # type: Optional[str]
        StorageClass=None,  # type: Optional[str]
        WebsiteRedirectLocation=None,  # type: Optional[str]
        SSECustomerAlgorithm=None,  # type: Optional[str]
        SSECustomerKey=None,  # type: Optional[str]
        SSECustomerKeyMD5=None,  # type: Optional[str]
        SSEKMSKeyId=None,  # type: Optional[str]
        SSEKMSEncryptionContext=None,  # type: Optional[str]
        CopySourceSSECustomerAlgorithm=None,  # type: Optional[str]
        CopySourceSSECustomerKey=None,  # type: Optional[str]
        CopySourceSSECustomerKeyMD5=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
        Tagging=None,  # type: Optional[str]
        ObjectLockMode=None,  # type: Optional[str]
        ObjectLockRetainUntilDate=None,  # type: Optional[datetime]
        ObjectLockLegalHoldStatus=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Creates a copy of an object that is already stored in Amazon S3.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CopyObject>`_
        
        **Request Syntax**
        ::
          response = client.copy_object(
              ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
              Bucket='string',
              CacheControl='string',
              ContentDisposition='string',
              ContentEncoding='string',
              ContentLanguage='string',
              ContentType='string',
              CopySource='string' or {'Bucket': 'string', 'Key': 'string', 'VersionId': 'string'},
              CopySourceIfMatch='string',
              CopySourceIfModifiedSince=datetime(2015, 1, 1),
              CopySourceIfNoneMatch='string',
              CopySourceIfUnmodifiedSince=datetime(2015, 1, 1),
              Expires=datetime(2015, 1, 1),
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWriteACP='string',
              Key='string',
              Metadata={
                  'string': 'string'
              },
              MetadataDirective='COPY'|'REPLACE',
              TaggingDirective='COPY'|'REPLACE',
              ServerSideEncryption='AES256'|'aws:kms',
              StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
              WebsiteRedirectLocation='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              SSEKMSKeyId='string',
              SSEKMSEncryptionContext='string',
              CopySourceSSECustomerAlgorithm='string',
              CopySourceSSECustomerKey='string',
              RequestPayer='requester',
              Tagging='string',
              ObjectLockMode='GOVERNANCE'|'COMPLIANCE',
              ObjectLockRetainUntilDate=datetime(2015, 1, 1),
              ObjectLockLegalHoldStatus='ON'|'OFF'
          )
        
        **Response Syntax**
        ::
            {
                'CopyObjectResult': {
                    'ETag': 'string',
                    'LastModified': datetime(2015, 1, 1)
                },
                'Expiration': 'string',
                'CopySourceVersionId': 'string',
                'VersionId': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'SSEKMSEncryptionContext': 'string',
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CopyObjectResult** *(dict) --* 
              - **ETag** *(string) --* 
              - **LastModified** *(datetime) --* 
            - **Expiration** *(string) --* 
              If the object expiration is configured, the response includes this header.
            - **CopySourceVersionId** *(string) --* 
            - **VersionId** *(string) --* 
              Version ID of the newly created copy.
            - **ServerSideEncryption** *(string) --* 
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
            - **SSECustomerAlgorithm** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
            - **SSECustomerKeyMD5** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
            - **SSEKMSKeyId** *(string) --* 
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
            - **SSEKMSEncryptionContext** *(string) --* 
              If present, specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type ACL: string
        :param ACL:
          The canned ACL to apply to the object.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type CacheControl: string
        :param CacheControl:
          Specifies caching behavior along the request/reply chain.
        :type ContentDisposition: string
        :param ContentDisposition:
          Specifies presentational information for the object.
        :type ContentEncoding: string
        :param ContentEncoding:
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        :type ContentLanguage: string
        :param ContentLanguage:
          The language the content is in.
        :type ContentType: string
        :param ContentType:
          A standard MIME type describing the format of the object data.
        :type CopySource: str or dict
        :param CopySource: **[REQUIRED]** The name of the source bucket, key name of the source object, and optional version ID of the source object.  You can either provide this value as a string or a dictionary.  The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version.  You can also provide this value as a dictionary.  The dictionary format is recommended over the string format because it is more explicit.  The dictionary format is: {\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}.  Note that the VersionId key is optional and may be omitted.
        :type CopySourceIfMatch: string
        :param CopySourceIfMatch:
          Copies the object if its entity tag (ETag) matches the specified tag.
        :type CopySourceIfModifiedSince: datetime
        :param CopySourceIfModifiedSince:
          Copies the object if it has been modified since the specified time.
        :type CopySourceIfNoneMatch: string
        :param CopySourceIfNoneMatch:
          Copies the object if its entity tag (ETag) is different than the specified ETag.
        :type CopySourceIfUnmodifiedSince: datetime
        :param CopySourceIfUnmodifiedSince:
          Copies the object if it hasn\'t been modified since the specified time.
        :type Expires: datetime
        :param Expires:
          The date and time at which the object is no longer cacheable.
        :type GrantFullControl: string
        :param GrantFullControl:
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        :type GrantRead: string
        :param GrantRead:
          Allows grantee to read the object data and its metadata.
        :type GrantReadACP: string
        :param GrantReadACP:
          Allows grantee to read the object ACL.
        :type GrantWriteACP: string
        :param GrantWriteACP:
          Allows grantee to write the ACL for the applicable object.
        :type Key: string
        :param Key: **[REQUIRED]**
        :type Metadata: dict
        :param Metadata:
          A map of metadata to store with the object in S3.
          - *(string) --*
            - *(string) --*
        :type MetadataDirective: string
        :param MetadataDirective:
          Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request.
        :type TaggingDirective: string
        :param TaggingDirective:
          Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request.
        :type ServerSideEncryption: string
        :param ServerSideEncryption:
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        :type StorageClass: string
        :param StorageClass:
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation:
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        :type SSECustomerKey: string
        :param SSECustomerKey:
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId:
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        :type SSEKMSEncryptionContext: string
        :param SSEKMSEncryptionContext:
          Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
        :type CopySourceSSECustomerAlgorithm: string
        :param CopySourceSSECustomerAlgorithm:
          Specifies the algorithm to use when decrypting the source object (e.g., AES256).
        :type CopySourceSSECustomerKey: string
        :param CopySourceSSECustomerKey:
          Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.
        :type CopySourceSSECustomerKeyMD5: string
        :param CopySourceSSECustomerKeyMD5:
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type Tagging: string
        :param Tagging:
          The tag-set for the object destination object this value must be used in conjunction with the TaggingDirective. The tag-set must be encoded as URL Query parameters
        :type ObjectLockMode: string
        :param ObjectLockMode:
          The object lock mode that you want to apply to the copied object.
        :type ObjectLockRetainUntilDate: datetime
        :param ObjectLockRetainUntilDate:
          The date and time when you want the copied object\'s object lock to expire.
        :type ObjectLockLegalHoldStatus: string
        :param ObjectLockLegalHoldStatus:
          Specifies whether you want to apply a Legal Hold to the copied object.
        :rtype: dict
        :returns:
        """
        pass

    def create_bucket(
        self,
        Bucket,  # type: str
        ACL=None,  # type: Optional[str]
        CreateBucketConfiguration=None,  # type: Optional[Dict]
        GrantFullControl=None,  # type: Optional[str]
        GrantRead=None,  # type: Optional[str]
        GrantReadACP=None,  # type: Optional[str]
        GrantWrite=None,  # type: Optional[str]
        GrantWriteACP=None,  # type: Optional[str]
        ObjectLockEnabledForBucket=None,  # type: Optional[bool]
    ):
        # type: (...) -> Dict
        """
        Creates a new bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CreateBucket>`_
        
        **Request Syntax**
        ::
          response = client.create_bucket(
              ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
              Bucket='string',
              CreateBucketConfiguration={
                  'LocationConstraint': 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
              },
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWrite='string',
              GrantWriteACP='string',
              ObjectLockEnabledForBucket=True|False
          )
        
        **Response Syntax**
        ::
            {
                'Location': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Location** *(string) --* 
        :type ACL: string
        :param ACL:
          The canned ACL to apply to the bucket.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type CreateBucketConfiguration: dict
        :param CreateBucketConfiguration:
          - **LocationConstraint** *(string) --*
            Specifies the region where the bucket will be created. If you don\'t specify a region, the bucket is created in US East (N. Virginia) Region (us-east-1).
        :type GrantFullControl: string
        :param GrantFullControl:
          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
        :type GrantRead: string
        :param GrantRead:
          Allows grantee to list the objects in the bucket.
        :type GrantReadACP: string
        :param GrantReadACP:
          Allows grantee to read the bucket ACL.
        :type GrantWrite: string
        :param GrantWrite:
          Allows grantee to create, overwrite, and delete any object in the bucket.
        :type GrantWriteACP: string
        :param GrantWriteACP:
          Allows grantee to write the ACL for the applicable bucket.
        :type ObjectLockEnabledForBucket: boolean
        :param ObjectLockEnabledForBucket:
          Specifies whether you want Amazon S3 object lock to be enabled for the new bucket.
        :rtype: dict
        :returns:
        """
        pass

    def create_multipart_upload(
        self,
        Bucket,  # type: str
        Key,  # type: str
        ACL=None,  # type: Optional[str]
        CacheControl=None,  # type: Optional[str]
        ContentDisposition=None,  # type: Optional[str]
        ContentEncoding=None,  # type: Optional[str]
        ContentLanguage=None,  # type: Optional[str]
        ContentType=None,  # type: Optional[str]
        Expires=None,  # type: Optional[datetime]
        GrantFullControl=None,  # type: Optional[str]
        GrantRead=None,  # type: Optional[str]
        GrantReadACP=None,  # type: Optional[str]
        GrantWriteACP=None,  # type: Optional[str]
        Metadata=None,  # type: Optional[Dict]
        ServerSideEncryption=None,  # type: Optional[str]
        StorageClass=None,  # type: Optional[str]
        WebsiteRedirectLocation=None,  # type: Optional[str]
        SSECustomerAlgorithm=None,  # type: Optional[str]
        SSECustomerKey=None,  # type: Optional[str]
        SSECustomerKeyMD5=None,  # type: Optional[str]
        SSEKMSKeyId=None,  # type: Optional[str]
        SSEKMSEncryptionContext=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
        Tagging=None,  # type: Optional[str]
        ObjectLockMode=None,  # type: Optional[str]
        ObjectLockRetainUntilDate=None,  # type: Optional[datetime]
        ObjectLockLegalHoldStatus=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Initiates a multipart upload and returns an upload ID.
         **Note:** After you initiate multipart upload and upload one or more parts, you must either complete or abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you for the parts storage.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CreateMultipartUpload>`_
        
        **Request Syntax**
        ::
          response = client.create_multipart_upload(
              ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
              Bucket='string',
              CacheControl='string',
              ContentDisposition='string',
              ContentEncoding='string',
              ContentLanguage='string',
              ContentType='string',
              Expires=datetime(2015, 1, 1),
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWriteACP='string',
              Key='string',
              Metadata={
                  'string': 'string'
              },
              ServerSideEncryption='AES256'|'aws:kms',
              StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
              WebsiteRedirectLocation='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              SSEKMSKeyId='string',
              SSEKMSEncryptionContext='string',
              RequestPayer='requester',
              Tagging='string',
              ObjectLockMode='GOVERNANCE'|'COMPLIANCE',
              ObjectLockRetainUntilDate=datetime(2015, 1, 1),
              ObjectLockLegalHoldStatus='ON'|'OFF'
          )
        
        **Response Syntax**
        ::
            {
                'AbortDate': datetime(2015, 1, 1),
                'AbortRuleId': 'string',
                'Bucket': 'string',
                'Key': 'string',
                'UploadId': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'SSEKMSEncryptionContext': 'string',
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AbortDate** *(datetime) --* 
              Date when multipart upload will become eligible for abort operation by lifecycle.
            - **AbortRuleId** *(string) --* 
              Id of the lifecycle rule that makes a multipart upload eligible for abort operation.
            - **Bucket** *(string) --* 
              Name of the bucket to which the multipart upload was initiated.
            - **Key** *(string) --* 
              Object key for which the multipart upload was initiated.
            - **UploadId** *(string) --* 
              ID for the initiated multipart upload.
            - **ServerSideEncryption** *(string) --* 
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
            - **SSECustomerAlgorithm** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
            - **SSECustomerKeyMD5** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
            - **SSEKMSKeyId** *(string) --* 
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
            - **SSEKMSEncryptionContext** *(string) --* 
              If present, specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type ACL: string
        :param ACL:
          The canned ACL to apply to the object.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type CacheControl: string
        :param CacheControl:
          Specifies caching behavior along the request/reply chain.
        :type ContentDisposition: string
        :param ContentDisposition:
          Specifies presentational information for the object.
        :type ContentEncoding: string
        :param ContentEncoding:
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        :type ContentLanguage: string
        :param ContentLanguage:
          The language the content is in.
        :type ContentType: string
        :param ContentType:
          A standard MIME type describing the format of the object data.
        :type Expires: datetime
        :param Expires:
          The date and time at which the object is no longer cacheable.
        :type GrantFullControl: string
        :param GrantFullControl:
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        :type GrantRead: string
        :param GrantRead:
          Allows grantee to read the object data and its metadata.
        :type GrantReadACP: string
        :param GrantReadACP:
          Allows grantee to read the object ACL.
        :type GrantWriteACP: string
        :param GrantWriteACP:
          Allows grantee to write the ACL for the applicable object.
        :type Key: string
        :param Key: **[REQUIRED]**
        :type Metadata: dict
        :param Metadata:
          A map of metadata to store with the object in S3.
          - *(string) --*
            - *(string) --*
        :type ServerSideEncryption: string
        :param ServerSideEncryption:
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        :type StorageClass: string
        :param StorageClass:
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation:
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        :type SSECustomerKey: string
        :param SSECustomerKey:
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId:
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        :type SSEKMSEncryptionContext: string
        :param SSEKMSEncryptionContext:
          Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type Tagging: string
        :param Tagging:
          The tag-set for the object. The tag-set must be encoded as URL Query parameters
        :type ObjectLockMode: string
        :param ObjectLockMode:
          Specifies the object lock mode that you want to apply to the uploaded object.
        :type ObjectLockRetainUntilDate: datetime
        :param ObjectLockRetainUntilDate:
          Specifies the date and time when you want the object lock to expire.
        :type ObjectLockLegalHoldStatus: string
        :param ObjectLockLegalHoldStatus:
          Specifies whether you want to apply a Legal Hold to the uploaded object.
        :rtype: dict
        :returns:
        """
        pass

    def delete_bucket(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes the bucket. All objects (including all object versions and Delete Markers) in the bucket must be deleted before the bucket itself can be deleted.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucket>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :returns: None
        """
        pass

    def delete_bucket_analytics_configuration(
        self,
        Bucket,  # type: str
        Id,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes an analytics configuration for the bucket (specified by the analytics configuration ID).
        To use this operation, you must have permissions to perform the s3:PutAnalyticsConfiguration action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketAnalyticsConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_analytics_configuration(
              Bucket='string',
              Id='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket from which an analytics configuration is deleted.
        :type Id: string
        :param Id: **[REQUIRED]**
          The ID that identifies the analytics configuration.
        :returns: None
        """
        pass

    def delete_bucket_cors(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes the CORS configuration information set for the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketCors>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_cors(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :returns: None
        """
        pass

    def delete_bucket_encryption(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes the server-side encryption configuration from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketEncryption>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_encryption(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket containing the server-side encryption configuration to delete.
        :returns: None
        """
        pass

    def delete_bucket_inventory_configuration(
        self,
        Bucket,  # type: str
        Id,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes an inventory configuration (identified by the inventory ID) from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketInventoryConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_inventory_configuration(
              Bucket='string',
              Id='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket containing the inventory configuration to delete.
        :type Id: string
        :param Id: **[REQUIRED]**
          The ID used to identify the inventory configuration.
        :returns: None
        """
        pass

    def delete_bucket_lifecycle(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes the lifecycle configuration from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketLifecycle>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_lifecycle(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :returns: None
        """
        pass

    def delete_bucket_metrics_configuration(
        self,
        Bucket,  # type: str
        Id,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes a metrics configuration (specified by the metrics configuration ID) from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketMetricsConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_metrics_configuration(
              Bucket='string',
              Id='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket containing the metrics configuration to delete.
        :type Id: string
        :param Id: **[REQUIRED]**
          The ID used to identify the metrics configuration.
        :returns: None
        """
        pass

    def delete_bucket_policy(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes the policy from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketPolicy>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_policy(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :returns: None
        """
        pass

    def delete_bucket_replication(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes the replication configuration from the bucket. For information about replication configuration, see `Cross-Region Replication (CRR) <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html>`__ in the *Amazon S3 Developer Guide* . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketReplication>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_replication(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The bucket name.
          .. note::
            It can take a while to propagate the deletion of a replication configuration to all Amazon S3 systems.
        :returns: None
        """
        pass

    def delete_bucket_tagging(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        Deletes the tags from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketTagging>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_tagging(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :returns: None
        """
        pass

    def delete_bucket_website(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        This operation removes the website configuration from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketWebsite>`_
        
        **Request Syntax**
        ::
          response = client.delete_bucket_website(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :returns: None
        """
        pass

    def delete_object(
        self,
        Bucket,  # type: str
        Key,  # type: str
        MFA=None,  # type: Optional[str]
        VersionId=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
        BypassGovernanceRetention=None,  # type: Optional[bool]
    ):
        # type: (...) -> Dict
        """
        Removes the null version (if there is one) of an object and inserts a delete marker, which becomes the latest version of the object. If there isn't a null version, Amazon S3 does not remove any objects.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObject>`_
        
        **Request Syntax**
        ::
          response = client.delete_object(
              Bucket='string',
              Key='string',
              MFA='string',
              VersionId='string',
              RequestPayer='requester',
              BypassGovernanceRetention=True|False
          )
        
        **Response Syntax**
        ::
            {
                'DeleteMarker': True|False,
                'VersionId': 'string',
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DeleteMarker** *(boolean) --* 
              Specifies whether the versioned object that was permanently deleted was (true) or was not (false) a delete marker.
            - **VersionId** *(string) --* 
              Returns the version ID of the delete marker created as a result of the DELETE operation.
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Key: string
        :param Key: **[REQUIRED]**
        :type MFA: string
        :param MFA:
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        :type VersionId: string
        :param VersionId:
          VersionId used to reference a specific version of the object.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type BypassGovernanceRetention: boolean
        :param BypassGovernanceRetention:
          Indicates whether Amazon S3 object lock should bypass governance-mode restrictions to process this operation.
        :rtype: dict
        :returns:
        """
        pass

    def delete_object_tagging(
        self,
        Bucket,  # type: str
        Key,  # type: str
        VersionId=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Removes the tag-set from an existing object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObjectTagging>`_
        
        **Request Syntax**
        ::
          response = client.delete_object_tagging(
              Bucket='string',
              Key='string',
              VersionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'VersionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VersionId** *(string) --* 
              The versionId of the object the tag-set was removed from.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Key: string
        :param Key: **[REQUIRED]**
        :type VersionId: string
        :param VersionId:
          The versionId of the object that the tag-set will be removed from.
        :rtype: dict
        :returns:
        """
        pass

    def delete_objects(
        self,
        Bucket,  # type: str
        Delete,  # type: Dict
        MFA=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
        BypassGovernanceRetention=None,  # type: Optional[bool]
    ):
        # type: (...) -> Dict
        """
        This operation enables you to delete multiple objects from a bucket using a single HTTP request. You may specify up to 1000 keys.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObjects>`_
        
        **Request Syntax**
        ::
          response = client.delete_objects(
              Bucket='string',
              Delete={
                  'Objects': [
                      {
                          'Key': 'string',
                          'VersionId': 'string'
                      },
                  ],
                  'Quiet': True|False
              },
              MFA='string',
              RequestPayer='requester',
              BypassGovernanceRetention=True|False
          )
        
        **Response Syntax**
        ::
            {
                'Deleted': [
                    {
                        'Key': 'string',
                        'VersionId': 'string',
                        'DeleteMarker': True|False,
                        'DeleteMarkerVersionId': 'string'
                    },
                ],
                'RequestCharged': 'requester',
                'Errors': [
                    {
                        'Key': 'string',
                        'VersionId': 'string',
                        'Code': 'string',
                        'Message': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Deleted** *(list) --* 
              - *(dict) --* 
                - **Key** *(string) --* 
                - **VersionId** *(string) --* 
                - **DeleteMarker** *(boolean) --* 
                - **DeleteMarkerVersionId** *(string) --* 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
            - **Errors** *(list) --* 
              - *(dict) --* 
                - **Key** *(string) --* 
                - **VersionId** *(string) --* 
                - **Code** *(string) --* 
                - **Message** *(string) --* 
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Delete: dict
        :param Delete: **[REQUIRED]**
          - **Objects** *(list) --* **[REQUIRED]**
            - *(dict) --*
              - **Key** *(string) --* **[REQUIRED]**
                Key name of the object to delete.
              - **VersionId** *(string) --*
                VersionId for the specific version of the object to delete.
          - **Quiet** *(boolean) --*
            Element to enable quiet mode for the request. When you add this element, you must set its value to true.
        :type MFA: string
        :param MFA:
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type BypassGovernanceRetention: boolean
        :param BypassGovernanceRetention:
          Specifies whether you want to delete this object even if it has a Governance-type object lock in place. You must have sufficient permissions to perform this operation.
        :rtype: dict
        :returns:
        """
        pass

    def delete_public_access_block(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        Removes the ``PublicAccessBlock`` configuration from an Amazon S3 bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeletePublicAccessBlock>`_
        
        **Request Syntax**
        ::
          response = client.delete_public_access_block(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The Amazon S3 bucket whose ``PublicAccessBlock`` configuration you want to delete.
        :returns: None
        """
        pass

    def download_file(
        self,
        Bucket=None,  # type: Optional[str]
        Key=None,  # type: Optional[str]
        Filename=None,  # type: Optional[str]
        ExtraArgs=None,  # type: Optional[Dict]
        Callback=None,  # type: Optional[Callable]
        Config=None,  # type: Optional[TransferConfig]
    ):
        # type: (...) -> None
        """
        Download an S3 object to a file.
        Usage::
            import boto3
            s3 = boto3.resource('s3')
            s3.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')
        Similar behavior as S3Transfer's download_file() method,
        except that parameters are capitalized. Detailed examples can be found at
        :ref:`S3Transfer\'s Usage <ref_s3transfer_usage>`.
        :type Bucket: str
        :param Bucket: The name of the bucket to download from.
        :type Key: str
        :param Key: The name of the key to download from.
        :type Filename: str
        :param Filename: The path to the file to download to.
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            transfer.
        """
        pass

    def download_fileobj(
        self,
        Fileobj=None,  # type: Optional[IO]
        Bucket=None,  # type: Optional[str]
        Key=None,  # type: Optional[str]
        ExtraArgs=None,  # type: Optional[Dict]
        Callback=None,  # type: Optional[Callable]
        Config=None,  # type: Optional[TransferConfig]
    ):
        # type: (...) -> None
        """
        Download an object from S3 to a file-like object.
        The file-like object must be in binary mode.
        This is a managed transfer which will perform a multipart download in
        multiple threads if necessary.
        Usage::
            import boto3
            s3 = boto3.client('s3')
            with open('filename', 'wb') as data:
                s3.download_fileobj('mybucket', 'mykey', data)
        :type Fileobj: a file-like object
        :param Fileobj: A file-like object to download into. At a minimum, it must
            implement the `write` method and must accept bytes.
        :type Bucket: str
        :param Bucket: The name of the bucket to download from.
        :type Key: str
        :param Key: The name of the key to download from.
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            download.
        """
        pass

    def generate_presigned_post(
        self,
        Bucket=None,  # type: Optional[str]
        Key=None,  # type: Optional[str]
        Fields=None,  # type: Optional[Dict]
        Conditions=None,  # type: Optional[List]
        ExpiresIn=None,  # type: Optional[int]
    ):
        # type: (...) -> Dict
        """
        Builds the url and the form fields used for a presigned s3 post
        :type Bucket: string
        :param Bucket: The name of the bucket to presign the post to. Note that
            bucket related conditions should not be included in the
            ``conditions`` parameter.
        :type Key: string
        :param Key: Key name, optionally add ${filename} to the end to
            attach the submitted filename. Note that key related conditions and
            fields are filled out for you and should not be included in the
            ``Fields`` or ``Conditions`` parameter.
        :type Fields: dict
        :param Fields: A dictionary of prefilled form fields to build on top
            of. Elements that may be included are acl, Cache-Control,
            Content-Type, Content-Disposition, Content-Encoding, Expires,
            success_action_redirect, redirect, success_action_status,
            and x-amz-meta-.
            Note that if a particular element is included in the fields
            dictionary it will not be automatically added to the conditions
            list. You must specify a condition for the element as well.
        :type Conditions: list
        :param Conditions: A list of conditions to include in the policy. Each
            element can be either a list or a structure. For example:
            [
             {\"acl\": \"public-read\"},
             [\"content-length-range\", 2, 5],
             [\"starts-with\", \"$success_action_redirect\", \"\"]
            ]
            Conditions that are included may pertain to acl,
            content-length-range, Cache-Control, Content-Type,
            Content-Disposition, Content-Encoding, Expires,
            success_action_redirect, redirect, success_action_status,
            and/or x-amz-meta-.
            Note that if you include a condition, you must specify
            the a valid value in the fields dictionary as well. A value will
            not be added automatically to the fields dictionary based on the
            conditions.
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned post
            is valid for.
        :rtype: dict
        :returns: A dictionary with two elements: ``url`` and ``fields``.
            Url is the url to post to. Fields is a dictionary filled with
            the form fields and respective values to use when submitting the
            post. For example:
            {\'url\': \'https://mybucket.s3.amazonaws.com
             \'fields\': {\'acl\': \'public-read\',
                        \'key\': \'mykey\',
                        \'signature\': \'mysignature\',
                        \'policy\': \'mybase64 encoded policy\'}
            }
        """
        pass

    def generate_presigned_url(
        self,
        ClientMethod=None,  # type: Optional[str]
        Params=None,  # type: Optional[Dict]
        ExpiresIn=None,  # type: Optional[int]
        HttpMethod=None,  # type: Optional[str]
    ):
        # type: (...) -> None
        """
        Generate a presigned url given a client, its method, and arguments
        :type ClientMethod: string
        :param ClientMethod: The client method to presign for
        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method\'s model.
        :returns: The presigned url
        """
        pass

    def get_bucket_accelerate_configuration(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the accelerate configuration of a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketAccelerateConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_accelerate_configuration(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'Status': 'Enabled'|'Suspended'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Status** *(string) --* 
              The accelerate configuration of the bucket.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          Name of the bucket for which the accelerate configuration is retrieved.
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_acl(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Gets the access control policy for the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketAcl>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_acl(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                },
                'Grants': [
                    {
                        'Grantee': {
                            'DisplayName': 'string',
                            'EmailAddress': 'string',
                            'ID': 'string',
                            'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                            'URI': 'string'
                        },
                        'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Owner** *(dict) --* 
              - **DisplayName** *(string) --* 
              - **ID** *(string) --* 
            - **Grants** *(list) --* 
              A list of grants.
              - *(dict) --* 
                - **Grantee** *(dict) --* 
                  - **DisplayName** *(string) --* 
                    Screen name of the grantee.
                  - **EmailAddress** *(string) --* 
                    Email address of the grantee.
                  - **ID** *(string) --* 
                    The canonical user ID of the grantee.
                  - **Type** *(string) --* 
                    Type of grantee
                  - **URI** *(string) --* 
                    URI of the grantee group.
                - **Permission** *(string) --* 
                  Specifies the permission given to the grantee.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_analytics_configuration(
        self,
        Bucket,  # type: str
        Id,  # type: str
    ):
        # type: (...) -> Dict
        """
        Gets an analytics configuration for the bucket (specified by the analytics configuration ID).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketAnalyticsConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_analytics_configuration(
              Bucket='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {
                'AnalyticsConfiguration': {
                    'Id': 'string',
                    'Filter': {
                        'Prefix': 'string',
                        'Tag': {
                            'Key': 'string',
                            'Value': 'string'
                        },
                        'And': {
                            'Prefix': 'string',
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        }
                    },
                    'StorageClassAnalysis': {
                        'DataExport': {
                            'OutputSchemaVersion': 'V_1',
                            'Destination': {
                                'S3BucketDestination': {
                                    'Format': 'CSV',
                                    'BucketAccountId': 'string',
                                    'Bucket': 'string',
                                    'Prefix': 'string'
                                }
                            }
                        }
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AnalyticsConfiguration** *(dict) --* 
              The configuration and any analyses for the analytics filter.
              - **Id** *(string) --* 
                The ID that identifies the analytics configuration.
              - **Filter** *(dict) --* 
                The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.
                - **Prefix** *(string) --* 
                  The prefix to use when evaluating an analytics filter.
                - **Tag** *(dict) --* 
                  The tag to use when evaluating an analytics filter.
                  - **Key** *(string) --* 
                    Name of the tag.
                  - **Value** *(string) --* 
                    Value of the tag.
                - **And** *(dict) --* 
                  A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.
                  - **Prefix** *(string) --* 
                    The prefix to use when evaluating an AND predicate: The prefix that an object must have to be included in the metrics results.
                  - **Tags** *(list) --* 
                    The list of tags to use when evaluating an AND predicate.
                    - *(dict) --* 
                      - **Key** *(string) --* 
                        Name of the tag.
                      - **Value** *(string) --* 
                        Value of the tag.
              - **StorageClassAnalysis** *(dict) --* 
                Contains data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes. 
                - **DataExport** *(dict) --* 
                  Specifies how data related to the storage class analysis for an Amazon S3 bucket should be exported.
                  - **OutputSchemaVersion** *(string) --* 
                    The version of the output schema to use when exporting data. Must be ``V_1`` .
                  - **Destination** *(dict) --* 
                    The place to store the data for an analysis.
                    - **S3BucketDestination** *(dict) --* 
                      A destination signifying output to an S3 bucket.
                      - **Format** *(string) --* 
                        Specifies the file format used when exporting data to Amazon S3.
                      - **BucketAccountId** *(string) --* 
                        The account ID that owns the destination bucket. If no account ID is provided, the owner will not be validated prior to exporting data.
                      - **Bucket** *(string) --* 
                        The Amazon Resource Name (ARN) of the bucket to which data is exported.
                      - **Prefix** *(string) --* 
                        The prefix to use when exporting data. The prefix is prepended to all results.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket from which an analytics configuration is retrieved.
        :type Id: string
        :param Id: **[REQUIRED]**
          The ID that identifies the analytics configuration.
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_cors(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the CORS configuration for the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketCors>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_cors(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'CORSRules': [
                    {
                        'AllowedHeaders': [
                            'string',
                        ],
                        'AllowedMethods': [
                            'string',
                        ],
                        'AllowedOrigins': [
                            'string',
                        ],
                        'ExposeHeaders': [
                            'string',
                        ],
                        'MaxAgeSeconds': 123
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CORSRules** *(list) --* 
              - *(dict) --* 
                Specifies a cross-origin access rule for an Amazon S3 bucket.
                - **AllowedHeaders** *(list) --* 
                  Headers that are specified in the ``Access-Control-Request-Headers`` header. These headers are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request, Amazon S3 returns any requested headers that are allowed.
                  - *(string) --* 
                - **AllowedMethods** *(list) --* 
                  An HTTP method that you allow the origin to execute. Valid values are ``GET`` , ``PUT`` , ``HEAD`` , ``POST`` , and ``DELETE`` .
                  - *(string) --* 
                - **AllowedOrigins** *(list) --* 
                  One or more origins you want customers to be able to access the bucket from.
                  - *(string) --* 
                - **ExposeHeaders** *(list) --* 
                  One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object).
                  - *(string) --* 
                - **MaxAgeSeconds** *(integer) --* 
                  The time in seconds that your browser is to cache the preflight response for the specified resource.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_encryption(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the server-side encryption configuration of a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketEncryption>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_encryption(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'ServerSideEncryptionConfiguration': {
                    'Rules': [
                        {
                            'ApplyServerSideEncryptionByDefault': {
                                'SSEAlgorithm': 'AES256'|'aws:kms',
                                'KMSMasterKeyID': 'string'
                            }
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServerSideEncryptionConfiguration** *(dict) --* 
              - **Rules** *(list) --* 
                Container for information about a particular server-side encryption configuration rule.
                - *(dict) --* 
                  Specifies the default server-side encryption configuration.
                  - **ApplyServerSideEncryptionByDefault** *(dict) --* 
                    Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn't specify any server-side encryption, this default encryption will be applied.
                    - **SSEAlgorithm** *(string) --* 
                      Server-side encryption algorithm to use for the default encryption.
                    - **KMSMasterKeyID** *(string) --* 
                      KMS master key ID to use for the default encryption. This parameter is allowed if and only if ``SSEAlgorithm`` is set to ``aws:kms`` .
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket from which the server-side encryption configuration is retrieved.
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_inventory_configuration(
        self,
        Bucket,  # type: str
        Id,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns an inventory configuration (identified by the inventory ID) from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketInventoryConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_inventory_configuration(
              Bucket='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {
                'InventoryConfiguration': {
                    'Destination': {
                        'S3BucketDestination': {
                            'AccountId': 'string',
                            'Bucket': 'string',
                            'Format': 'CSV'|'ORC'|'Parquet',
                            'Prefix': 'string',
                            'Encryption': {
                                'SSES3': {},
                                'SSEKMS': {
                                    'KeyId': 'string'
                                }
                            }
                        }
                    },
                    'IsEnabled': True|False,
                    'Filter': {
                        'Prefix': 'string'
                    },
                    'Id': 'string',
                    'IncludedObjectVersions': 'All'|'Current',
                    'OptionalFields': [
                        'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'|'ObjectLockMode'|'ObjectLockLegalHoldStatus',
                    ],
                    'Schedule': {
                        'Frequency': 'Daily'|'Weekly'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InventoryConfiguration** *(dict) --* 
              Specifies the inventory configuration.
              - **Destination** *(dict) --* 
                Contains information about where to publish the inventory results.
                - **S3BucketDestination** *(dict) --* 
                  Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.
                  - **AccountId** *(string) --* 
                    The ID of the account that owns the destination bucket.
                  - **Bucket** *(string) --* 
                    The Amazon resource name (ARN) of the bucket where inventory results will be published.
                  - **Format** *(string) --* 
                    Specifies the output format of the inventory results.
                  - **Prefix** *(string) --* 
                    The prefix that is prepended to all inventory results.
                  - **Encryption** *(dict) --* 
                    Contains the type of server-side encryption used to encrypt the inventory results.
                    - **SSES3** *(dict) --* 
                      Specifies the use of SSE-S3 to encrypt delivered Inventory reports.
                    - **SSEKMS** *(dict) --* 
                      Specifies the use of SSE-KMS to encrypt delivered Inventory reports.
                      - **KeyId** *(string) --* 
                        Specifies the ID of the AWS Key Management Service (KMS) master encryption key to use for encrypting Inventory reports.
              - **IsEnabled** *(boolean) --* 
                Specifies whether the inventory is enabled or disabled. If set to ``True`` , an inventory list is generated. If set to ``False`` , no inventory list is generated.
              - **Filter** *(dict) --* 
                Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria.
                - **Prefix** *(string) --* 
                  The prefix that an object must have to be included in the inventory results.
              - **Id** *(string) --* 
                The ID used to identify the inventory configuration.
              - **IncludedObjectVersions** *(string) --* 
                Object versions to include in the inventory list. If set to ``All`` , the list includes all the object versions, which adds the version-related fields ``VersionId`` , ``IsLatest`` , and ``DeleteMarker`` to the list. If set to ``Current`` , the list does not contain these version-related fields.
              - **OptionalFields** *(list) --* 
                Contains the optional fields that are included in the inventory results.
                - *(string) --* 
              - **Schedule** *(dict) --* 
                Specifies the schedule for generating inventory results.
                - **Frequency** *(string) --* 
                  Specifies how frequently inventory results are produced.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket containing the inventory configuration to retrieve.
        :type Id: string
        :param Id: **[REQUIRED]**
          The ID used to identify the inventory configuration.
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_lifecycle(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        No longer used, see the GetBucketLifecycleConfiguration operation.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketLifecycle>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_lifecycle(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'Rules': [
                    {
                        'Expiration': {
                            'Date': datetime(2015, 1, 1),
                            'Days': 123,
                            'ExpiredObjectDeleteMarker': True|False
                        },
                        'ID': 'string',
                        'Prefix': 'string',
                        'Status': 'Enabled'|'Disabled',
                        'Transition': {
                            'Date': datetime(2015, 1, 1),
                            'Days': 123,
                            'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                        },
                        'NoncurrentVersionTransition': {
                            'NoncurrentDays': 123,
                            'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                        },
                        'NoncurrentVersionExpiration': {
                            'NoncurrentDays': 123
                        },
                        'AbortIncompleteMultipartUpload': {
                            'DaysAfterInitiation': 123
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Rules** *(list) --* 
              - *(dict) --* 
                Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__ in the *Amazon Simple Storage Service API Reference* .
                - **Expiration** *(dict) --* 
                  - **Date** *(datetime) --* 
                    Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
                  - **Days** *(integer) --* 
                    Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
                  - **ExpiredObjectDeleteMarker** *(boolean) --* 
                    Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
                - **ID** *(string) --* 
                  Unique identifier for the rule. The value can't be longer than 255 characters.
                - **Prefix** *(string) --* 
                  Object key prefix that identifies one or more objects to which this rule applies.
                - **Status** *(string) --* 
                  If ``Enabled`` , the rule is currently being applied. If ``Disabled`` , the rule is not currently being applied.
                - **Transition** *(dict) --* 
                  - **Date** *(datetime) --* 
                    Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.
                  - **Days** *(integer) --* 
                    Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.
                  - **StorageClass** *(string) --* 
                    The storage class to which you want the object to transition.
                - **NoncurrentVersionTransition** *(dict) --* 
                  - **NoncurrentDays** *(integer) --* 
                    Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                  - **StorageClass** *(string) --* 
                    The class of storage used to store the object.
                - **NoncurrentVersionExpiration** *(dict) --* 
                  - **NoncurrentDays** *(integer) --* 
                    Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__ in the Amazon Simple Storage Service Developer Guide.
                - **AbortIncompleteMultipartUpload** *(dict) --* 
                  - **DaysAfterInitiation** *(integer) --* 
                    Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_lifecycle_configuration(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the lifecycle configuration information set on the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketLifecycleConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_lifecycle_configuration(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'Rules': [
                    {
                        'Expiration': {
                            'Date': datetime(2015, 1, 1),
                            'Days': 123,
                            'ExpiredObjectDeleteMarker': True|False
                        },
                        'ID': 'string',
                        'Prefix': 'string',
                        'Filter': {
                            'Prefix': 'string',
                            'Tag': {
                                'Key': 'string',
                                'Value': 'string'
                            },
                            'And': {
                                'Prefix': 'string',
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        },
                        'Status': 'Enabled'|'Disabled',
                        'Transitions': [
                            {
                                'Date': datetime(2015, 1, 1),
                                'Days': 123,
                                'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                            },
                        ],
                        'NoncurrentVersionTransitions': [
                            {
                                'NoncurrentDays': 123,
                                'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                            },
                        ],
                        'NoncurrentVersionExpiration': {
                            'NoncurrentDays': 123
                        },
                        'AbortIncompleteMultipartUpload': {
                            'DaysAfterInitiation': 123
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Rules** *(list) --* 
              - *(dict) --* 
                - **Expiration** *(dict) --* 
                  - **Date** *(datetime) --* 
                    Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
                  - **Days** *(integer) --* 
                    Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
                  - **ExpiredObjectDeleteMarker** *(boolean) --* 
                    Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
                - **ID** *(string) --* 
                  Unique identifier for the rule. The value cannot be longer than 255 characters.
                - **Prefix** *(string) --* 
                  Prefix identifying one or more objects to which the rule applies. This is No longer used; use Filter instead.
                - **Filter** *(dict) --* 
                  - **Prefix** *(string) --* 
                    Prefix identifying one or more objects to which the rule applies.
                  - **Tag** *(dict) --* 
                    This tag must exist in the object's tag set in order for the rule to apply.
                    - **Key** *(string) --* 
                      Name of the tag.
                    - **Value** *(string) --* 
                      Value of the tag.
                  - **And** *(dict) --* 
                    - **Prefix** *(string) --* 
                    - **Tags** *(list) --* 
                      All of these tags must exist in the object's tag set in order for the rule to apply.
                      - *(dict) --* 
                        - **Key** *(string) --* 
                          Name of the tag.
                        - **Value** *(string) --* 
                          Value of the tag.
                - **Status** *(string) --* 
                  If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being applied.
                - **Transitions** *(list) --* 
                  - *(dict) --* 
                    Specifies when an object transitions to a specified storage class.
                    - **Date** *(datetime) --* 
                      Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.
                    - **Days** *(integer) --* 
                      Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.
                    - **StorageClass** *(string) --* 
                      The storage class to which you want the object to transition.
                - **NoncurrentVersionTransitions** *(list) --* 
                  - *(dict) --* 
                    Container for the transition rule that describes when noncurrent objects transition to the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` , ``GLACIER`` , or ``DEEP_ARCHIVE`` storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` , ``GLACIER`` , or ``DEEP_ARCHIVE`` storage class at a specific period in the object's lifetime.
                    - **NoncurrentDays** *(integer) --* 
                      Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                    - **StorageClass** *(string) --* 
                      The class of storage used to store the object.
                - **NoncurrentVersionExpiration** *(dict) --* 
                  - **NoncurrentDays** *(integer) --* 
                    Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__ in the Amazon Simple Storage Service Developer Guide.
                - **AbortIncompleteMultipartUpload** *(dict) --* 
                  - **DaysAfterInitiation** *(integer) --* 
                    Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_location(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the region the bucket resides in.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketLocation>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_location(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'LocationConstraint': 'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LocationConstraint** *(string) --* 
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_logging(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the logging status of a bucket and the permissions users have to view and modify that status. To use GET, you must be the bucket owner.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketLogging>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_logging(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'LoggingEnabled': {
                    'TargetBucket': 'string',
                    'TargetGrants': [
                        {
                            'Grantee': {
                                'DisplayName': 'string',
                                'EmailAddress': 'string',
                                'ID': 'string',
                                'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                                'URI': 'string'
                            },
                            'Permission': 'FULL_CONTROL'|'READ'|'WRITE'
                        },
                    ],
                    'TargetPrefix': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LoggingEnabled** *(dict) --* 
              - **TargetBucket** *(string) --* 
                Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case you should choose a different TargetPrefix for each source bucket so that the delivered log files can be distinguished by key.
              - **TargetGrants** *(list) --* 
                - *(dict) --* 
                  - **Grantee** *(dict) --* 
                    - **DisplayName** *(string) --* 
                      Screen name of the grantee.
                    - **EmailAddress** *(string) --* 
                      Email address of the grantee.
                    - **ID** *(string) --* 
                      The canonical user ID of the grantee.
                    - **Type** *(string) --* 
                      Type of grantee
                    - **URI** *(string) --* 
                      URI of the grantee group.
                  - **Permission** *(string) --* 
                    Logging permissions assigned to the Grantee for the bucket.
              - **TargetPrefix** *(string) --* 
                A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_metrics_configuration(
        self,
        Bucket,  # type: str
        Id,  # type: str
    ):
        # type: (...) -> Dict
        """
        Gets a metrics configuration (specified by the metrics configuration ID) from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketMetricsConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_metrics_configuration(
              Bucket='string',
              Id='string'
          )
        
        **Response Syntax**
        ::
            {
                'MetricsConfiguration': {
                    'Id': 'string',
                    'Filter': {
                        'Prefix': 'string',
                        'Tag': {
                            'Key': 'string',
                            'Value': 'string'
                        },
                        'And': {
                            'Prefix': 'string',
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        }
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **MetricsConfiguration** *(dict) --* 
              Specifies the metrics configuration.
              - **Id** *(string) --* 
                The ID used to identify the metrics configuration.
              - **Filter** *(dict) --* 
                Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter's criteria. A filter must be a prefix, a tag, or a conjunction (MetricsAndOperator).
                - **Prefix** *(string) --* 
                  The prefix used when evaluating a metrics filter.
                - **Tag** *(dict) --* 
                  The tag used when evaluating a metrics filter.
                  - **Key** *(string) --* 
                    Name of the tag.
                  - **Value** *(string) --* 
                    Value of the tag.
                - **And** *(dict) --* 
                  A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.
                  - **Prefix** *(string) --* 
                    The prefix used when evaluating an AND predicate.
                  - **Tags** *(list) --* 
                    The list of tags used when evaluating an AND predicate.
                    - *(dict) --* 
                      - **Key** *(string) --* 
                        Name of the tag.
                      - **Value** *(string) --* 
                        Value of the tag.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket containing the metrics configuration to retrieve.
        :type Id: string
        :param Id: **[REQUIRED]**
          The ID used to identify the metrics configuration.
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_notification(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        No longer used, see the GetBucketNotificationConfiguration operation.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketNotification>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_notification(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'TopicConfiguration': {
                    'Id': 'string',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    ],
                    'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    'Topic': 'string'
                },
                'QueueConfiguration': {
                    'Id': 'string',
                    'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    ],
                    'Queue': 'string'
                },
                'CloudFunctionConfiguration': {
                    'Id': 'string',
                    'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    ],
                    'CloudFunction': 'string',
                    'InvocationRole': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TopicConfiguration** *(dict) --* 
              - **Id** *(string) --* 
                An optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
              - **Events** *(list) --* 
                - *(string) --* 
                  The bucket event for which to send notifications.
              - **Event** *(string) --* 
                Bucket event for which to send notifications.
              - **Topic** *(string) --* 
                Amazon SNS topic to which Amazon S3 will publish a message to report the specified events for the bucket.
            - **QueueConfiguration** *(dict) --* 
              - **Id** *(string) --* 
                An optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
              - **Event** *(string) --* 
                The bucket event for which to send notifications.
              - **Events** *(list) --* 
                - *(string) --* 
                  The bucket event for which to send notifications.
              - **Queue** *(string) --* 
            - **CloudFunctionConfiguration** *(dict) --* 
              - **Id** *(string) --* 
                An optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
              - **Event** *(string) --* 
                The bucket event for which to send notifications.
              - **Events** *(list) --* 
                - *(string) --* 
                  The bucket event for which to send notifications.
              - **CloudFunction** *(string) --* 
              - **InvocationRole** *(string) --* 
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          Name of the bucket to get the notification configuration for.
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_notification_configuration(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the notification configuration of a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketNotificationConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_notification_configuration(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'TopicConfigurations': [
                    {
                        'Id': 'string',
                        'TopicArn': 'string',
                        'Events': [
                            's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                        ],
                        'Filter': {
                            'Key': {
                                'FilterRules': [
                                    {
                                        'Name': 'prefix'|'suffix',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ],
                'QueueConfigurations': [
                    {
                        'Id': 'string',
                        'QueueArn': 'string',
                        'Events': [
                            's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                        ],
                        'Filter': {
                            'Key': {
                                'FilterRules': [
                                    {
                                        'Name': 'prefix'|'suffix',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ],
                'LambdaFunctionConfigurations': [
                    {
                        'Id': 'string',
                        'LambdaFunctionArn': 'string',
                        'Events': [
                            's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                        ],
                        'Filter': {
                            'Key': {
                                'FilterRules': [
                                    {
                                        'Name': 'prefix'|'suffix',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            A container for specifying the notification configuration of the bucket. If this element is empty, notifications are turned off for the bucket.
            - **TopicConfigurations** *(list) --* 
              The topic to which notifications are sent and the events for which notifications are generated.
              - *(dict) --* 
                A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
                - **Id** *(string) --* 
                  An optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
                - **TopicArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a message when it detects events of the specified type.
                - **Events** *(list) --* 
                  The Amazon S3 bucket event about which to send notifications. For more information, see `Supported Event Types <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                  - *(string) --* 
                    The bucket event for which to send notifications.
                - **Filter** *(dict) --* 
                  - **Key** *(dict) --* 
                    - **FilterRules** *(list) --* 
                      - *(dict) --* 
                        Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.
                        - **Name** *(string) --* 
                          The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see `Configuring Event Notifications <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                        - **Value** *(string) --* 
                          The value that the filter searches for in object key names.
            - **QueueConfigurations** *(list) --* 
              The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.
              - *(dict) --* 
                Specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.
                - **Id** *(string) --* 
                  An optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
                - **QueueArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.
                - **Events** *(list) --* 
                  - *(string) --* 
                    The bucket event for which to send notifications.
                - **Filter** *(dict) --* 
                  - **Key** *(dict) --* 
                    - **FilterRules** *(list) --* 
                      - *(dict) --* 
                        Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.
                        - **Name** *(string) --* 
                          The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see `Configuring Event Notifications <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                        - **Value** *(string) --* 
                          The value that the filter searches for in object key names.
            - **LambdaFunctionConfigurations** *(list) --* 
              Describes the AWS Lambda functions to invoke and the events for which to invoke them.
              - *(dict) --* 
                A container for specifying the configuration for AWS Lambda notifications.
                - **Id** *(string) --* 
                  An optional unique identifier for configurations in a notification configuration. If you don't provide one, Amazon S3 will assign an ID.
                - **LambdaFunctionArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the AWS Lambda function that Amazon S3 invokes when the specified event type occurs.
                - **Events** *(list) --* 
                  The Amazon S3 bucket event for which to invoke the AWS Lambda function. For more information, see `Supported Event Types <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                  - *(string) --* 
                    The bucket event for which to send notifications.
                - **Filter** *(dict) --* 
                  - **Key** *(dict) --* 
                    - **FilterRules** *(list) --* 
                      - *(dict) --* 
                        Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.
                        - **Name** *(string) --* 
                          The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see `Configuring Event Notifications <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                        - **Value** *(string) --* 
                          The value that the filter searches for in object key names.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          Name of the bucket to get the notification configuration for.
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_policy(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the policy of a specified bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketPolicy>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_policy(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'Policy': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Policy** *(string) --* 
              The bucket policy as a JSON document.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_policy_status(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Retrieves the policy status for an Amazon S3 bucket, indicating whether the bucket is public.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketPolicyStatus>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_policy_status(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'PolicyStatus': {
                    'IsPublic': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PolicyStatus** *(dict) --* 
              The policy status for the specified bucket.
              - **IsPublic** *(boolean) --* 
                The policy status for this bucket. ``TRUE`` indicates that this bucket is public. ``FALSE`` indicates that the bucket is not public.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the Amazon S3 bucket whose policy status you want to retrieve.
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_replication(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the replication configuration of a bucket.
        .. note::
          It can take a while to propagate the put or delete a replication configuration to all Amazon S3 systems. Therefore, a get request soon after put or delete can return a wrong result. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketReplication>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_replication(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'ReplicationConfiguration': {
                    'Role': 'string',
                    'Rules': [
                        {
                            'ID': 'string',
                            'Priority': 123,
                            'Prefix': 'string',
                            'Filter': {
                                'Prefix': 'string',
                                'Tag': {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                                'And': {
                                    'Prefix': 'string',
                                    'Tags': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                }
                            },
                            'Status': 'Enabled'|'Disabled',
                            'SourceSelectionCriteria': {
                                'SseKmsEncryptedObjects': {
                                    'Status': 'Enabled'|'Disabled'
                                }
                            },
                            'Destination': {
                                'Bucket': 'string',
                                'Account': 'string',
                                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                                'AccessControlTranslation': {
                                    'Owner': 'Destination'
                                },
                                'EncryptionConfiguration': {
                                    'ReplicaKmsKeyID': 'string'
                                }
                            },
                            'DeleteMarkerReplication': {
                                'Status': 'Enabled'|'Disabled'
                            }
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ReplicationConfiguration** *(dict) --* 
              - **Role** *(string) --* 
                The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon S3 assumes when replicating objects. For more information, see `How to Set Up Cross-Region Replication <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-how-setup.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
              - **Rules** *(list) --* 
                A container for one or more replication rules. A replication configuration must have at least one rule and can contain a maximum of 1,000 rules. 
                - *(dict) --* 
                  Specifies which Amazon S3 objects to replicate and where to store the replicas.
                  - **ID** *(string) --* 
                    A unique identifier for the rule. The maximum value is 255 characters.
                  - **Priority** *(integer) --* 
                    The priority associated with the rule. If you specify multiple rules in a replication configuration, Amazon S3 prioritizes the rules to prevent conflicts when filtering. If two or more rules identify the same object based on a specified filter, the rule with higher priority takes precedence. For example:
                    * Same object quality prefix based filter criteria If prefixes you specified in multiple rules overlap  
                    * Same object qualify tag based filter criteria specified in multiple rules 
                    For more information, see `Cross-Region Replication (CRR) <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html>`__ in the *Amazon S3 Developer Guide* .
                  - **Prefix** *(string) --* 
                    An object keyname prefix that identifies the object or objects to which the rule applies. The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string. 
                  - **Filter** *(dict) --* 
                    - **Prefix** *(string) --* 
                      An object keyname prefix that identifies the subset of objects to which the rule applies.
                    - **Tag** *(dict) --* 
                      A container for specifying a tag key and value. 
                      The rule applies only to objects that have the tag in their tag set.
                      - **Key** *(string) --* 
                        Name of the tag.
                      - **Value** *(string) --* 
                        Value of the tag.
                    - **And** *(dict) --* 
                      A container for specifying rule filters. The filters determine the subset of objects to which the rule applies. This element is required only if you specify more than one filter. For example: 
                      * If you specify both a ``Prefix`` and a ``Tag`` filter, wrap these filters in an ``And`` tag. 
                      * If you specify a filter based on multiple tags, wrap the ``Tag`` elements in an ``And`` tag. 
                      - **Prefix** *(string) --* 
                      - **Tags** *(list) --* 
                        - *(dict) --* 
                          - **Key** *(string) --* 
                            Name of the tag.
                          - **Value** *(string) --* 
                            Value of the tag.
                  - **Status** *(string) --* 
                    Specifies whether the rule is enabled.
                  - **SourceSelectionCriteria** *(dict) --* 
                    A container that describes additional filters for identifying the source objects that you want to replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3 supports only the filter that you can specify for objects created with server-side encryption using an AWS KMS-Managed Key (SSE-KMS).
                    - **SseKmsEncryptedObjects** *(dict) --* 
                      A container for filter information for the selection of Amazon S3 objects encrypted with AWS KMS. If you include ``SourceSelectionCriteria`` in the replication configuration, this element is required. 
                      - **Status** *(string) --* 
                        Specifies whether Amazon S3 replicates objects created with server-side encryption using an AWS KMS-managed key.
                  - **Destination** *(dict) --* 
                    A container for information about the replication destination.
                    - **Bucket** *(string) --* 
                      The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store replicas of the object identified by the rule.
                      A replication configuration can replicate objects to only one destination bucket. If there are multiple rules in your replication configuration, all rules must specify the same destination bucket.
                    - **Account** *(string) --* 
                      Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3 to change replica ownership to the AWS account that owns the destination bucket by specifying the ``AccessControlTranslation`` property, this is the account ID of the destination bucket owner. For more information, see `Cross-Region Replication Additional Configuration\: Change Replica Owner <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-change-owner.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                    - **StorageClass** *(string) --* 
                      The storage class to use when replicating objects, such as standard or reduced redundancy. By default, Amazon S3 uses the storage class of the source object to create the object replica. 
                      For valid values, see the ``StorageClass`` element of the `PUT Bucket replication <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__ action in the *Amazon Simple Storage Service API Reference* .
                    - **AccessControlTranslation** *(dict) --* 
                      Specify this only in a cross-account scenario (where source and destination bucket owners are not the same), and you want to change replica ownership to the AWS account that owns the destination bucket. If this is not specified in the replication configuration, the replicas are owned by same AWS account that owns the source object.
                      - **Owner** *(string) --* 
                        Specifies the replica ownership. For default and valid values, see `PUT bucket replication <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__ in the *Amazon Simple Storage Service API Reference* .
                    - **EncryptionConfiguration** *(dict) --* 
                      A container that provides information about encryption. If ``SourceSelectionCriteria`` is specified, you must specify this element.
                      - **ReplicaKmsKeyID** *(string) --* 
                        Specifies the AWS KMS Key ID (Key ARN or Alias ARN) for the destination bucket. Amazon S3 uses this key to encrypt replica objects.
                  - **DeleteMarkerReplication** *(dict) --* 
                    - **Status** *(string) --* 
                      The status of the delete marker replication.
                      .. note::
                        In the current implementation, Amazon S3 doesn't replicate the delete markers. The status must be ``Disabled`` . 
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_request_payment(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the request payment configuration of a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketRequestPayment>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_request_payment(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'Payer': 'Requester'|'BucketOwner'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Payer** *(string) --* 
              Specifies who pays for the download and request fees.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_tagging(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the tag set associated with the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketTagging>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_tagging(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'TagSet': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TagSet** *(list) --* 
              - *(dict) --* 
                - **Key** *(string) --* 
                  Name of the tag.
                - **Value** *(string) --* 
                  Value of the tag.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_versioning(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the versioning state of a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketVersioning>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_versioning(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'Status': 'Enabled'|'Suspended',
                'MFADelete': 'Enabled'|'Disabled'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Status** *(string) --* 
              The versioning state of the bucket.
            - **MFADelete** *(string) --* 
              Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_bucket_website(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Returns the website configuration for a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketWebsite>`_
        
        **Request Syntax**
        ::
          response = client.get_bucket_website(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'RedirectAllRequestsTo': {
                    'HostName': 'string',
                    'Protocol': 'http'|'https'
                },
                'IndexDocument': {
                    'Suffix': 'string'
                },
                'ErrorDocument': {
                    'Key': 'string'
                },
                'RoutingRules': [
                    {
                        'Condition': {
                            'HttpErrorCodeReturnedEquals': 'string',
                            'KeyPrefixEquals': 'string'
                        },
                        'Redirect': {
                            'HostName': 'string',
                            'HttpRedirectCode': 'string',
                            'Protocol': 'http'|'https',
                            'ReplaceKeyPrefixWith': 'string',
                            'ReplaceKeyWith': 'string'
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RedirectAllRequestsTo** *(dict) --* 
              - **HostName** *(string) --* 
                Name of the host where requests are redirected.
              - **Protocol** *(string) --* 
                Protocol to use when redirecting requests. The default is the protocol that is used in the original request.
            - **IndexDocument** *(dict) --* 
              - **Suffix** *(string) --* 
                A suffix that is appended to a request that is for a directory on the website endpoint (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html) The suffix must not be empty and must not include a slash character.
            - **ErrorDocument** *(dict) --* 
              - **Key** *(string) --* 
                The object key name to use when a 4XX class error occurs.
            - **RoutingRules** *(list) --* 
              - *(dict) --* 
                Specifies the redirect behavior and when a redirect is applied.
                - **Condition** *(dict) --* 
                  A container for describing a condition that must be met for the specified redirect to apply. For example, 1. If request is for pages in the ``/docs`` folder, redirect to the ``/documents`` folder. 2. If request results in HTTP error 4xx, redirect request to another host where you might process the error.
                  - **HttpErrorCodeReturnedEquals** *(string) --* 
                    The HTTP error code when the redirect is applied. In the event of an error, if the error code equals this value, then the specified redirect is applied. Required when parent element ``Condition`` is specified and sibling ``KeyPrefixEquals`` is not specified. If both are specified, then both must be true for the redirect to be applied.
                  - **KeyPrefixEquals** *(string) --* 
                    The object key name prefix when the redirect is applied. For example, to redirect requests for ``ExamplePage.html`` , the key prefix will be ``ExamplePage.html`` . To redirect request for all pages with the prefix ``docs/`` , the key prefix will be ``/docs`` , which identifies all objects in the docs/ folder. Required when the parent element ``Condition`` is specified and sibling ``HttpErrorCodeReturnedEquals`` is not specified. If both conditions are specified, both must be true for the redirect to be applied.
                - **Redirect** *(dict) --* 
                  Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can specify a different error code to return.
                  - **HostName** *(string) --* 
                    The host name to use in the redirect request.
                  - **HttpRedirectCode** *(string) --* 
                    The HTTP redirect code to use on the response. Not required if one of the siblings is present.
                  - **Protocol** *(string) --* 
                    Protocol to use when redirecting requests. The default is the protocol that is used in the original request.
                  - **ReplaceKeyPrefixWith** *(string) --* 
                    The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix ``docs/`` (objects in the ``docs/`` folder) to ``documents/`` , you can set a condition block with ``KeyPrefixEquals`` set to ``docs/`` and in the Redirect set ``ReplaceKeyPrefixWith`` to ``/documents`` . Not required if one of the siblings is present. Can be present only if ``ReplaceKeyWith`` is not provided.
                  - **ReplaceKeyWith** *(string) --* 
                    The specific object key to use in the redirect request. For example, redirect request to ``error.html`` . Not required if one of the siblings is present. Can be present only if ``ReplaceKeyPrefixWith`` is not provided.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :rtype: dict
        :returns:
        """
        pass

    def get_object(
        self,
        Bucket,  # type: str
        Key,  # type: str
        IfMatch=None,  # type: Optional[str]
        IfModifiedSince=None,  # type: Optional[datetime]
        IfNoneMatch=None,  # type: Optional[str]
        IfUnmodifiedSince=None,  # type: Optional[datetime]
        Range=None,  # type: Optional[str]
        ResponseCacheControl=None,  # type: Optional[str]
        ResponseContentDisposition=None,  # type: Optional[str]
        ResponseContentEncoding=None,  # type: Optional[str]
        ResponseContentLanguage=None,  # type: Optional[str]
        ResponseContentType=None,  # type: Optional[str]
        ResponseExpires=None,  # type: Optional[datetime]
        VersionId=None,  # type: Optional[str]
        SSECustomerAlgorithm=None,  # type: Optional[str]
        SSECustomerKey=None,  # type: Optional[str]
        SSECustomerKeyMD5=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
        PartNumber=None,  # type: Optional[int]
    ):
        # type: (...) -> Dict
        """
        Retrieves objects from Amazon S3.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObject>`_
        
        **Request Syntax**
        ::
          response = client.get_object(
              Bucket='string',
              IfMatch='string',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch='string',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Key='string',
              Range='string',
              ResponseCacheControl='string',
              ResponseContentDisposition='string',
              ResponseContentEncoding='string',
              ResponseContentLanguage='string',
              ResponseContentType='string',
              ResponseExpires=datetime(2015, 1, 1),
              VersionId='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              RequestPayer='requester',
              PartNumber=123
          )
        
        **Response Syntax**
        ::
            {
                'Body': StreamingBody(),
                'DeleteMarker': True|False,
                'AcceptRanges': 'string',
                'Expiration': 'string',
                'Restore': 'string',
                'LastModified': datetime(2015, 1, 1),
                'ContentLength': 123,
                'ETag': 'string',
                'MissingMeta': 123,
                'VersionId': 'string',
                'CacheControl': 'string',
                'ContentDisposition': 'string',
                'ContentEncoding': 'string',
                'ContentLanguage': 'string',
                'ContentRange': 'string',
                'ContentType': 'string',
                'Expires': datetime(2015, 1, 1),
                'WebsiteRedirectLocation': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'Metadata': {
                    'string': 'string'
                },
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                'RequestCharged': 'requester',
                'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
                'PartsCount': 123,
                'TagCount': 123,
                'ObjectLockMode': 'GOVERNANCE'|'COMPLIANCE',
                'ObjectLockRetainUntilDate': datetime(2015, 1, 1),
                'ObjectLockLegalHoldStatus': 'ON'|'OFF'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Body** (:class:`.StreamingBody`) -- 
              Object data.
            - **DeleteMarker** *(boolean) --* 
              Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.
            - **AcceptRanges** *(string) --* 
            - **Expiration** *(string) --* 
              If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
            - **Restore** *(string) --* 
              Provides information about object restoration operation and expiration time of the restored object copy.
            - **LastModified** *(datetime) --* 
              Last modified date of the object
            - **ContentLength** *(integer) --* 
              Size of the body in bytes.
            - **ETag** *(string) --* 
              An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL
            - **MissingMeta** *(integer) --* 
              This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.
            - **VersionId** *(string) --* 
              Version of the object.
            - **CacheControl** *(string) --* 
              Specifies caching behavior along the request/reply chain.
            - **ContentDisposition** *(string) --* 
              Specifies presentational information for the object.
            - **ContentEncoding** *(string) --* 
              Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
            - **ContentLanguage** *(string) --* 
              The language the content is in.
            - **ContentRange** *(string) --* 
              The portion of the object returned in the response.
            - **ContentType** *(string) --* 
              A standard MIME type describing the format of the object data.
            - **Expires** *(datetime) --* 
              The date and time at which the object is no longer cacheable.
            - **WebsiteRedirectLocation** *(string) --* 
              If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
            - **ServerSideEncryption** *(string) --* 
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
            - **Metadata** *(dict) --* 
              A map of metadata to store with the object in S3.
              - *(string) --* 
                - *(string) --* 
            - **SSECustomerAlgorithm** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
            - **SSECustomerKeyMD5** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
            - **SSEKMSKeyId** *(string) --* 
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
            - **StorageClass** *(string) --* 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
            - **ReplicationStatus** *(string) --* 
            - **PartsCount** *(integer) --* 
              The count of parts this object has.
            - **TagCount** *(integer) --* 
              The number of tags, if any, on the object.
            - **ObjectLockMode** *(string) --* 
              The object lock mode currently in place for this object.
            - **ObjectLockRetainUntilDate** *(datetime) --* 
              The date and time when this object's object lock will expire.
            - **ObjectLockLegalHoldStatus** *(string) --* 
              Indicates whether this object has an active legal hold. This field is only returned if you have permission to view an object's legal hold status.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type IfMatch: string
        :param IfMatch:
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        :type IfModifiedSince: datetime
        :param IfModifiedSince:
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        :type IfNoneMatch: string
        :param IfNoneMatch:
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince:
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        :type Key: string
        :param Key: **[REQUIRED]**
        :type Range: string
        :param Range:
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        :type ResponseCacheControl: string
        :param ResponseCacheControl:
          Sets the Cache-Control header of the response.
        :type ResponseContentDisposition: string
        :param ResponseContentDisposition:
          Sets the Content-Disposition header of the response
        :type ResponseContentEncoding: string
        :param ResponseContentEncoding:
          Sets the Content-Encoding header of the response.
        :type ResponseContentLanguage: string
        :param ResponseContentLanguage:
          Sets the Content-Language header of the response.
        :type ResponseContentType: string
        :param ResponseContentType:
          Sets the Content-Type header of the response.
        :type ResponseExpires: datetime
        :param ResponseExpires:
          Sets the Expires header of the response.
        :type VersionId: string
        :param VersionId:
          VersionId used to reference a specific version of the object.
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        :type SSECustomerKey: string
        :param SSECustomerKey:
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type PartNumber: integer
        :param PartNumber:
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' GET request for the part specified. Useful for downloading just a part of an object.
        :rtype: dict
        :returns:
        """
        pass

    def get_object_acl(
        self,
        Bucket,  # type: str
        Key,  # type: str
        VersionId=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Returns the access control list (ACL) of an object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectAcl>`_
        
        **Request Syntax**
        ::
          response = client.get_object_acl(
              Bucket='string',
              Key='string',
              VersionId='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                },
                'Grants': [
                    {
                        'Grantee': {
                            'DisplayName': 'string',
                            'EmailAddress': 'string',
                            'ID': 'string',
                            'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                            'URI': 'string'
                        },
                        'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                    },
                ],
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Owner** *(dict) --* 
              - **DisplayName** *(string) --* 
              - **ID** *(string) --* 
            - **Grants** *(list) --* 
              A list of grants.
              - *(dict) --* 
                - **Grantee** *(dict) --* 
                  - **DisplayName** *(string) --* 
                    Screen name of the grantee.
                  - **EmailAddress** *(string) --* 
                    Email address of the grantee.
                  - **ID** *(string) --* 
                    The canonical user ID of the grantee.
                  - **Type** *(string) --* 
                    Type of grantee
                  - **URI** *(string) --* 
                    URI of the grantee group.
                - **Permission** *(string) --* 
                  Specifies the permission given to the grantee.
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Key: string
        :param Key: **[REQUIRED]**
        :type VersionId: string
        :param VersionId:
          VersionId used to reference a specific version of the object.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass

    def get_object_legal_hold(
        self,
        Bucket,  # type: str
        Key,  # type: str
        VersionId=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Gets an object's current Legal Hold status.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectLegalHold>`_
        
        **Request Syntax**
        ::
          response = client.get_object_legal_hold(
              Bucket='string',
              Key='string',
              VersionId='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'LegalHold': {
                    'Status': 'ON'|'OFF'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LegalHold** *(dict) --* 
              The current Legal Hold status for the specified object.
              - **Status** *(string) --* 
                Indicates whether the specified object has a Legal Hold in place.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The bucket containing the object whose Legal Hold status you want to retrieve.
        :type Key: string
        :param Key: **[REQUIRED]**
          The key name for the object whose Legal Hold status you want to retrieve.
        :type VersionId: string
        :param VersionId:
          The version ID of the object whose Legal Hold status you want to retrieve.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass

    def get_object_lock_configuration(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Gets the object lock configuration for a bucket. The rule specified in the object lock configuration will be applied by default to every new object placed in the specified bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectLockConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_object_lock_configuration(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'ObjectLockConfiguration': {
                    'ObjectLockEnabled': 'Enabled',
                    'Rule': {
                        'DefaultRetention': {
                            'Mode': 'GOVERNANCE'|'COMPLIANCE',
                            'Days': 123,
                            'Years': 123
                        }
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ObjectLockConfiguration** *(dict) --* 
              The specified bucket's object lock configuration.
              - **ObjectLockEnabled** *(string) --* 
                Indicates whether this bucket has an object lock configuration enabled.
              - **Rule** *(dict) --* 
                The object lock rule in place for the specified object.
                - **DefaultRetention** *(dict) --* 
                  The default retention period that you want to apply to new objects placed in the specified bucket.
                  - **Mode** *(string) --* 
                    The default object lock retention mode you want to apply to new objects placed in the specified bucket.
                  - **Days** *(integer) --* 
                    The number of days that you want to specify for the default retention period.
                  - **Years** *(integer) --* 
                    The number of years that you want to specify for the default retention period.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The bucket whose object lock configuration you want to retrieve.
        :rtype: dict
        :returns:
        """
        pass

    def get_object_retention(
        self,
        Bucket,  # type: str
        Key,  # type: str
        VersionId=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Retrieves an object's retention settings.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectRetention>`_
        
        **Request Syntax**
        ::
          response = client.get_object_retention(
              Bucket='string',
              Key='string',
              VersionId='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'Retention': {
                    'Mode': 'GOVERNANCE'|'COMPLIANCE',
                    'RetainUntilDate': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Retention** *(dict) --* 
              The container element for an object's retention settings.
              - **Mode** *(string) --* 
                Indicates the Retention mode for the specified object.
              - **RetainUntilDate** *(datetime) --* 
                The date on which this object lock retention expires.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The bucket containing the object whose retention settings you want to retrieve.
        :type Key: string
        :param Key: **[REQUIRED]**
          The key name for the object whose retention settings you want to retrieve.
        :type VersionId: string
        :param VersionId:
          The version ID for the object whose retention settings you want to retrieve.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass

    def get_object_tagging(
        self,
        Bucket,  # type: str
        Key,  # type: str
        VersionId=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Returns the tag-set of an object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectTagging>`_
        
        **Request Syntax**
        ::
          response = client.get_object_tagging(
              Bucket='string',
              Key='string',
              VersionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'VersionId': 'string',
                'TagSet': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VersionId** *(string) --* 
            - **TagSet** *(list) --* 
              - *(dict) --* 
                - **Key** *(string) --* 
                  Name of the tag.
                - **Value** *(string) --* 
                  Value of the tag.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Key: string
        :param Key: **[REQUIRED]**
        :type VersionId: string
        :param VersionId:
        :rtype: dict
        :returns:
        """
        pass

    def get_object_torrent(
        self,
        Bucket,  # type: str
        Key,  # type: str
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Return torrent files from a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectTorrent>`_
        
        **Request Syntax**
        ::
          response = client.get_object_torrent(
              Bucket='string',
              Key='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'Body': StreamingBody(),
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Body** (:class:`.StreamingBody`) -- 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Key: string
        :param Key: **[REQUIRED]**
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass

    def get_paginator(
        self,
        operation_name=None,  # type: Optional[str]
    ):
        # type: (...) -> Paginator
        """
        Create a paginator for an operation.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_public_access_block(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> Dict
        """
        Retrieves the ``PublicAccessBlock`` configuration for an Amazon S3 bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetPublicAccessBlock>`_
        
        **Request Syntax**
        ::
          response = client.get_public_access_block(
              Bucket='string'
          )
        
        **Response Syntax**
        ::
            {
                'PublicAccessBlockConfiguration': {
                    'BlockPublicAcls': True|False,
                    'IgnorePublicAcls': True|False,
                    'BlockPublicPolicy': True|False,
                    'RestrictPublicBuckets': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PublicAccessBlockConfiguration** *(dict) --* 
              The ``PublicAccessBlock`` configuration currently in effect for this Amazon S3 bucket.
              - **BlockPublicAcls** *(boolean) --* 
                Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and objects in this bucket. Setting this element to ``TRUE`` causes the following behavior:
                * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public. 
                * PUT Object calls fail if the request includes a public ACL. 
                Enabling this setting doesn't affect existing policies or ACLs.
              - **IgnorePublicAcls** *(boolean) --* 
                Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on this bucket and objects in this bucket.
                Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.
              - **BlockPublicPolicy** *(boolean) --* 
                Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access. 
                Enabling this setting doesn't affect existing bucket policies.
              - **RestrictPublicBuckets** *(boolean) --* 
                Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to ``TRUE`` restricts access to this bucket to only AWS services and authorized users within this account if the bucket has a public policy.
                Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the Amazon S3 bucket whose ``PublicAccessBlock`` configuration you want to retrieve.
        :rtype: dict
        :returns:
        """
        pass

    def get_waiter(
        self,
        waiter_name=None,  # type: Optional[str]
    ):
        # type: (...) -> Waiter
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def head_bucket(
        self,
        Bucket,  # type: str
    ):
        # type: (...) -> None
        """
        This operation is useful to determine if a bucket exists and you have permission to access it.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadBucket>`_
        
        **Request Syntax**
        ::
          response = client.head_bucket(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :returns: None
        """
        pass

    def head_object(
        self,
        Bucket,  # type: str
        Key,  # type: str
        IfMatch=None,  # type: Optional[str]
        IfModifiedSince=None,  # type: Optional[datetime]
        IfNoneMatch=None,  # type: Optional[str]
        IfUnmodifiedSince=None,  # type: Optional[datetime]
        Range=None,  # type: Optional[str]
        VersionId=None,  # type: Optional[str]
        SSECustomerAlgorithm=None,  # type: Optional[str]
        SSECustomerKey=None,  # type: Optional[str]
        SSECustomerKeyMD5=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
        PartNumber=None,  # type: Optional[int]
    ):
        # type: (...) -> Dict
        """
        The HEAD operation retrieves metadata from an object without returning the object itself. This operation is useful if you're only interested in an object's metadata. To use HEAD, you must have READ access to the object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject>`_
        
        **Request Syntax**
        ::
          response = client.head_object(
              Bucket='string',
              IfMatch='string',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch='string',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Key='string',
              Range='string',
              VersionId='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              RequestPayer='requester',
              PartNumber=123
          )
        
        **Response Syntax**
        ::
            {
                'DeleteMarker': True|False,
                'AcceptRanges': 'string',
                'Expiration': 'string',
                'Restore': 'string',
                'LastModified': datetime(2015, 1, 1),
                'ContentLength': 123,
                'ETag': 'string',
                'MissingMeta': 123,
                'VersionId': 'string',
                'CacheControl': 'string',
                'ContentDisposition': 'string',
                'ContentEncoding': 'string',
                'ContentLanguage': 'string',
                'ContentType': 'string',
                'Expires': datetime(2015, 1, 1),
                'WebsiteRedirectLocation': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'Metadata': {
                    'string': 'string'
                },
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                'RequestCharged': 'requester',
                'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
                'PartsCount': 123,
                'ObjectLockMode': 'GOVERNANCE'|'COMPLIANCE',
                'ObjectLockRetainUntilDate': datetime(2015, 1, 1),
                'ObjectLockLegalHoldStatus': 'ON'|'OFF'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DeleteMarker** *(boolean) --* 
              Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.
            - **AcceptRanges** *(string) --* 
            - **Expiration** *(string) --* 
              If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
            - **Restore** *(string) --* 
              Provides information about object restoration operation and expiration time of the restored object copy.
            - **LastModified** *(datetime) --* 
              Last modified date of the object
            - **ContentLength** *(integer) --* 
              Size of the body in bytes.
            - **ETag** *(string) --* 
              An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL
            - **MissingMeta** *(integer) --* 
              This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.
            - **VersionId** *(string) --* 
              Version of the object.
            - **CacheControl** *(string) --* 
              Specifies caching behavior along the request/reply chain.
            - **ContentDisposition** *(string) --* 
              Specifies presentational information for the object.
            - **ContentEncoding** *(string) --* 
              Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
            - **ContentLanguage** *(string) --* 
              The language the content is in.
            - **ContentType** *(string) --* 
              A standard MIME type describing the format of the object data.
            - **Expires** *(datetime) --* 
              The date and time at which the object is no longer cacheable.
            - **WebsiteRedirectLocation** *(string) --* 
              If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
            - **ServerSideEncryption** *(string) --* 
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
            - **Metadata** *(dict) --* 
              A map of metadata to store with the object in S3.
              - *(string) --* 
                - *(string) --* 
            - **SSECustomerAlgorithm** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
            - **SSECustomerKeyMD5** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
            - **SSEKMSKeyId** *(string) --* 
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
            - **StorageClass** *(string) --* 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
            - **ReplicationStatus** *(string) --* 
            - **PartsCount** *(integer) --* 
              The count of parts this object has.
            - **ObjectLockMode** *(string) --* 
              The object lock mode currently in place for this object.
            - **ObjectLockRetainUntilDate** *(datetime) --* 
              The date and time when this object's object lock expires.
            - **ObjectLockLegalHoldStatus** *(string) --* 
              The Legal Hold status for the specified object.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type IfMatch: string
        :param IfMatch:
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        :type IfModifiedSince: datetime
        :param IfModifiedSince:
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        :type IfNoneMatch: string
        :param IfNoneMatch:
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince:
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        :type Key: string
        :param Key: **[REQUIRED]**
        :type Range: string
        :param Range:
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        :type VersionId: string
        :param VersionId:
          VersionId used to reference a specific version of the object.
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        :type SSECustomerKey: string
        :param SSECustomerKey:
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type PartNumber: integer
        :param PartNumber:
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.
        :rtype: dict
        :returns:
        """
        pass

    def list_bucket_analytics_configurations(
        self,
        Bucket,  # type: str
        ContinuationToken=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Lists the analytics configurations for the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBucketAnalyticsConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.list_bucket_analytics_configurations(
              Bucket='string',
              ContinuationToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'IsTruncated': True|False,
                'ContinuationToken': 'string',
                'NextContinuationToken': 'string',
                'AnalyticsConfigurationList': [
                    {
                        'Id': 'string',
                        'Filter': {
                            'Prefix': 'string',
                            'Tag': {
                                'Key': 'string',
                                'Value': 'string'
                            },
                            'And': {
                                'Prefix': 'string',
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        },
                        'StorageClassAnalysis': {
                            'DataExport': {
                                'OutputSchemaVersion': 'V_1',
                                'Destination': {
                                    'S3BucketDestination': {
                                        'Format': 'CSV',
                                        'BucketAccountId': 'string',
                                        'Bucket': 'string',
                                        'Prefix': 'string'
                                    }
                                }
                            }
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **IsTruncated** *(boolean) --* 
              Indicates whether the returned list of analytics configurations is complete. A value of true indicates that the list is not complete and the NextContinuationToken will be provided for a subsequent request.
            - **ContinuationToken** *(string) --* 
              The ContinuationToken that represents where this request began.
            - **NextContinuationToken** *(string) --* 
              NextContinuationToken is sent when isTruncated is true, which indicates that there are more analytics configurations to list. The next request must include this NextContinuationToken. The token is obfuscated and is not a usable value.
            - **AnalyticsConfigurationList** *(list) --* 
              The list of analytics configurations for a bucket.
              - *(dict) --* 
                Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.
                For more information, see `GET Bucket analytics <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETAnalyticsConfig.html>`__ in the *Amazon Simple Storage Service API Reference* . 
                - **Id** *(string) --* 
                  The ID that identifies the analytics configuration.
                - **Filter** *(dict) --* 
                  The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.
                  - **Prefix** *(string) --* 
                    The prefix to use when evaluating an analytics filter.
                  - **Tag** *(dict) --* 
                    The tag to use when evaluating an analytics filter.
                    - **Key** *(string) --* 
                      Name of the tag.
                    - **Value** *(string) --* 
                      Value of the tag.
                  - **And** *(dict) --* 
                    A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.
                    - **Prefix** *(string) --* 
                      The prefix to use when evaluating an AND predicate: The prefix that an object must have to be included in the metrics results.
                    - **Tags** *(list) --* 
                      The list of tags to use when evaluating an AND predicate.
                      - *(dict) --* 
                        - **Key** *(string) --* 
                          Name of the tag.
                        - **Value** *(string) --* 
                          Value of the tag.
                - **StorageClassAnalysis** *(dict) --* 
                  Contains data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes. 
                  - **DataExport** *(dict) --* 
                    Specifies how data related to the storage class analysis for an Amazon S3 bucket should be exported.
                    - **OutputSchemaVersion** *(string) --* 
                      The version of the output schema to use when exporting data. Must be ``V_1`` .
                    - **Destination** *(dict) --* 
                      The place to store the data for an analysis.
                      - **S3BucketDestination** *(dict) --* 
                        A destination signifying output to an S3 bucket.
                        - **Format** *(string) --* 
                          Specifies the file format used when exporting data to Amazon S3.
                        - **BucketAccountId** *(string) --* 
                          The account ID that owns the destination bucket. If no account ID is provided, the owner will not be validated prior to exporting data.
                        - **Bucket** *(string) --* 
                          The Amazon Resource Name (ARN) of the bucket to which data is exported.
                        - **Prefix** *(string) --* 
                          The prefix to use when exporting data. The prefix is prepended to all results.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket from which analytics configurations are retrieved.
        :type ContinuationToken: string
        :param ContinuationToken:
          The ContinuationToken that represents a placeholder from where this request should begin.
        :rtype: dict
        :returns:
        """
        pass

    def list_bucket_inventory_configurations(
        self,
        Bucket,  # type: str
        ContinuationToken=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Returns a list of inventory configurations for the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBucketInventoryConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.list_bucket_inventory_configurations(
              Bucket='string',
              ContinuationToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ContinuationToken': 'string',
                'InventoryConfigurationList': [
                    {
                        'Destination': {
                            'S3BucketDestination': {
                                'AccountId': 'string',
                                'Bucket': 'string',
                                'Format': 'CSV'|'ORC'|'Parquet',
                                'Prefix': 'string',
                                'Encryption': {
                                    'SSES3': {},
                                    'SSEKMS': {
                                        'KeyId': 'string'
                                    }
                                }
                            }
                        },
                        'IsEnabled': True|False,
                        'Filter': {
                            'Prefix': 'string'
                        },
                        'Id': 'string',
                        'IncludedObjectVersions': 'All'|'Current',
                        'OptionalFields': [
                            'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'|'ObjectLockMode'|'ObjectLockLegalHoldStatus',
                        ],
                        'Schedule': {
                            'Frequency': 'Daily'|'Weekly'
                        }
                    },
                ],
                'IsTruncated': True|False,
                'NextContinuationToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ContinuationToken** *(string) --* 
              If sent in the request, the marker that is used as a starting point for this inventory configuration list response.
            - **InventoryConfigurationList** *(list) --* 
              The list of inventory configurations for a bucket.
              - *(dict) --* 
                Specifies the inventory configuration for an Amazon S3 bucket. For more information, see `GET Bucket inventory <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETInventoryConfig.html>`__ in the *Amazon Simple Storage Service API Reference* . 
                - **Destination** *(dict) --* 
                  Contains information about where to publish the inventory results.
                  - **S3BucketDestination** *(dict) --* 
                    Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.
                    - **AccountId** *(string) --* 
                      The ID of the account that owns the destination bucket.
                    - **Bucket** *(string) --* 
                      The Amazon resource name (ARN) of the bucket where inventory results will be published.
                    - **Format** *(string) --* 
                      Specifies the output format of the inventory results.
                    - **Prefix** *(string) --* 
                      The prefix that is prepended to all inventory results.
                    - **Encryption** *(dict) --* 
                      Contains the type of server-side encryption used to encrypt the inventory results.
                      - **SSES3** *(dict) --* 
                        Specifies the use of SSE-S3 to encrypt delivered Inventory reports.
                      - **SSEKMS** *(dict) --* 
                        Specifies the use of SSE-KMS to encrypt delivered Inventory reports.
                        - **KeyId** *(string) --* 
                          Specifies the ID of the AWS Key Management Service (KMS) master encryption key to use for encrypting Inventory reports.
                - **IsEnabled** *(boolean) --* 
                  Specifies whether the inventory is enabled or disabled. If set to ``True`` , an inventory list is generated. If set to ``False`` , no inventory list is generated.
                - **Filter** *(dict) --* 
                  Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria.
                  - **Prefix** *(string) --* 
                    The prefix that an object must have to be included in the inventory results.
                - **Id** *(string) --* 
                  The ID used to identify the inventory configuration.
                - **IncludedObjectVersions** *(string) --* 
                  Object versions to include in the inventory list. If set to ``All`` , the list includes all the object versions, which adds the version-related fields ``VersionId`` , ``IsLatest`` , and ``DeleteMarker`` to the list. If set to ``Current`` , the list does not contain these version-related fields.
                - **OptionalFields** *(list) --* 
                  Contains the optional fields that are included in the inventory results.
                  - *(string) --* 
                - **Schedule** *(dict) --* 
                  Specifies the schedule for generating inventory results.
                  - **Frequency** *(string) --* 
                    Specifies how frequently inventory results are produced.
            - **IsTruncated** *(boolean) --* 
              Indicates whether the returned list of inventory configurations is truncated in this response. A value of true indicates that the list is truncated.
            - **NextContinuationToken** *(string) --* 
              The marker used to continue this inventory configuration listing. Use the NextContinuationToken from this response to continue the listing in a subsequent request. The continuation token is an opaque value that Amazon S3 understands.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket containing the inventory configurations to retrieve.
        :type ContinuationToken: string
        :param ContinuationToken:
          The marker used to continue an inventory configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.
        :rtype: dict
        :returns:
        """
        pass

    def list_bucket_metrics_configurations(
        self,
        Bucket,  # type: str
        ContinuationToken=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Lists the metrics configurations for the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBucketMetricsConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.list_bucket_metrics_configurations(
              Bucket='string',
              ContinuationToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'IsTruncated': True|False,
                'ContinuationToken': 'string',
                'NextContinuationToken': 'string',
                'MetricsConfigurationList': [
                    {
                        'Id': 'string',
                        'Filter': {
                            'Prefix': 'string',
                            'Tag': {
                                'Key': 'string',
                                'Value': 'string'
                            },
                            'And': {
                                'Prefix': 'string',
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **IsTruncated** *(boolean) --* 
              Indicates whether the returned list of metrics configurations is complete. A value of true indicates that the list is not complete and the NextContinuationToken will be provided for a subsequent request.
            - **ContinuationToken** *(string) --* 
              The marker that is used as a starting point for this metrics configuration list response. This value is present if it was sent in the request.
            - **NextContinuationToken** *(string) --* 
              The marker used to continue a metrics configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.
            - **MetricsConfigurationList** *(list) --* 
              The list of metrics configurations for a bucket.
              - *(dict) --* 
                Specifies a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from an Amazon S3 bucket. If you're updating an existing metrics configuration, note that this is a full replacement of the existing metrics configuration. If you don't include the elements you want to keep, they are erased. For more information, see `PUT Bucket metrics <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTMetricConfiguration.html>`__ in the *Amazon Simple Storage Service API Reference* .
                - **Id** *(string) --* 
                  The ID used to identify the metrics configuration.
                - **Filter** *(dict) --* 
                  Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter's criteria. A filter must be a prefix, a tag, or a conjunction (MetricsAndOperator).
                  - **Prefix** *(string) --* 
                    The prefix used when evaluating a metrics filter.
                  - **Tag** *(dict) --* 
                    The tag used when evaluating a metrics filter.
                    - **Key** *(string) --* 
                      Name of the tag.
                    - **Value** *(string) --* 
                      Value of the tag.
                  - **And** *(dict) --* 
                    A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.
                    - **Prefix** *(string) --* 
                      The prefix used when evaluating an AND predicate.
                    - **Tags** *(list) --* 
                      The list of tags used when evaluating an AND predicate.
                      - *(dict) --* 
                        - **Key** *(string) --* 
                          Name of the tag.
                        - **Value** *(string) --* 
                          Value of the tag.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket containing the metrics configurations to retrieve.
        :type ContinuationToken: string
        :param ContinuationToken:
          The marker that is used to continue a metrics configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.
        :rtype: dict
        :returns:
        """
        pass

    def list_buckets(
        self,
    ):
        # type: (...) -> Dict
        """
        Returns a list of all buckets owned by the authenticated sender of the request.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBuckets>`_
        
        **Request Syntax**
        ::
          response = client.list_buckets()
        
        **Response Syntax**
        ::
            {
                'Buckets': [
                    {
                        'Name': 'string',
                        'CreationDate': datetime(2015, 1, 1)
                    },
                ],
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Buckets** *(list) --* 
              - *(dict) --* 
                - **Name** *(string) --* 
                  The name of the bucket.
                - **CreationDate** *(datetime) --* 
                  Date the bucket was created.
            - **Owner** *(dict) --* 
              - **DisplayName** *(string) --* 
              - **ID** *(string) --* 
        :rtype: dict
        :returns:
        """
        pass

    def list_multipart_uploads(
        self,
        Bucket,  # type: str
        Delimiter=None,  # type: Optional[str]
        EncodingType=None,  # type: Optional[str]
        KeyMarker=None,  # type: Optional[str]
        MaxUploads=None,  # type: Optional[int]
        Prefix=None,  # type: Optional[str]
        UploadIdMarker=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        This operation lists in-progress multipart uploads.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListMultipartUploads>`_
        
        **Request Syntax**
        ::
          response = client.list_multipart_uploads(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              KeyMarker='string',
              MaxUploads=123,
              Prefix='string',
              UploadIdMarker='string'
          )
        
        **Response Syntax**
        ::
            {
                'Bucket': 'string',
                'KeyMarker': 'string',
                'UploadIdMarker': 'string',
                'NextKeyMarker': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'NextUploadIdMarker': 'string',
                'MaxUploads': 123,
                'IsTruncated': True|False,
                'Uploads': [
                    {
                        'UploadId': 'string',
                        'Key': 'string',
                        'Initiated': datetime(2015, 1, 1),
                        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        },
                        'Initiator': {
                            'ID': 'string',
                            'DisplayName': 'string'
                        }
                    },
                ],
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Bucket** *(string) --* 
              Name of the bucket to which the multipart upload was initiated.
            - **KeyMarker** *(string) --* 
              The key at or after which the listing began.
            - **UploadIdMarker** *(string) --* 
              Upload ID after which listing began.
            - **NextKeyMarker** *(string) --* 
              When a list is truncated, this element specifies the value that should be used for the key-marker request parameter in a subsequent request.
            - **Prefix** *(string) --* 
              When a prefix is provided in the request, this field contains the specified prefix. The result contains only keys starting with the specified prefix.
            - **Delimiter** *(string) --* 
            - **NextUploadIdMarker** *(string) --* 
              When a list is truncated, this element specifies the value that should be used for the upload-id-marker request parameter in a subsequent request.
            - **MaxUploads** *(integer) --* 
              Maximum number of multipart uploads that could have been included in the response.
            - **IsTruncated** *(boolean) --* 
              Indicates whether the returned list of multipart uploads is truncated. A value of true indicates that the list was truncated. The list can be truncated if the number of multipart uploads exceeds the limit allowed or specified by max uploads.
            - **Uploads** *(list) --* 
              - *(dict) --* 
                - **UploadId** *(string) --* 
                  Upload ID that identifies the multipart upload.
                - **Key** *(string) --* 
                  Key of the object for which the multipart upload was initiated.
                - **Initiated** *(datetime) --* 
                  Date and time at which the multipart upload was initiated.
                - **StorageClass** *(string) --* 
                  The class of storage used to store the object.
                - **Owner** *(dict) --* 
                  - **DisplayName** *(string) --* 
                  - **ID** *(string) --* 
                - **Initiator** *(dict) --* 
                  Identifies who initiated the multipart upload.
                  - **ID** *(string) --* 
                    If the principal is an AWS account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.
                  - **DisplayName** *(string) --* 
                    Name of the Principal.
            - **CommonPrefixes** *(list) --* 
              - *(dict) --* 
                - **Prefix** *(string) --* 
            - **EncodingType** *(string) --* 
              Encoding type used by Amazon S3 to encode object keys in the response.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Delimiter: string
        :param Delimiter:
          Character you use to group keys.
        :type EncodingType: string
        :param EncodingType:
          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
        :type KeyMarker: string
        :param KeyMarker:
          Together with upload-id-marker, this parameter specifies the multipart upload after which listing should begin.
        :type MaxUploads: integer
        :param MaxUploads:
          Sets the maximum number of multipart uploads, from 1 to 1,000, to return in the response body. 1,000 is the maximum number of uploads that can be returned in a response.
        :type Prefix: string
        :param Prefix:
          Lists in-progress uploads only for those keys that begin with the specified prefix.
        :type UploadIdMarker: string
        :param UploadIdMarker:
          Together with key-marker, specifies the multipart upload after which listing should begin. If key-marker is not specified, the upload-id-marker parameter is ignored.
        :rtype: dict
        :returns:
        """
        pass

    def list_object_versions(
        self,
        Bucket,  # type: str
        Delimiter=None,  # type: Optional[str]
        EncodingType=None,  # type: Optional[str]
        KeyMarker=None,  # type: Optional[str]
        MaxKeys=None,  # type: Optional[int]
        Prefix=None,  # type: Optional[str]
        VersionIdMarker=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Returns metadata about all of the versions of objects in a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjectVersions>`_
        
        **Request Syntax**
        ::
          response = client.list_object_versions(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              KeyMarker='string',
              MaxKeys=123,
              Prefix='string',
              VersionIdMarker='string'
          )
        
        **Response Syntax**
        ::
            {
                'IsTruncated': True|False,
                'KeyMarker': 'string',
                'VersionIdMarker': 'string',
                'NextKeyMarker': 'string',
                'NextVersionIdMarker': 'string',
                'Versions': [
                    {
                        'ETag': 'string',
                        'Size': 123,
                        'StorageClass': 'STANDARD',
                        'Key': 'string',
                        'VersionId': 'string',
                        'IsLatest': True|False,
                        'LastModified': datetime(2015, 1, 1),
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        }
                    },
                ],
                'DeleteMarkers': [
                    {
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        },
                        'Key': 'string',
                        'VersionId': 'string',
                        'IsLatest': True|False,
                        'LastModified': datetime(2015, 1, 1)
                    },
                ],
                'Name': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxKeys': 123,
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **IsTruncated** *(boolean) --* 
              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the search criteria. If your results were truncated, you can make a follow-up paginated request using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in another request to return the rest of the results.
            - **KeyMarker** *(string) --* 
              Marks the last Key returned in a truncated response.
            - **VersionIdMarker** *(string) --* 
            - **NextKeyMarker** *(string) --* 
              Use this value for the key marker request parameter in a subsequent request.
            - **NextVersionIdMarker** *(string) --* 
              Use this value for the next version id marker parameter in a subsequent request.
            - **Versions** *(list) --* 
              - *(dict) --* 
                - **ETag** *(string) --* 
                - **Size** *(integer) --* 
                  Size in bytes of the object.
                - **StorageClass** *(string) --* 
                  The class of storage used to store the object.
                - **Key** *(string) --* 
                  The object key.
                - **VersionId** *(string) --* 
                  Version ID of an object.
                - **IsLatest** *(boolean) --* 
                  Specifies whether the object is (true) or is not (false) the latest version of an object.
                - **LastModified** *(datetime) --* 
                  Date and time the object was last modified.
                - **Owner** *(dict) --* 
                  - **DisplayName** *(string) --* 
                  - **ID** *(string) --* 
            - **DeleteMarkers** *(list) --* 
              - *(dict) --* 
                - **Owner** *(dict) --* 
                  - **DisplayName** *(string) --* 
                  - **ID** *(string) --* 
                - **Key** *(string) --* 
                  The object key.
                - **VersionId** *(string) --* 
                  Version ID of an object.
                - **IsLatest** *(boolean) --* 
                  Specifies whether the object is (true) or is not (false) the latest version of an object.
                - **LastModified** *(datetime) --* 
                  Date and time the object was last modified.
            - **Name** *(string) --* 
            - **Prefix** *(string) --* 
            - **Delimiter** *(string) --* 
            - **MaxKeys** *(integer) --* 
            - **CommonPrefixes** *(list) --* 
              - *(dict) --* 
                - **Prefix** *(string) --* 
            - **EncodingType** *(string) --* 
              Encoding type used by Amazon S3 to encode object keys in the response.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Delimiter: string
        :param Delimiter:
          A delimiter is a character you use to group keys.
        :type EncodingType: string
        :param EncodingType:
          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
        :type KeyMarker: string
        :param KeyMarker:
          Specifies the key to start with when listing objects in a bucket.
        :type MaxKeys: integer
        :param MaxKeys:
          Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.
        :type Prefix: string
        :param Prefix:
          Limits the response to keys that begin with the specified prefix.
        :type VersionIdMarker: string
        :param VersionIdMarker:
          Specifies the object version you want to start listing from.
        :rtype: dict
        :returns:
        """
        pass

    def list_objects(
        self,
        Bucket,  # type: str
        Delimiter=None,  # type: Optional[str]
        EncodingType=None,  # type: Optional[str]
        Marker=None,  # type: Optional[str]
        MaxKeys=None,  # type: Optional[int]
        Prefix=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Returns some or all (up to 1000) of the objects in a bucket. You can use the request parameters as selection criteria to return a subset of the objects in a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjects>`_
        
        **Request Syntax**
        ::
          response = client.list_objects(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              Marker='string',
              MaxKeys=123,
              Prefix='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'IsTruncated': True|False,
                'Marker': 'string',
                'NextMarker': 'string',
                'Contents': [
                    {
                        'Key': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'ETag': 'string',
                        'Size': 123,
                        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        }
                    },
                ],
                'Name': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxKeys': 123,
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **IsTruncated** *(boolean) --* 
              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the search criteria.
            - **Marker** *(string) --* 
            - **NextMarker** *(string) --* 
              When response is truncated (the IsTruncated element value in the response is true), you can use the key name in this field as marker in the subsequent request to get next set of objects. Amazon S3 lists objects in alphabetical order Note: This element is returned only if you have delimiter request parameter specified. If response does not include the NextMaker and it is truncated, you can use the value of the last Key in the response as the marker in the subsequent request to get the next set of object keys.
            - **Contents** *(list) --* 
              - *(dict) --* 
                - **Key** *(string) --* 
                - **LastModified** *(datetime) --* 
                - **ETag** *(string) --* 
                - **Size** *(integer) --* 
                - **StorageClass** *(string) --* 
                  The class of storage used to store the object.
                - **Owner** *(dict) --* 
                  - **DisplayName** *(string) --* 
                  - **ID** *(string) --* 
            - **Name** *(string) --* 
            - **Prefix** *(string) --* 
            - **Delimiter** *(string) --* 
            - **MaxKeys** *(integer) --* 
            - **CommonPrefixes** *(list) --* 
              - *(dict) --* 
                - **Prefix** *(string) --* 
            - **EncodingType** *(string) --* 
              Encoding type used by Amazon S3 to encode object keys in the response.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Delimiter: string
        :param Delimiter:
          A delimiter is a character you use to group keys.
        :type EncodingType: string
        :param EncodingType:
          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
        :type Marker: string
        :param Marker:
          Specifies the key to start with when listing objects in a bucket.
        :type MaxKeys: integer
        :param MaxKeys:
          Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.
        :type Prefix: string
        :param Prefix:
          Limits the response to keys that begin with the specified prefix.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the list objects request. Bucket owners need not specify this parameter in their requests.
        :rtype: dict
        :returns:
        """
        pass

    def list_objects_v2(
        self,
        Bucket,  # type: str
        Delimiter=None,  # type: Optional[str]
        EncodingType=None,  # type: Optional[str]
        MaxKeys=None,  # type: Optional[int]
        Prefix=None,  # type: Optional[str]
        ContinuationToken=None,  # type: Optional[str]
        FetchOwner=None,  # type: Optional[bool]
        StartAfter=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Returns some or all (up to 1000) of the objects in a bucket. You can use the request parameters as selection criteria to return a subset of the objects in a bucket. Note: ListObjectsV2 is the revised List Objects API and we recommend you use this revised API for new application development.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjectsV2>`_
        
        **Request Syntax**
        ::
          response = client.list_objects_v2(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              MaxKeys=123,
              Prefix='string',
              ContinuationToken='string',
              FetchOwner=True|False,
              StartAfter='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'IsTruncated': True|False,
                'Contents': [
                    {
                        'Key': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'ETag': 'string',
                        'Size': 123,
                        'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        }
                    },
                ],
                'Name': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxKeys': 123,
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url',
                'KeyCount': 123,
                'ContinuationToken': 'string',
                'NextContinuationToken': 'string',
                'StartAfter': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **IsTruncated** *(boolean) --* 
              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the search criteria.
            - **Contents** *(list) --* 
              Metadata about each object returned.
              - *(dict) --* 
                - **Key** *(string) --* 
                - **LastModified** *(datetime) --* 
                - **ETag** *(string) --* 
                - **Size** *(integer) --* 
                - **StorageClass** *(string) --* 
                  The class of storage used to store the object.
                - **Owner** *(dict) --* 
                  - **DisplayName** *(string) --* 
                  - **ID** *(string) --* 
            - **Name** *(string) --* 
              Name of the bucket to list.
            - **Prefix** *(string) --* 
              Limits the response to keys that begin with the specified prefix.
            - **Delimiter** *(string) --* 
              A delimiter is a character you use to group keys.
            - **MaxKeys** *(integer) --* 
              Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.
            - **CommonPrefixes** *(list) --* 
              CommonPrefixes contains all (if there are any) keys between Prefix and the next occurrence of the string specified by delimiter
              - *(dict) --* 
                - **Prefix** *(string) --* 
            - **EncodingType** *(string) --* 
              Encoding type used by Amazon S3 to encode object keys in the response.
            - **KeyCount** *(integer) --* 
              KeyCount is the number of keys returned with this request. KeyCount will always be less than equals to MaxKeys field. Say you ask for 50 keys, your result will include less than equals 50 keys 
            - **ContinuationToken** *(string) --* 
              ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a token. ContinuationToken is obfuscated and is not a real key
            - **NextContinuationToken** *(string) --* 
              NextContinuationToken is sent when isTruncated is true which means there are more keys in the bucket that can be listed. The next list requests to Amazon S3 can be continued with this NextContinuationToken. NextContinuationToken is obfuscated and is not a real key
            - **StartAfter** *(string) --* 
              StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          Name of the bucket to list.
        :type Delimiter: string
        :param Delimiter:
          A delimiter is a character you use to group keys.
        :type EncodingType: string
        :param EncodingType:
          Encoding type used by Amazon S3 to encode object keys in the response.
        :type MaxKeys: integer
        :param MaxKeys:
          Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.
        :type Prefix: string
        :param Prefix:
          Limits the response to keys that begin with the specified prefix.
        :type ContinuationToken: string
        :param ContinuationToken:
          ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a token. ContinuationToken is obfuscated and is not a real key
        :type FetchOwner: boolean
        :param FetchOwner:
          The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true
        :type StartAfter: string
        :param StartAfter:
          StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the list objects request in V2 style. Bucket owners need not specify this parameter in their requests.
        :rtype: dict
        :returns:
        """
        pass

    def list_parts(
        self,
        Bucket,  # type: str
        Key,  # type: str
        UploadId,  # type: str
        MaxParts=None,  # type: Optional[int]
        PartNumberMarker=None,  # type: Optional[int]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Lists the parts that have been uploaded for a specific multipart upload.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListParts>`_
        
        **Request Syntax**
        ::
          response = client.list_parts(
              Bucket='string',
              Key='string',
              MaxParts=123,
              PartNumberMarker=123,
              UploadId='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'AbortDate': datetime(2015, 1, 1),
                'AbortRuleId': 'string',
                'Bucket': 'string',
                'Key': 'string',
                'UploadId': 'string',
                'PartNumberMarker': 123,
                'NextPartNumberMarker': 123,
                'MaxParts': 123,
                'IsTruncated': True|False,
                'Parts': [
                    {
                        'PartNumber': 123,
                        'LastModified': datetime(2015, 1, 1),
                        'ETag': 'string',
                        'Size': 123
                    },
                ],
                'Initiator': {
                    'ID': 'string',
                    'DisplayName': 'string'
                },
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                },
                'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AbortDate** *(datetime) --* 
              Date when multipart upload will become eligible for abort operation by lifecycle.
            - **AbortRuleId** *(string) --* 
              Id of the lifecycle rule that makes a multipart upload eligible for abort operation.
            - **Bucket** *(string) --* 
              Name of the bucket to which the multipart upload was initiated.
            - **Key** *(string) --* 
              Object key for which the multipart upload was initiated.
            - **UploadId** *(string) --* 
              Upload ID identifying the multipart upload whose parts are being listed.
            - **PartNumberMarker** *(integer) --* 
              Part number after which listing begins.
            - **NextPartNumberMarker** *(integer) --* 
              When a list is truncated, this element specifies the last part in the list, as well as the value to use for the part-number-marker request parameter in a subsequent request.
            - **MaxParts** *(integer) --* 
              Maximum number of parts that were allowed in the response.
            - **IsTruncated** *(boolean) --* 
              Indicates whether the returned list of parts is truncated.
            - **Parts** *(list) --* 
              - *(dict) --* 
                - **PartNumber** *(integer) --* 
                  Part number identifying the part. This is a positive integer between 1 and 10,000.
                - **LastModified** *(datetime) --* 
                  Date and time at which the part was uploaded.
                - **ETag** *(string) --* 
                  Entity tag returned when the part was uploaded.
                - **Size** *(integer) --* 
                  Size in bytes of the uploaded part data.
            - **Initiator** *(dict) --* 
              Identifies who initiated the multipart upload.
              - **ID** *(string) --* 
                If the principal is an AWS account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.
              - **DisplayName** *(string) --* 
                Name of the Principal.
            - **Owner** *(dict) --* 
              - **DisplayName** *(string) --* 
              - **ID** *(string) --* 
            - **StorageClass** *(string) --* 
              The class of storage used to store the object.
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Key: string
        :param Key: **[REQUIRED]**
        :type MaxParts: integer
        :param MaxParts:
          Sets the maximum number of parts to return.
        :type PartNumberMarker: integer
        :param PartNumberMarker:
          Specifies the part after which listing should begin. Only parts with higher part numbers will be listed.
        :type UploadId: string
        :param UploadId: **[REQUIRED]**
          Upload ID identifying the multipart upload whose parts are being listed.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass

    def put_bucket_accelerate_configuration(
        self,
        Bucket,  # type: str
        AccelerateConfiguration,  # type: Dict
    ):
        # type: (...) -> None
        """
        Sets the accelerate configuration of an existing bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketAccelerateConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_accelerate_configuration(
              Bucket='string',
              AccelerateConfiguration={
                  'Status': 'Enabled'|'Suspended'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          Name of the bucket for which the accelerate configuration is set.
        :type AccelerateConfiguration: dict
        :param AccelerateConfiguration: **[REQUIRED]**
          Specifies the Accelerate Configuration you want to set for the bucket.
          - **Status** *(string) --*
            Specifies the transfer acceleration status of the bucket.
        :returns: None
        """
        pass

    def put_bucket_acl(
        self,
        Bucket,  # type: str
        ACL=None,  # type: Optional[str]
        AccessControlPolicy=None,  # type: Optional[Dict]
        GrantFullControl=None,  # type: Optional[str]
        GrantRead=None,  # type: Optional[str]
        GrantReadACP=None,  # type: Optional[str]
        GrantWrite=None,  # type: Optional[str]
        GrantWriteACP=None,  # type: Optional[str]
    ):
        # type: (...) -> None
        """
        Sets the permissions on a bucket using access control lists (ACL).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketAcl>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_acl(
              ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
              AccessControlPolicy={
                  'Grants': [
                      {
                          'Grantee': {
                              'DisplayName': 'string',
                              'EmailAddress': 'string',
                              'ID': 'string',
                              'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                              'URI': 'string'
                          },
                          'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                      },
                  ],
                  'Owner': {
                      'DisplayName': 'string',
                      'ID': 'string'
                  }
              },
              Bucket='string',
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWrite='string',
              GrantWriteACP='string'
          )
        :type ACL: string
        :param ACL:
          The canned ACL to apply to the bucket.
        :type AccessControlPolicy: dict
        :param AccessControlPolicy:
          Contains the elements that set the ACL permissions for an object per grantee.
          - **Grants** *(list) --*
            A list of grants.
            - *(dict) --*
              - **Grantee** *(dict) --*
                - **DisplayName** *(string) --*
                  Screen name of the grantee.
                - **EmailAddress** *(string) --*
                  Email address of the grantee.
                - **ID** *(string) --*
                  The canonical user ID of the grantee.
                - **Type** *(string) --* **[REQUIRED]**
                  Type of grantee
                - **URI** *(string) --*
                  URI of the grantee group.
              - **Permission** *(string) --*
                Specifies the permission given to the grantee.
          - **Owner** *(dict) --*
            Container for the bucket owner\'s display name and ID.
            - **DisplayName** *(string) --*
            - **ID** *(string) --*
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type GrantFullControl: string
        :param GrantFullControl:
          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
        :type GrantRead: string
        :param GrantRead:
          Allows grantee to list the objects in the bucket.
        :type GrantReadACP: string
        :param GrantReadACP:
          Allows grantee to read the bucket ACL.
        :type GrantWrite: string
        :param GrantWrite:
          Allows grantee to create, overwrite, and delete any object in the bucket.
        :type GrantWriteACP: string
        :param GrantWriteACP:
          Allows grantee to write the ACL for the applicable bucket.
        :returns: None
        """
        pass

    def put_bucket_analytics_configuration(
        self,
        Bucket,  # type: str
        Id,  # type: str
        AnalyticsConfiguration,  # type: Dict
    ):
        # type: (...) -> None
        """
        Sets an analytics configuration for the bucket (specified by the analytics configuration ID).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketAnalyticsConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_analytics_configuration(
              Bucket='string',
              Id='string',
              AnalyticsConfiguration={
                  'Id': 'string',
                  'Filter': {
                      'Prefix': 'string',
                      'Tag': {
                          'Key': 'string',
                          'Value': 'string'
                      },
                      'And': {
                          'Prefix': 'string',
                          'Tags': [
                              {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                          ]
                      }
                  },
                  'StorageClassAnalysis': {
                      'DataExport': {
                          'OutputSchemaVersion': 'V_1',
                          'Destination': {
                              'S3BucketDestination': {
                                  'Format': 'CSV',
                                  'BucketAccountId': 'string',
                                  'Bucket': 'string',
                                  'Prefix': 'string'
                              }
                          }
                      }
                  }
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket to which an analytics configuration is stored.
        :type Id: string
        :param Id: **[REQUIRED]**
          The ID that identifies the analytics configuration.
        :type AnalyticsConfiguration: dict
        :param AnalyticsConfiguration: **[REQUIRED]**
          The configuration and any analyses for the analytics filter.
          - **Id** *(string) --* **[REQUIRED]**
            The ID that identifies the analytics configuration.
          - **Filter** *(dict) --*
            The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.
            - **Prefix** *(string) --*
              The prefix to use when evaluating an analytics filter.
            - **Tag** *(dict) --*
              The tag to use when evaluating an analytics filter.
              - **Key** *(string) --* **[REQUIRED]**
                Name of the tag.
              - **Value** *(string) --* **[REQUIRED]**
                Value of the tag.
            - **And** *(dict) --*
              A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter. The operator must have at least two predicates.
              - **Prefix** *(string) --*
                The prefix to use when evaluating an AND predicate: The prefix that an object must have to be included in the metrics results.
              - **Tags** *(list) --*
                The list of tags to use when evaluating an AND predicate.
                - *(dict) --*
                  - **Key** *(string) --* **[REQUIRED]**
                    Name of the tag.
                  - **Value** *(string) --* **[REQUIRED]**
                    Value of the tag.
          - **StorageClassAnalysis** *(dict) --* **[REQUIRED]**
            Contains data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes.
            - **DataExport** *(dict) --*
              Specifies how data related to the storage class analysis for an Amazon S3 bucket should be exported.
              - **OutputSchemaVersion** *(string) --* **[REQUIRED]**
                The version of the output schema to use when exporting data. Must be ``V_1`` .
              - **Destination** *(dict) --* **[REQUIRED]**
                The place to store the data for an analysis.
                - **S3BucketDestination** *(dict) --* **[REQUIRED]**
                  A destination signifying output to an S3 bucket.
                  - **Format** *(string) --* **[REQUIRED]**
                    Specifies the file format used when exporting data to Amazon S3.
                  - **BucketAccountId** *(string) --*
                    The account ID that owns the destination bucket. If no account ID is provided, the owner will not be validated prior to exporting data.
                  - **Bucket** *(string) --* **[REQUIRED]**
                    The Amazon Resource Name (ARN) of the bucket to which data is exported.
                  - **Prefix** *(string) --*
                    The prefix to use when exporting data. The prefix is prepended to all results.
        :returns: None
        """
        pass

    def put_bucket_cors(
        self,
        Bucket,  # type: str
        CORSConfiguration,  # type: Dict
    ):
        # type: (...) -> None
        """
        Sets the CORS configuration for a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketCors>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_cors(
              Bucket='string',
              CORSConfiguration={
                  'CORSRules': [
                      {
                          'AllowedHeaders': [
                              'string',
                          ],
                          'AllowedMethods': [
                              'string',
                          ],
                          'AllowedOrigins': [
                              'string',
                          ],
                          'ExposeHeaders': [
                              'string',
                          ],
                          'MaxAgeSeconds': 123
                      },
                  ]
              },
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type CORSConfiguration: dict
        :param CORSConfiguration: **[REQUIRED]**
          - **CORSRules** *(list) --* **[REQUIRED]**
            A set of allowed origins and methods.
            - *(dict) --*
              Specifies a cross-origin access rule for an Amazon S3 bucket.
              - **AllowedHeaders** *(list) --*
                Headers that are specified in the ``Access-Control-Request-Headers`` header. These headers are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request, Amazon S3 returns any requested headers that are allowed.
                - *(string) --*
              - **AllowedMethods** *(list) --* **[REQUIRED]**
                An HTTP method that you allow the origin to execute. Valid values are ``GET`` , ``PUT`` , ``HEAD`` , ``POST`` , and ``DELETE`` .
                - *(string) --*
              - **AllowedOrigins** *(list) --* **[REQUIRED]**
                One or more origins you want customers to be able to access the bucket from.
                - *(string) --*
              - **ExposeHeaders** *(list) --*
                One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript ``XMLHttpRequest`` object).
                - *(string) --*
              - **MaxAgeSeconds** *(integer) --*
                The time in seconds that your browser is to cache the preflight response for the specified resource.
        :returns: None
        """
        pass

    def put_bucket_encryption(
        self,
        Bucket,  # type: str
        ServerSideEncryptionConfiguration,  # type: Dict
        ContentMD5=None,  # type: Optional[str]
    ):
        # type: (...) -> None
        """
        Creates a new server-side encryption configuration (or replaces an existing one, if present).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketEncryption>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_encryption(
              Bucket='string',
              ContentMD5='string',
              ServerSideEncryptionConfiguration={
                  'Rules': [
                      {
                          'ApplyServerSideEncryptionByDefault': {
                              'SSEAlgorithm': 'AES256'|'aws:kms',
                              'KMSMasterKeyID': 'string'
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          Specifies default encryption for a bucket using server-side encryption with Amazon S3-managed keys (SSE-S3) or AWS KMS-managed keys (SSE-KMS). For information about the Amazon S3 default encryption feature, see `Amazon S3 Default Bucket Encryption <https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
        :type ContentMD5: string
        :param ContentMD5:
          The base64-encoded 128-bit MD5 digest of the server-side encryption configuration. This parameter is auto-populated when using the command from the CLI.
        :type ServerSideEncryptionConfiguration: dict
        :param ServerSideEncryptionConfiguration: **[REQUIRED]**
          - **Rules** *(list) --* **[REQUIRED]**
            Container for information about a particular server-side encryption configuration rule.
            - *(dict) --*
              Specifies the default server-side encryption configuration.
              - **ApplyServerSideEncryptionByDefault** *(dict) --*
                Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn\'t specify any server-side encryption, this default encryption will be applied.
                - **SSEAlgorithm** *(string) --* **[REQUIRED]**
                  Server-side encryption algorithm to use for the default encryption.
                - **KMSMasterKeyID** *(string) --*
                  KMS master key ID to use for the default encryption. This parameter is allowed if and only if ``SSEAlgorithm`` is set to ``aws:kms`` .
        :returns: None
        """
        pass

    def put_bucket_inventory_configuration(
        self,
        Bucket,  # type: str
        Id,  # type: str
        InventoryConfiguration,  # type: Dict
    ):
        # type: (...) -> None
        """
        Adds an inventory configuration (identified by the inventory ID) from the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketInventoryConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_inventory_configuration(
              Bucket='string',
              Id='string',
              InventoryConfiguration={
                  'Destination': {
                      'S3BucketDestination': {
                          'AccountId': 'string',
                          'Bucket': 'string',
                          'Format': 'CSV'|'ORC'|'Parquet',
                          'Prefix': 'string',
                          'Encryption': {
                              'SSES3': {}
                              ,
                              'SSEKMS': {
                                  'KeyId': 'string'
                              }
                          }
                      }
                  },
                  'IsEnabled': True|False,
                  'Filter': {
                      'Prefix': 'string'
                  },
                  'Id': 'string',
                  'IncludedObjectVersions': 'All'|'Current',
                  'OptionalFields': [
                      'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'|'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'|'ObjectLockMode'|'ObjectLockLegalHoldStatus',
                  ],
                  'Schedule': {
                      'Frequency': 'Daily'|'Weekly'
                  }
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket where the inventory configuration will be stored.
        :type Id: string
        :param Id: **[REQUIRED]**
          The ID used to identify the inventory configuration.
        :type InventoryConfiguration: dict
        :param InventoryConfiguration: **[REQUIRED]**
          Specifies the inventory configuration.
          - **Destination** *(dict) --* **[REQUIRED]**
            Contains information about where to publish the inventory results.
            - **S3BucketDestination** *(dict) --* **[REQUIRED]**
              Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.
              - **AccountId** *(string) --*
                The ID of the account that owns the destination bucket.
              - **Bucket** *(string) --* **[REQUIRED]**
                The Amazon resource name (ARN) of the bucket where inventory results will be published.
              - **Format** *(string) --* **[REQUIRED]**
                Specifies the output format of the inventory results.
              - **Prefix** *(string) --*
                The prefix that is prepended to all inventory results.
              - **Encryption** *(dict) --*
                Contains the type of server-side encryption used to encrypt the inventory results.
                - **SSES3** *(dict) --*
                  Specifies the use of SSE-S3 to encrypt delivered Inventory reports.
                - **SSEKMS** *(dict) --*
                  Specifies the use of SSE-KMS to encrypt delivered Inventory reports.
                  - **KeyId** *(string) --* **[REQUIRED]**
                    Specifies the ID of the AWS Key Management Service (KMS) master encryption key to use for encrypting Inventory reports.
          - **IsEnabled** *(boolean) --* **[REQUIRED]**
            Specifies whether the inventory is enabled or disabled. If set to ``True`` , an inventory list is generated. If set to ``False`` , no inventory list is generated.
          - **Filter** *(dict) --*
            Specifies an inventory filter. The inventory only includes objects that meet the filter\'s criteria.
            - **Prefix** *(string) --* **[REQUIRED]**
              The prefix that an object must have to be included in the inventory results.
          - **Id** *(string) --* **[REQUIRED]**
            The ID used to identify the inventory configuration.
          - **IncludedObjectVersions** *(string) --* **[REQUIRED]**
            Object versions to include in the inventory list. If set to ``All`` , the list includes all the object versions, which adds the version-related fields ``VersionId`` , ``IsLatest`` , and ``DeleteMarker`` to the list. If set to ``Current`` , the list does not contain these version-related fields.
          - **OptionalFields** *(list) --*
            Contains the optional fields that are included in the inventory results.
            - *(string) --*
          - **Schedule** *(dict) --* **[REQUIRED]**
            Specifies the schedule for generating inventory results.
            - **Frequency** *(string) --* **[REQUIRED]**
              Specifies how frequently inventory results are produced.
        :returns: None
        """
        pass

    def put_bucket_lifecycle(
        self,
        Bucket,  # type: str
        LifecycleConfiguration=None,  # type: Optional[Dict]
    ):
        # type: (...) -> None
        """
        No longer used, see the PutBucketLifecycleConfiguration operation.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketLifecycle>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_lifecycle(
              Bucket='string',
              LifecycleConfiguration={
                  'Rules': [
                      {
                          'Expiration': {
                              'Date': datetime(2015, 1, 1),
                              'Days': 123,
                              'ExpiredObjectDeleteMarker': True|False
                          },
                          'ID': 'string',
                          'Prefix': 'string',
                          'Status': 'Enabled'|'Disabled',
                          'Transition': {
                              'Date': datetime(2015, 1, 1),
                              'Days': 123,
                              'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                          },
                          'NoncurrentVersionTransition': {
                              'NoncurrentDays': 123,
                              'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                          },
                          'NoncurrentVersionExpiration': {
                              'NoncurrentDays': 123
                          },
                          'AbortIncompleteMultipartUpload': {
                              'DaysAfterInitiation': 123
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type LifecycleConfiguration: dict
        :param LifecycleConfiguration:
          - **Rules** *(list) --* **[REQUIRED]**
            - *(dict) --*
              Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__ in the *Amazon Simple Storage Service API Reference* .
              - **Expiration** *(dict) --*
                - **Date** *(datetime) --*
                  Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
                - **Days** *(integer) --*
                  Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
                - **ExpiredObjectDeleteMarker** *(boolean) --*
                  Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
              - **ID** *(string) --*
                Unique identifier for the rule. The value can\'t be longer than 255 characters.
              - **Prefix** *(string) --* **[REQUIRED]**
                Object key prefix that identifies one or more objects to which this rule applies.
              - **Status** *(string) --* **[REQUIRED]**
                If ``Enabled`` , the rule is currently being applied. If ``Disabled`` , the rule is not currently being applied.
              - **Transition** *(dict) --*
                - **Date** *(datetime) --*
                  Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.
                - **Days** *(integer) --*
                  Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.
                - **StorageClass** *(string) --*
                  The storage class to which you want the object to transition.
              - **NoncurrentVersionTransition** *(dict) --*
                - **NoncurrentDays** *(integer) --*
                  Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                - **StorageClass** *(string) --*
                  The class of storage used to store the object.
              - **NoncurrentVersionExpiration** *(dict) --*
                - **NoncurrentDays** *(integer) --*
                  Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__ in the Amazon Simple Storage Service Developer Guide.
              - **AbortIncompleteMultipartUpload** *(dict) --*
                - **DaysAfterInitiation** *(integer) --*
                  Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.
        :returns: None
        """
        pass

    def put_bucket_lifecycle_configuration(
        self,
        Bucket,  # type: str
        LifecycleConfiguration=None,  # type: Optional[Dict]
    ):
        # type: (...) -> None
        """
        Sets lifecycle configuration for your bucket. If a lifecycle configuration exists, it replaces it.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketLifecycleConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_lifecycle_configuration(
              Bucket='string',
              LifecycleConfiguration={
                  'Rules': [
                      {
                          'Expiration': {
                              'Date': datetime(2015, 1, 1),
                              'Days': 123,
                              'ExpiredObjectDeleteMarker': True|False
                          },
                          'ID': 'string',
                          'Prefix': 'string',
                          'Filter': {
                              'Prefix': 'string',
                              'Tag': {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                              'And': {
                                  'Prefix': 'string',
                                  'Tags': [
                                      {
                                          'Key': 'string',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          },
                          'Status': 'Enabled'|'Disabled',
                          'Transitions': [
                              {
                                  'Date': datetime(2015, 1, 1),
                                  'Days': 123,
                                  'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                              },
                          ],
                          'NoncurrentVersionTransitions': [
                              {
                                  'NoncurrentDays': 123,
                                  'StorageClass': 'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                              },
                          ],
                          'NoncurrentVersionExpiration': {
                              'NoncurrentDays': 123
                          },
                          'AbortIncompleteMultipartUpload': {
                              'DaysAfterInitiation': 123
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type LifecycleConfiguration: dict
        :param LifecycleConfiguration:
          - **Rules** *(list) --* **[REQUIRED]**
            A lifecycle rule for individual objects in an Amazon S3 bucket.
            - *(dict) --*
              - **Expiration** *(dict) --*
                - **Date** *(datetime) --*
                  Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
                - **Days** *(integer) --*
                  Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
                - **ExpiredObjectDeleteMarker** *(boolean) --*
                  Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
              - **ID** *(string) --*
                Unique identifier for the rule. The value cannot be longer than 255 characters.
              - **Prefix** *(string) --*
                Prefix identifying one or more objects to which the rule applies. This is No longer used; use Filter instead.
              - **Filter** *(dict) --*
                - **Prefix** *(string) --*
                  Prefix identifying one or more objects to which the rule applies.
                - **Tag** *(dict) --*
                  This tag must exist in the object\'s tag set in order for the rule to apply.
                  - **Key** *(string) --* **[REQUIRED]**
                    Name of the tag.
                  - **Value** *(string) --* **[REQUIRED]**
                    Value of the tag.
                - **And** *(dict) --*
                  - **Prefix** *(string) --*
                  - **Tags** *(list) --*
                    All of these tags must exist in the object\'s tag set in order for the rule to apply.
                    - *(dict) --*
                      - **Key** *(string) --* **[REQUIRED]**
                        Name of the tag.
                      - **Value** *(string) --* **[REQUIRED]**
                        Value of the tag.
              - **Status** *(string) --* **[REQUIRED]**
                If \'Enabled\', the rule is currently being applied. If \'Disabled\', the rule is not currently being applied.
              - **Transitions** *(list) --*
                - *(dict) --*
                  Specifies when an object transitions to a specified storage class.
                  - **Date** *(datetime) --*
                    Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.
                  - **Days** *(integer) --*
                    Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.
                  - **StorageClass** *(string) --*
                    The storage class to which you want the object to transition.
              - **NoncurrentVersionTransitions** *(list) --*
                - *(dict) --*
                  Container for the transition rule that describes when noncurrent objects transition to the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` , ``GLACIER`` , or ``DEEP_ARCHIVE`` storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` , ``GLACIER`` , or ``DEEP_ARCHIVE`` storage class at a specific period in the object\'s lifetime.
                  - **NoncurrentDays** *(integer) --*
                    Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                  - **StorageClass** *(string) --*
                    The class of storage used to store the object.
              - **NoncurrentVersionExpiration** *(dict) --*
                - **NoncurrentDays** *(integer) --*
                  Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__ in the Amazon Simple Storage Service Developer Guide.
              - **AbortIncompleteMultipartUpload** *(dict) --*
                - **DaysAfterInitiation** *(integer) --*
                  Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.
        :returns: None
        """
        pass

    def put_bucket_logging(
        self,
        Bucket,  # type: str
        BucketLoggingStatus,  # type: Dict
    ):
        # type: (...) -> None
        """
        Set the logging parameters for a bucket and to specify permissions for who can view and modify the logging parameters. To set the logging status of a bucket, you must be the bucket owner.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketLogging>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_logging(
              Bucket='string',
              BucketLoggingStatus={
                  'LoggingEnabled': {
                      'TargetBucket': 'string',
                      'TargetGrants': [
                          {
                              'Grantee': {
                                  'DisplayName': 'string',
                                  'EmailAddress': 'string',
                                  'ID': 'string',
                                  'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                                  'URI': 'string'
                              },
                              'Permission': 'FULL_CONTROL'|'READ'|'WRITE'
                          },
                      ],
                      'TargetPrefix': 'string'
                  }
              },
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type BucketLoggingStatus: dict
        :param BucketLoggingStatus: **[REQUIRED]**
          - **LoggingEnabled** *(dict) --*
            - **TargetBucket** *(string) --* **[REQUIRED]**
              Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case you should choose a different TargetPrefix for each source bucket so that the delivered log files can be distinguished by key.
            - **TargetGrants** *(list) --*
              - *(dict) --*
                - **Grantee** *(dict) --*
                  - **DisplayName** *(string) --*
                    Screen name of the grantee.
                  - **EmailAddress** *(string) --*
                    Email address of the grantee.
                  - **ID** *(string) --*
                    The canonical user ID of the grantee.
                  - **Type** *(string) --* **[REQUIRED]**
                    Type of grantee
                  - **URI** *(string) --*
                    URI of the grantee group.
                - **Permission** *(string) --*
                  Logging permissions assigned to the Grantee for the bucket.
            - **TargetPrefix** *(string) --* **[REQUIRED]**
              A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket.
        :returns: None
        """
        pass

    def put_bucket_metrics_configuration(
        self,
        Bucket,  # type: str
        Id,  # type: str
        MetricsConfiguration,  # type: Dict
    ):
        # type: (...) -> None
        """
        Sets a metrics configuration (specified by the metrics configuration ID) for the bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketMetricsConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_metrics_configuration(
              Bucket='string',
              Id='string',
              MetricsConfiguration={
                  'Id': 'string',
                  'Filter': {
                      'Prefix': 'string',
                      'Tag': {
                          'Key': 'string',
                          'Value': 'string'
                      },
                      'And': {
                          'Prefix': 'string',
                          'Tags': [
                              {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                          ]
                      }
                  }
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the bucket for which the metrics configuration is set.
        :type Id: string
        :param Id: **[REQUIRED]**
          The ID used to identify the metrics configuration.
        :type MetricsConfiguration: dict
        :param MetricsConfiguration: **[REQUIRED]**
          Specifies the metrics configuration.
          - **Id** *(string) --* **[REQUIRED]**
            The ID used to identify the metrics configuration.
          - **Filter** *(dict) --*
            Specifies a metrics configuration filter. The metrics configuration will only include objects that meet the filter\'s criteria. A filter must be a prefix, a tag, or a conjunction (MetricsAndOperator).
            - **Prefix** *(string) --*
              The prefix used when evaluating a metrics filter.
            - **Tag** *(dict) --*
              The tag used when evaluating a metrics filter.
              - **Key** *(string) --* **[REQUIRED]**
                Name of the tag.
              - **Value** *(string) --* **[REQUIRED]**
                Value of the tag.
            - **And** *(dict) --*
              A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The operator must have at least two predicates, and an object must match all of the predicates in order for the filter to apply.
              - **Prefix** *(string) --*
                The prefix used when evaluating an AND predicate.
              - **Tags** *(list) --*
                The list of tags used when evaluating an AND predicate.
                - *(dict) --*
                  - **Key** *(string) --* **[REQUIRED]**
                    Name of the tag.
                  - **Value** *(string) --* **[REQUIRED]**
                    Value of the tag.
        :returns: None
        """
        pass

    def put_bucket_notification(
        self,
        Bucket,  # type: str
        NotificationConfiguration,  # type: Dict
    ):
        # type: (...) -> None
        """
        No longer used, see the PutBucketNotificationConfiguration operation.
        .. danger::
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketNotification>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_notification(
              Bucket='string',
              NotificationConfiguration={
                  'TopicConfiguration': {
                      'Id': 'string',
                      'Events': [
                          's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      ],
                      'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      'Topic': 'string'
                  },
                  'QueueConfiguration': {
                      'Id': 'string',
                      'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      'Events': [
                          's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      ],
                      'Queue': 'string'
                  },
                  'CloudFunctionConfiguration': {
                      'Id': 'string',
                      'Event': 's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      'Events': [
                          's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      ],
                      'CloudFunction': 'string',
                      'InvocationRole': 'string'
                  }
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type NotificationConfiguration: dict
        :param NotificationConfiguration: **[REQUIRED]**
          - **TopicConfiguration** *(dict) --*
            - **Id** *(string) --*
              An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
            - **Events** *(list) --*
              - *(string) --*
                The bucket event for which to send notifications.
            - **Event** *(string) --*
              Bucket event for which to send notifications.
            - **Topic** *(string) --*
              Amazon SNS topic to which Amazon S3 will publish a message to report the specified events for the bucket.
          - **QueueConfiguration** *(dict) --*
            - **Id** *(string) --*
              An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
            - **Event** *(string) --*
              The bucket event for which to send notifications.
            - **Events** *(list) --*
              - *(string) --*
                The bucket event for which to send notifications.
            - **Queue** *(string) --*
          - **CloudFunctionConfiguration** *(dict) --*
            - **Id** *(string) --*
              An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
            - **Event** *(string) --*
              The bucket event for which to send notifications.
            - **Events** *(list) --*
              - *(string) --*
                The bucket event for which to send notifications.
            - **CloudFunction** *(string) --*
            - **InvocationRole** *(string) --*
        :returns: None
        """
        pass

    def put_bucket_notification_configuration(
        self,
        Bucket,  # type: str
        NotificationConfiguration,  # type: Dict
    ):
        # type: (...) -> None
        """
        Enables notifications of specified events for a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketNotificationConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_notification_configuration(
              Bucket='string',
              NotificationConfiguration={
                  'TopicConfigurations': [
                      {
                          'Id': 'string',
                          'TopicArn': 'string',
                          'Events': [
                              's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                          ],
                          'Filter': {
                              'Key': {
                                  'FilterRules': [
                                      {
                                          'Name': 'prefix'|'suffix',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          }
                      },
                  ],
                  'QueueConfigurations': [
                      {
                          'Id': 'string',
                          'QueueArn': 'string',
                          'Events': [
                              's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                          ],
                          'Filter': {
                              'Key': {
                                  'FilterRules': [
                                      {
                                          'Name': 'prefix'|'suffix',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          }
                      },
                  ],
                  'LambdaFunctionConfigurations': [
                      {
                          'Id': 'string',
                          'LambdaFunctionArn': 'string',
                          'Events': [
                              's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'|'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'|'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'|'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'|'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                          ],
                          'Filter': {
                              'Key': {
                                  'FilterRules': [
                                      {
                                          'Name': 'prefix'|'suffix',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type NotificationConfiguration: dict
        :param NotificationConfiguration: **[REQUIRED]**
          - **TopicConfigurations** *(list) --*
            The topic to which notifications are sent and the events for which notifications are generated.
            - *(dict) --*
              A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.
              - **Id** *(string) --*
                An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
              - **TopicArn** *(string) --* **[REQUIRED]**
                The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a message when it detects events of the specified type.
              - **Events** *(list) --* **[REQUIRED]**
                The Amazon S3 bucket event about which to send notifications. For more information, see `Supported Event Types <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                - *(string) --*
                  The bucket event for which to send notifications.
              - **Filter** *(dict) --*
                - **Key** *(dict) --*
                  - **FilterRules** *(list) --*
                    - *(dict) --*
                      Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.
                      - **Name** *(string) --*
                        The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see `Configuring Event Notifications <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                      - **Value** *(string) --*
                        The value that the filter searches for in object key names.
          - **QueueConfigurations** *(list) --*
            The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.
            - *(dict) --*
              Specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.
              - **Id** *(string) --*
                An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
              - **QueueArn** *(string) --* **[REQUIRED]**
                The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.
              - **Events** *(list) --* **[REQUIRED]**
                - *(string) --*
                  The bucket event for which to send notifications.
              - **Filter** *(dict) --*
                - **Key** *(dict) --*
                  - **FilterRules** *(list) --*
                    - *(dict) --*
                      Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.
                      - **Name** *(string) --*
                        The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see `Configuring Event Notifications <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                      - **Value** *(string) --*
                        The value that the filter searches for in object key names.
          - **LambdaFunctionConfigurations** *(list) --*
            Describes the AWS Lambda functions to invoke and the events for which to invoke them.
            - *(dict) --*
              A container for specifying the configuration for AWS Lambda notifications.
              - **Id** *(string) --*
                An optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
              - **LambdaFunctionArn** *(string) --* **[REQUIRED]**
                The Amazon Resource Name (ARN) of the AWS Lambda function that Amazon S3 invokes when the specified event type occurs.
              - **Events** *(list) --* **[REQUIRED]**
                The Amazon S3 bucket event for which to invoke the AWS Lambda function. For more information, see `Supported Event Types <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                - *(string) --*
                  The bucket event for which to send notifications.
              - **Filter** *(dict) --*
                - **Key** *(dict) --*
                  - **FilterRules** *(list) --*
                    - *(dict) --*
                      Specifies the Amazon S3 object key name to filter on and whether to filter on the suffix or prefix of the key name.
                      - **Name** *(string) --*
                        The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see `Configuring Event Notifications <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                      - **Value** *(string) --*
                        The value that the filter searches for in object key names.
        :returns: None
        """
        pass

    def put_bucket_policy(
        self,
        Bucket,  # type: str
        Policy,  # type: str
        ConfirmRemoveSelfBucketAccess=None,  # type: Optional[bool]
    ):
        # type: (...) -> None
        """
        Applies an Amazon S3 bucket policy to an Amazon S3 bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketPolicy>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_policy(
              Bucket='string',
              ConfirmRemoveSelfBucketAccess=True|False,
              Policy='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type ConfirmRemoveSelfBucketAccess: boolean
        :param ConfirmRemoveSelfBucketAccess:
          Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.
        :type Policy: string
        :param Policy: **[REQUIRED]**
          The bucket policy as a JSON document.
        :returns: None
        """
        pass

    def put_bucket_replication(
        self,
        Bucket,  # type: str
        ReplicationConfiguration,  # type: Dict
        Token=None,  # type: Optional[str]
    ):
        # type: (...) -> None
        """
        Creates a replication configuration or replaces an existing one. For more information, see `Cross-Region Replication (CRR) <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html>`__ in the *Amazon S3 Developer Guide* . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketReplication>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_replication(
              Bucket='string',
              ReplicationConfiguration={
                  'Role': 'string',
                  'Rules': [
                      {
                          'ID': 'string',
                          'Priority': 123,
                          'Prefix': 'string',
                          'Filter': {
                              'Prefix': 'string',
                              'Tag': {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                              'And': {
                                  'Prefix': 'string',
                                  'Tags': [
                                      {
                                          'Key': 'string',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          },
                          'Status': 'Enabled'|'Disabled',
                          'SourceSelectionCriteria': {
                              'SseKmsEncryptedObjects': {
                                  'Status': 'Enabled'|'Disabled'
                              }
                          },
                          'Destination': {
                              'Bucket': 'string',
                              'Account': 'string',
                              'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                              'AccessControlTranslation': {
                                  'Owner': 'Destination'
                              },
                              'EncryptionConfiguration': {
                                  'ReplicaKmsKeyID': 'string'
                              }
                          },
                          'DeleteMarkerReplication': {
                              'Status': 'Enabled'|'Disabled'
                          }
                      },
                  ]
              },
              Token='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type ReplicationConfiguration: dict
        :param ReplicationConfiguration: **[REQUIRED]**
          - **Role** *(string) --* **[REQUIRED]**
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon S3 assumes when replicating objects. For more information, see `How to Set Up Cross-Region Replication <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-how-setup.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
          - **Rules** *(list) --* **[REQUIRED]**
            A container for one or more replication rules. A replication configuration must have at least one rule and can contain a maximum of 1,000 rules.
            - *(dict) --*
              Specifies which Amazon S3 objects to replicate and where to store the replicas.
              - **ID** *(string) --*
                A unique identifier for the rule. The maximum value is 255 characters.
              - **Priority** *(integer) --*
                The priority associated with the rule. If you specify multiple rules in a replication configuration, Amazon S3 prioritizes the rules to prevent conflicts when filtering. If two or more rules identify the same object based on a specified filter, the rule with higher priority takes precedence. For example:
                * Same object quality prefix based filter criteria If prefixes you specified in multiple rules overlap
                * Same object qualify tag based filter criteria specified in multiple rules
                For more information, see `Cross-Region Replication (CRR) <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html>`__ in the *Amazon S3 Developer Guide* .
              - **Prefix** *(string) --*
                An object keyname prefix that identifies the object or objects to which the rule applies. The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string.
              - **Filter** *(dict) --*
                - **Prefix** *(string) --*
                  An object keyname prefix that identifies the subset of objects to which the rule applies.
                - **Tag** *(dict) --*
                  A container for specifying a tag key and value.
                  The rule applies only to objects that have the tag in their tag set.
                  - **Key** *(string) --* **[REQUIRED]**
                    Name of the tag.
                  - **Value** *(string) --* **[REQUIRED]**
                    Value of the tag.
                - **And** *(dict) --*
                  A container for specifying rule filters. The filters determine the subset of objects to which the rule applies. This element is required only if you specify more than one filter. For example:
                  * If you specify both a ``Prefix`` and a ``Tag`` filter, wrap these filters in an ``And`` tag.
                  * If you specify a filter based on multiple tags, wrap the ``Tag`` elements in an ``And`` tag.
                  - **Prefix** *(string) --*
                  - **Tags** *(list) --*
                    - *(dict) --*
                      - **Key** *(string) --* **[REQUIRED]**
                        Name of the tag.
                      - **Value** *(string) --* **[REQUIRED]**
                        Value of the tag.
              - **Status** *(string) --* **[REQUIRED]**
                Specifies whether the rule is enabled.
              - **SourceSelectionCriteria** *(dict) --*
                A container that describes additional filters for identifying the source objects that you want to replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3 supports only the filter that you can specify for objects created with server-side encryption using an AWS KMS-Managed Key (SSE-KMS).
                - **SseKmsEncryptedObjects** *(dict) --*
                  A container for filter information for the selection of Amazon S3 objects encrypted with AWS KMS. If you include ``SourceSelectionCriteria`` in the replication configuration, this element is required.
                  - **Status** *(string) --* **[REQUIRED]**
                    Specifies whether Amazon S3 replicates objects created with server-side encryption using an AWS KMS-managed key.
              - **Destination** *(dict) --* **[REQUIRED]**
                A container for information about the replication destination.
                - **Bucket** *(string) --* **[REQUIRED]**
                  The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store replicas of the object identified by the rule.
                  A replication configuration can replicate objects to only one destination bucket. If there are multiple rules in your replication configuration, all rules must specify the same destination bucket.
                - **Account** *(string) --*
                  Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3 to change replica ownership to the AWS account that owns the destination bucket by specifying the ``AccessControlTranslation`` property, this is the account ID of the destination bucket owner. For more information, see `Cross-Region Replication Additional Configuration\: Change Replica Owner <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-change-owner.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
                - **StorageClass** *(string) --*
                  The storage class to use when replicating objects, such as standard or reduced redundancy. By default, Amazon S3 uses the storage class of the source object to create the object replica.
                  For valid values, see the ``StorageClass`` element of the `PUT Bucket replication <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__ action in the *Amazon Simple Storage Service API Reference* .
                - **AccessControlTranslation** *(dict) --*
                  Specify this only in a cross-account scenario (where source and destination bucket owners are not the same), and you want to change replica ownership to the AWS account that owns the destination bucket. If this is not specified in the replication configuration, the replicas are owned by same AWS account that owns the source object.
                  - **Owner** *(string) --* **[REQUIRED]**
                    Specifies the replica ownership. For default and valid values, see `PUT bucket replication <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__ in the *Amazon Simple Storage Service API Reference* .
                - **EncryptionConfiguration** *(dict) --*
                  A container that provides information about encryption. If ``SourceSelectionCriteria`` is specified, you must specify this element.
                  - **ReplicaKmsKeyID** *(string) --*
                    Specifies the AWS KMS Key ID (Key ARN or Alias ARN) for the destination bucket. Amazon S3 uses this key to encrypt replica objects.
              - **DeleteMarkerReplication** *(dict) --*
                - **Status** *(string) --*
                  The status of the delete marker replication.
                  .. note::
                    In the current implementation, Amazon S3 doesn\'t replicate the delete markers. The status must be ``Disabled`` .
        :type Token: string
        :param Token:
          A token that allows Amazon S3 object lock to be enabled for an existing bucket.
        :returns: None
        """
        pass

    def put_bucket_request_payment(
        self,
        Bucket,  # type: str
        RequestPaymentConfiguration,  # type: Dict
    ):
        # type: (...) -> None
        """
        Sets the request payment configuration for a bucket. By default, the bucket owner pays for downloads from the bucket. This configuration parameter enables the bucket owner (only) to specify that the person requesting the download will be charged for the download. Documentation on requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketRequestPayment>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_request_payment(
              Bucket='string',
              RequestPaymentConfiguration={
                  'Payer': 'Requester'|'BucketOwner'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type RequestPaymentConfiguration: dict
        :param RequestPaymentConfiguration: **[REQUIRED]**
          - **Payer** *(string) --* **[REQUIRED]**
            Specifies who pays for the download and request fees.
        :returns: None
        """
        pass

    def put_bucket_tagging(
        self,
        Bucket,  # type: str
        Tagging,  # type: Dict
    ):
        # type: (...) -> None
        """
        Sets the tags for a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketTagging>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_tagging(
              Bucket='string',
              Tagging={
                  'TagSet': [
                      {
                          'Key': 'string',
                          'Value': 'string'
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Tagging: dict
        :param Tagging: **[REQUIRED]**
          - **TagSet** *(list) --* **[REQUIRED]**
            - *(dict) --*
              - **Key** *(string) --* **[REQUIRED]**
                Name of the tag.
              - **Value** *(string) --* **[REQUIRED]**
                Value of the tag.
        :returns: None
        """
        pass

    def put_bucket_versioning(
        self,
        Bucket,  # type: str
        VersioningConfiguration,  # type: Dict
        MFA=None,  # type: Optional[str]
    ):
        # type: (...) -> None
        """
        Sets the versioning state of an existing bucket. To set the versioning state, you must be the bucket owner.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketVersioning>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_versioning(
              Bucket='string',
              MFA='string',
              VersioningConfiguration={
                  'MFADelete': 'Enabled'|'Disabled',
                  'Status': 'Enabled'|'Suspended'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type MFA: string
        :param MFA:
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        :type VersioningConfiguration: dict
        :param VersioningConfiguration: **[REQUIRED]**
          - **MFADelete** *(string) --*
            Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.
          - **Status** *(string) --*
            The versioning state of the bucket.
        :returns: None
        """
        pass

    def put_bucket_website(
        self,
        Bucket,  # type: str
        WebsiteConfiguration,  # type: Dict
    ):
        # type: (...) -> None
        """
        Set the website configuration for a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketWebsite>`_
        
        **Request Syntax**
        ::
          response = client.put_bucket_website(
              Bucket='string',
              WebsiteConfiguration={
                  'ErrorDocument': {
                      'Key': 'string'
                  },
                  'IndexDocument': {
                      'Suffix': 'string'
                  },
                  'RedirectAllRequestsTo': {
                      'HostName': 'string',
                      'Protocol': 'http'|'https'
                  },
                  'RoutingRules': [
                      {
                          'Condition': {
                              'HttpErrorCodeReturnedEquals': 'string',
                              'KeyPrefixEquals': 'string'
                          },
                          'Redirect': {
                              'HostName': 'string',
                              'HttpRedirectCode': 'string',
                              'Protocol': 'http'|'https',
                              'ReplaceKeyPrefixWith': 'string',
                              'ReplaceKeyWith': 'string'
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type WebsiteConfiguration: dict
        :param WebsiteConfiguration: **[REQUIRED]**
          - **ErrorDocument** *(dict) --*
            The name of the error document for the website.
            - **Key** *(string) --* **[REQUIRED]**
              The object key name to use when a 4XX class error occurs.
          - **IndexDocument** *(dict) --*
            The name of the index document for the website.
            - **Suffix** *(string) --* **[REQUIRED]**
              A suffix that is appended to a request that is for a directory on the website endpoint (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html) The suffix must not be empty and must not include a slash character.
          - **RedirectAllRequestsTo** *(dict) --*
            The redirect behavior for every request to this bucket\'s website endpoint.
            .. warning::
              If you specify this property, you can\'t specify any other property.
            - **HostName** *(string) --* **[REQUIRED]**
              Name of the host where requests are redirected.
            - **Protocol** *(string) --*
              Protocol to use when redirecting requests. The default is the protocol that is used in the original request.
          - **RoutingRules** *(list) --*
            Rules that define when a redirect is applied and the redirect behavior.
            - *(dict) --*
              Specifies the redirect behavior and when a redirect is applied.
              - **Condition** *(dict) --*
                A container for describing a condition that must be met for the specified redirect to apply. For example, 1. If request is for pages in the ``/docs`` folder, redirect to the ``/documents`` folder. 2. If request results in HTTP error 4xx, redirect request to another host where you might process the error.
                - **HttpErrorCodeReturnedEquals** *(string) --*
                  The HTTP error code when the redirect is applied. In the event of an error, if the error code equals this value, then the specified redirect is applied. Required when parent element ``Condition`` is specified and sibling ``KeyPrefixEquals`` is not specified. If both are specified, then both must be true for the redirect to be applied.
                - **KeyPrefixEquals** *(string) --*
                  The object key name prefix when the redirect is applied. For example, to redirect requests for ``ExamplePage.html`` , the key prefix will be ``ExamplePage.html`` . To redirect request for all pages with the prefix ``docs/`` , the key prefix will be ``/docs`` , which identifies all objects in the docs/ folder. Required when the parent element ``Condition`` is specified and sibling ``HttpErrorCodeReturnedEquals`` is not specified. If both conditions are specified, both must be true for the redirect to be applied.
              - **Redirect** *(dict) --* **[REQUIRED]**
                Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can specify a different error code to return.
                - **HostName** *(string) --*
                  The host name to use in the redirect request.
                - **HttpRedirectCode** *(string) --*
                  The HTTP redirect code to use on the response. Not required if one of the siblings is present.
                - **Protocol** *(string) --*
                  Protocol to use when redirecting requests. The default is the protocol that is used in the original request.
                - **ReplaceKeyPrefixWith** *(string) --*
                  The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix ``docs/`` (objects in the ``docs/`` folder) to ``documents/`` , you can set a condition block with ``KeyPrefixEquals`` set to ``docs/`` and in the Redirect set ``ReplaceKeyPrefixWith`` to ``/documents`` . Not required if one of the siblings is present. Can be present only if ``ReplaceKeyWith`` is not provided.
                - **ReplaceKeyWith** *(string) --*
                  The specific object key to use in the redirect request. For example, redirect request to ``error.html`` . Not required if one of the siblings is present. Can be present only if ``ReplaceKeyPrefixWith`` is not provided.
        :returns: None
        """
        pass

    def put_object(
        self,
        Bucket,  # type: str
        Key,  # type: str
        ACL=None,  # type: Optional[str]
        Body=None,  # type: Optional[Union[Optional[bytes], Optional[IO]]]
        CacheControl=None,  # type: Optional[str]
        ContentDisposition=None,  # type: Optional[str]
        ContentEncoding=None,  # type: Optional[str]
        ContentLanguage=None,  # type: Optional[str]
        ContentLength=None,  # type: Optional[int]
        ContentMD5=None,  # type: Optional[str]
        ContentType=None,  # type: Optional[str]
        Expires=None,  # type: Optional[datetime]
        GrantFullControl=None,  # type: Optional[str]
        GrantRead=None,  # type: Optional[str]
        GrantReadACP=None,  # type: Optional[str]
        GrantWriteACP=None,  # type: Optional[str]
        Metadata=None,  # type: Optional[Dict]
        ServerSideEncryption=None,  # type: Optional[str]
        StorageClass=None,  # type: Optional[str]
        WebsiteRedirectLocation=None,  # type: Optional[str]
        SSECustomerAlgorithm=None,  # type: Optional[str]
        SSECustomerKey=None,  # type: Optional[str]
        SSECustomerKeyMD5=None,  # type: Optional[str]
        SSEKMSKeyId=None,  # type: Optional[str]
        SSEKMSEncryptionContext=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
        Tagging=None,  # type: Optional[str]
        ObjectLockMode=None,  # type: Optional[str]
        ObjectLockRetainUntilDate=None,  # type: Optional[datetime]
        ObjectLockLegalHoldStatus=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Adds an object to a bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObject>`_
        
        **Request Syntax**
        ::
          response = client.put_object(
              ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
              Body=b'bytes'|file,
              Bucket='string',
              CacheControl='string',
              ContentDisposition='string',
              ContentEncoding='string',
              ContentLanguage='string',
              ContentLength=123,
              ContentMD5='string',
              ContentType='string',
              Expires=datetime(2015, 1, 1),
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWriteACP='string',
              Key='string',
              Metadata={
                  'string': 'string'
              },
              ServerSideEncryption='AES256'|'aws:kms',
              StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
              WebsiteRedirectLocation='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              SSEKMSKeyId='string',
              SSEKMSEncryptionContext='string',
              RequestPayer='requester',
              Tagging='string',
              ObjectLockMode='GOVERNANCE'|'COMPLIANCE',
              ObjectLockRetainUntilDate=datetime(2015, 1, 1),
              ObjectLockLegalHoldStatus='ON'|'OFF'
          )
        
        **Response Syntax**
        ::
            {
                'Expiration': 'string',
                'ETag': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'VersionId': 'string',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'SSEKMSEncryptionContext': 'string',
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Expiration** *(string) --* 
              If the object expiration is configured, this will contain the expiration date (expiry-date) and rule ID (rule-id). The value of rule-id is URL encoded.
            - **ETag** *(string) --* 
              Entity tag for the uploaded object.
            - **ServerSideEncryption** *(string) --* 
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
            - **VersionId** *(string) --* 
              Version of the object.
            - **SSECustomerAlgorithm** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
            - **SSECustomerKeyMD5** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
            - **SSEKMSKeyId** *(string) --* 
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
            - **SSEKMSEncryptionContext** *(string) --* 
              If present, specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type ACL: string
        :param ACL:
          The canned ACL to apply to the object.
        :type Body: bytes or seekable file-like object
        :param Body:
          Object data.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          Name of the bucket to which the PUT operation was initiated.
        :type CacheControl: string
        :param CacheControl:
          Specifies caching behavior along the request/reply chain.
        :type ContentDisposition: string
        :param ContentDisposition:
          Specifies presentational information for the object.
        :type ContentEncoding: string
        :param ContentEncoding:
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        :type ContentLanguage: string
        :param ContentLanguage:
          The language the content is in.
        :type ContentLength: integer
        :param ContentLength:
          Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.
        :type ContentMD5: string
        :param ContentMD5:
          The base64-encoded 128-bit MD5 digest of the part data. This parameter is auto-populated when using the command from the CLI. This parameted is required if object lock parameters are specified.
        :type ContentType: string
        :param ContentType:
          A standard MIME type describing the format of the object data.
        :type Expires: datetime
        :param Expires:
          The date and time at which the object is no longer cacheable.
        :type GrantFullControl: string
        :param GrantFullControl:
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        :type GrantRead: string
        :param GrantRead:
          Allows grantee to read the object data and its metadata.
        :type GrantReadACP: string
        :param GrantReadACP:
          Allows grantee to read the object ACL.
        :type GrantWriteACP: string
        :param GrantWriteACP:
          Allows grantee to write the ACL for the applicable object.
        :type Key: string
        :param Key: **[REQUIRED]**
          Object key for which the PUT operation was initiated.
        :type Metadata: dict
        :param Metadata:
          A map of metadata to store with the object in S3.
          - *(string) --*
            - *(string) --*
        :type ServerSideEncryption: string
        :param ServerSideEncryption:
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        :type StorageClass: string
        :param StorageClass:
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation:
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        :type SSECustomerKey: string
        :param SSECustomerKey:
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId:
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        :type SSEKMSEncryptionContext: string
        :param SSEKMSEncryptionContext:
          Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type Tagging: string
        :param Tagging:
          The tag-set for the object. The tag-set must be encoded as URL Query parameters. (For example, \"Key1=Value1\")
        :type ObjectLockMode: string
        :param ObjectLockMode:
          The object lock mode that you want to apply to this object.
        :type ObjectLockRetainUntilDate: datetime
        :param ObjectLockRetainUntilDate:
          The date and time when you want this object\'s object lock to expire.
        :type ObjectLockLegalHoldStatus: string
        :param ObjectLockLegalHoldStatus:
          The Legal Hold status that you want to apply to the specified object.
        :rtype: dict
        :returns:
        """
        pass

    def put_object_acl(
        self,
        Bucket,  # type: str
        Key,  # type: str
        ACL=None,  # type: Optional[str]
        AccessControlPolicy=None,  # type: Optional[Dict]
        GrantFullControl=None,  # type: Optional[str]
        GrantRead=None,  # type: Optional[str]
        GrantReadACP=None,  # type: Optional[str]
        GrantWrite=None,  # type: Optional[str]
        GrantWriteACP=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
        VersionId=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        uses the acl subresource to set the access control list (ACL) permissions for an object that already exists in a bucket
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectAcl>`_
        
        **Request Syntax**
        ::
          response = client.put_object_acl(
              ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
              AccessControlPolicy={
                  'Grants': [
                      {
                          'Grantee': {
                              'DisplayName': 'string',
                              'EmailAddress': 'string',
                              'ID': 'string',
                              'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                              'URI': 'string'
                          },
                          'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                      },
                  ],
                  'Owner': {
                      'DisplayName': 'string',
                      'ID': 'string'
                  }
              },
              Bucket='string',
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWrite='string',
              GrantWriteACP='string',
              Key='string',
              RequestPayer='requester',
              VersionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type ACL: string
        :param ACL:
          The canned ACL to apply to the object.
        :type AccessControlPolicy: dict
        :param AccessControlPolicy:
          Contains the elements that set the ACL permissions for an object per grantee.
          - **Grants** *(list) --*
            A list of grants.
            - *(dict) --*
              - **Grantee** *(dict) --*
                - **DisplayName** *(string) --*
                  Screen name of the grantee.
                - **EmailAddress** *(string) --*
                  Email address of the grantee.
                - **ID** *(string) --*
                  The canonical user ID of the grantee.
                - **Type** *(string) --* **[REQUIRED]**
                  Type of grantee
                - **URI** *(string) --*
                  URI of the grantee group.
              - **Permission** *(string) --*
                Specifies the permission given to the grantee.
          - **Owner** *(dict) --*
            Container for the bucket owner\'s display name and ID.
            - **DisplayName** *(string) --*
            - **ID** *(string) --*
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type GrantFullControl: string
        :param GrantFullControl:
          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
        :type GrantRead: string
        :param GrantRead:
          Allows grantee to list the objects in the bucket.
        :type GrantReadACP: string
        :param GrantReadACP:
          Allows grantee to read the bucket ACL.
        :type GrantWrite: string
        :param GrantWrite:
          Allows grantee to create, overwrite, and delete any object in the bucket.
        :type GrantWriteACP: string
        :param GrantWriteACP:
          Allows grantee to write the ACL for the applicable bucket.
        :type Key: string
        :param Key: **[REQUIRED]**
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type VersionId: string
        :param VersionId:
          VersionId used to reference a specific version of the object.
        :rtype: dict
        :returns:
        """
        pass

    def put_object_legal_hold(
        self,
        Bucket,  # type: str
        Key,  # type: str
        LegalHold=None,  # type: Optional[Dict]
        RequestPayer=None,  # type: Optional[str]
        VersionId=None,  # type: Optional[str]
        ContentMD5=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Applies a Legal Hold configuration to the specified object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectLegalHold>`_
        
        **Request Syntax**
        ::
          response = client.put_object_legal_hold(
              Bucket='string',
              Key='string',
              LegalHold={
                  'Status': 'ON'|'OFF'
              },
              RequestPayer='requester',
              VersionId='string',
              ContentMD5='string'
          )
        
        **Response Syntax**
        ::
            {
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The bucket containing the object that you want to place a Legal Hold on.
        :type Key: string
        :param Key: **[REQUIRED]**
          The key name for the object that you want to place a Legal Hold on.
        :type LegalHold: dict
        :param LegalHold:
          Container element for the Legal Hold configuration you want to apply to the specified object.
          - **Status** *(string) --*
            Indicates whether the specified object has a Legal Hold in place.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type VersionId: string
        :param VersionId:
          The version ID of the object that you want to place a Legal Hold on.
        :type ContentMD5: string
        :param ContentMD5:
          The MD5 hash for the request body.
        :rtype: dict
        :returns:
        """
        pass

    def put_object_lock_configuration(
        self,
        Bucket,  # type: str
        ObjectLockConfiguration=None,  # type: Optional[Dict]
        RequestPayer=None,  # type: Optional[str]
        Token=None,  # type: Optional[str]
        ContentMD5=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Places an object lock configuration on the specified bucket. The rule specified in the object lock configuration will be applied by default to every new object placed in the specified bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectLockConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_object_lock_configuration(
              Bucket='string',
              ObjectLockConfiguration={
                  'ObjectLockEnabled': 'Enabled',
                  'Rule': {
                      'DefaultRetention': {
                          'Mode': 'GOVERNANCE'|'COMPLIANCE',
                          'Days': 123,
                          'Years': 123
                      }
                  }
              },
              RequestPayer='requester',
              Token='string',
              ContentMD5='string'
          )
        
        **Response Syntax**
        ::
            {
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The bucket whose object lock configuration you want to create or replace.
        :type ObjectLockConfiguration: dict
        :param ObjectLockConfiguration:
          The object lock configuration that you want to apply to the specified bucket.
          - **ObjectLockEnabled** *(string) --*
            Indicates whether this bucket has an object lock configuration enabled.
          - **Rule** *(dict) --*
            The object lock rule in place for the specified object.
            - **DefaultRetention** *(dict) --*
              The default retention period that you want to apply to new objects placed in the specified bucket.
              - **Mode** *(string) --*
                The default object lock retention mode you want to apply to new objects placed in the specified bucket.
              - **Days** *(integer) --*
                The number of days that you want to specify for the default retention period.
              - **Years** *(integer) --*
                The number of years that you want to specify for the default retention period.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type Token: string
        :param Token:
          A token to allow Amazon S3 object lock to be enabled for an existing bucket.
        :type ContentMD5: string
        :param ContentMD5:
          The MD5 hash for the request body.
        :rtype: dict
        :returns:
        """
        pass

    def put_object_retention(
        self,
        Bucket,  # type: str
        Key,  # type: str
        Retention=None,  # type: Optional[Dict]
        RequestPayer=None,  # type: Optional[str]
        VersionId=None,  # type: Optional[str]
        BypassGovernanceRetention=None,  # type: Optional[bool]
        ContentMD5=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Places an Object Retention configuration on an object.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectRetention>`_
        
        **Request Syntax**
        ::
          response = client.put_object_retention(
              Bucket='string',
              Key='string',
              Retention={
                  'Mode': 'GOVERNANCE'|'COMPLIANCE',
                  'RetainUntilDate': datetime(2015, 1, 1)
              },
              RequestPayer='requester',
              VersionId='string',
              BypassGovernanceRetention=True|False,
              ContentMD5='string'
          )
        
        **Response Syntax**
        ::
            {
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The bucket that contains the object you want to apply this Object Retention configuration to.
        :type Key: string
        :param Key: **[REQUIRED]**
          The key name for the object that you want to apply this Object Retention configuration to.
        :type Retention: dict
        :param Retention:
          The container element for the Object Retention configuration.
          - **Mode** *(string) --*
            Indicates the Retention mode for the specified object.
          - **RetainUntilDate** *(datetime) --*
            The date on which this object lock retention expires.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :type VersionId: string
        :param VersionId:
          The version ID for the object that you want to apply this Object Retention configuration to.
        :type BypassGovernanceRetention: boolean
        :param BypassGovernanceRetention:
          Indicates whether this operation should bypass Governance-mode restrictions.j
        :type ContentMD5: string
        :param ContentMD5:
          The MD5 hash for the request body.
        :rtype: dict
        :returns:
        """
        pass

    def put_object_tagging(
        self,
        Bucket,  # type: str
        Key,  # type: str
        Tagging,  # type: Dict
        VersionId=None,  # type: Optional[str]
        ContentMD5=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Sets the supplied tag-set to an object that already exists in a bucket
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectTagging>`_
        
        **Request Syntax**
        ::
          response = client.put_object_tagging(
              Bucket='string',
              Key='string',
              VersionId='string',
              ContentMD5='string',
              Tagging={
                  'TagSet': [
                      {
                          'Key': 'string',
                          'Value': 'string'
                      },
                  ]
              }
          )
        
        **Response Syntax**
        ::
            {
                'VersionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VersionId** *(string) --* 
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Key: string
        :param Key: **[REQUIRED]**
        :type VersionId: string
        :param VersionId:
        :type ContentMD5: string
        :param ContentMD5:
        :type Tagging: dict
        :param Tagging: **[REQUIRED]**
          - **TagSet** *(list) --* **[REQUIRED]**
            - *(dict) --*
              - **Key** *(string) --* **[REQUIRED]**
                Name of the tag.
              - **Value** *(string) --* **[REQUIRED]**
                Value of the tag.
        :rtype: dict
        :returns:
        """
        pass

    def put_public_access_block(
        self,
        Bucket,  # type: str
        PublicAccessBlockConfiguration,  # type: Dict
        ContentMD5=None,  # type: Optional[str]
    ):
        # type: (...) -> None
        """
        Creates or modifies the ``PublicAccessBlock`` configuration for an Amazon S3 bucket.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutPublicAccessBlock>`_
        
        **Request Syntax**
        ::
          response = client.put_public_access_block(
              Bucket='string',
              ContentMD5='string',
              PublicAccessBlockConfiguration={
                  'BlockPublicAcls': True|False,
                  'IgnorePublicAcls': True|False,
                  'BlockPublicPolicy': True|False,
                  'RestrictPublicBuckets': True|False
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The name of the Amazon S3 bucket whose ``PublicAccessBlock`` configuration you want to set.
        :type ContentMD5: string
        :param ContentMD5:
          The MD5 hash of the ``PutPublicAccessBlock`` request body.
        :type PublicAccessBlockConfiguration: dict
        :param PublicAccessBlockConfiguration: **[REQUIRED]**
          The ``PublicAccessBlock`` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see `The Meaning of \"Public\" <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`__ in the *Amazon Simple Storage Service Developer Guide* .
          - **BlockPublicAcls** *(boolean) --*
            Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and objects in this bucket. Setting this element to ``TRUE`` causes the following behavior:
            * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
            * PUT Object calls fail if the request includes a public ACL.
            Enabling this setting doesn\'t affect existing policies or ACLs.
          - **IgnorePublicAcls** *(boolean) --*
            Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on this bucket and objects in this bucket.
            Enabling this setting doesn\'t affect the persistence of any existing ACLs and doesn\'t prevent new public ACLs from being set.
          - **BlockPublicPolicy** *(boolean) --*
            Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
            Enabling this setting doesn\'t affect existing bucket policies.
          - **RestrictPublicBuckets** *(boolean) --*
            Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to ``TRUE`` restricts access to this bucket to only AWS services and authorized users within this account if the bucket has a public policy.
            Enabling this setting doesn\'t affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.
        :returns: None
        """
        pass

    def restore_object(
        self,
        Bucket,  # type: str
        Key,  # type: str
        VersionId=None,  # type: Optional[str]
        RestoreRequest=None,  # type: Optional[Dict]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Restores an archived copy of an object back into Amazon S3
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/RestoreObject>`_
        
        **Request Syntax**
        ::
          response = client.restore_object(
              Bucket='string',
              Key='string',
              VersionId='string',
              RestoreRequest={
                  'Days': 123,
                  'GlacierJobParameters': {
                      'Tier': 'Standard'|'Bulk'|'Expedited'
                  },
                  'Type': 'SELECT',
                  'Tier': 'Standard'|'Bulk'|'Expedited',
                  'Description': 'string',
                  'SelectParameters': {
                      'InputSerialization': {
                          'CSV': {
                              'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                              'Comments': 'string',
                              'QuoteEscapeCharacter': 'string',
                              'RecordDelimiter': 'string',
                              'FieldDelimiter': 'string',
                              'QuoteCharacter': 'string',
                              'AllowQuotedRecordDelimiter': True|False
                          },
                          'CompressionType': 'NONE'|'GZIP'|'BZIP2',
                          'JSON': {
                              'Type': 'DOCUMENT'|'LINES'
                          },
                          'Parquet': {}
                      },
                      'ExpressionType': 'SQL',
                      'Expression': 'string',
                      'OutputSerialization': {
                          'CSV': {
                              'QuoteFields': 'ALWAYS'|'ASNEEDED',
                              'QuoteEscapeCharacter': 'string',
                              'RecordDelimiter': 'string',
                              'FieldDelimiter': 'string',
                              'QuoteCharacter': 'string'
                          },
                          'JSON': {
                              'RecordDelimiter': 'string'
                          }
                      }
                  },
                  'OutputLocation': {
                      'S3': {
                          'BucketName': 'string',
                          'Prefix': 'string',
                          'Encryption': {
                              'EncryptionType': 'AES256'|'aws:kms',
                              'KMSKeyId': 'string',
                              'KMSContext': 'string'
                          },
                          'CannedACL': 'private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
                          'AccessControlList': [
                              {
                                  'Grantee': {
                                      'DisplayName': 'string',
                                      'EmailAddress': 'string',
                                      'ID': 'string',
                                      'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                                      'URI': 'string'
                                  },
                                  'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                              },
                          ],
                          'Tagging': {
                              'TagSet': [
                                  {
                                      'Key': 'string',
                                      'Value': 'string'
                                  },
                              ]
                          },
                          'UserMetadata': [
                              {
                                  'Name': 'string',
                                  'Value': 'string'
                              },
                          ],
                          'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE'
                      }
                  }
              },
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'RequestCharged': 'requester',
                'RestoreOutputPath': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
            - **RestoreOutputPath** *(string) --* 
              Indicates the path in the provided S3 output location where Select results will be restored to.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type Key: string
        :param Key: **[REQUIRED]**
        :type VersionId: string
        :param VersionId:
        :type RestoreRequest: dict
        :param RestoreRequest:
          - **Days** *(integer) --*
            Lifetime of the active copy in days. Do not use with restores that specify OutputLocation.
          - **GlacierJobParameters** *(dict) --*
            Glacier related parameters pertaining to this job. Do not use with restores that specify OutputLocation.
            - **Tier** *(string) --* **[REQUIRED]**
              Glacier retrieval tier at which the restore will be processed.
          - **Type** *(string) --*
            Type of restore request.
          - **Tier** *(string) --*
            Glacier retrieval tier at which the restore will be processed.
          - **Description** *(string) --*
            The optional description for the job.
          - **SelectParameters** *(dict) --*
            Describes the parameters for Select job types.
            - **InputSerialization** *(dict) --* **[REQUIRED]**
              Describes the serialization format of the object.
              - **CSV** *(dict) --*
                Describes the serialization of a CSV-encoded object.
                - **FileHeaderInfo** *(string) --*
                  Describes the first line of input. Valid values: None, Ignore, Use.
                - **Comments** *(string) --*
                  The single character used to indicate a row should be ignored when present at the start of a row.
                - **QuoteEscapeCharacter** *(string) --*
                  The single character used for escaping the quote character inside an already escaped value.
                - **RecordDelimiter** *(string) --*
                  The value used to separate individual records.
                - **FieldDelimiter** *(string) --*
                  The value used to separate individual fields in a record.
                - **QuoteCharacter** *(string) --*
                  Value used for escaping where the field delimiter is part of the value.
                - **AllowQuotedRecordDelimiter** *(boolean) --*
                  Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.
              - **CompressionType** *(string) --*
                Specifies object\'s compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.
              - **JSON** *(dict) --*
                Specifies JSON as object\'s input serialization format.
                - **Type** *(string) --*
                  The type of JSON. Valid values: Document, Lines.
              - **Parquet** *(dict) --*
                Specifies Parquet as object\'s input serialization format.
            - **ExpressionType** *(string) --* **[REQUIRED]**
              The type of the provided expression (e.g., SQL).
            - **Expression** *(string) --* **[REQUIRED]**
              The expression that is used to query the object.
            - **OutputSerialization** *(dict) --* **[REQUIRED]**
              Describes how the results of the Select job are serialized.
              - **CSV** *(dict) --*
                Describes the serialization of CSV-encoded Select results.
                - **QuoteFields** *(string) --*
                  Indicates whether or not all output fields should be quoted.
                - **QuoteEscapeCharacter** *(string) --*
                  Th single character used for escaping the quote character inside an already escaped value.
                - **RecordDelimiter** *(string) --*
                  The value used to separate individual records.
                - **FieldDelimiter** *(string) --*
                  The value used to separate individual fields in a record.
                - **QuoteCharacter** *(string) --*
                  The value used for escaping where the field delimiter is part of the value.
              - **JSON** *(dict) --*
                Specifies JSON as request\'s output serialization format.
                - **RecordDelimiter** *(string) --*
                  The value used to separate individual records in the output.
          - **OutputLocation** *(dict) --*
            Describes the location where the restore job\'s output is stored.
            - **S3** *(dict) --*
              Describes an S3 location that will receive the results of the restore request.
              - **BucketName** *(string) --* **[REQUIRED]**
                The name of the bucket where the restore results will be placed.
              - **Prefix** *(string) --* **[REQUIRED]**
                The prefix that is prepended to the restore results for this request.
              - **Encryption** *(dict) --*
                - **EncryptionType** *(string) --* **[REQUIRED]**
                  The server-side encryption algorithm used when storing job results in Amazon S3 (e.g., AES256, aws:kms).
                - **KMSKeyId** *(string) --*
                  If the encryption type is aws:kms, this optional value specifies the AWS KMS key ID to use for encryption of job results.
                - **KMSContext** *(string) --*
                  If the encryption type is aws:kms, this optional value can be used to specify the encryption context for the restore results.
              - **CannedACL** *(string) --*
                The canned ACL to apply to the restore results.
              - **AccessControlList** *(list) --*
                A list of grants that control access to the staged results.
                - *(dict) --*
                  - **Grantee** *(dict) --*
                    - **DisplayName** *(string) --*
                      Screen name of the grantee.
                    - **EmailAddress** *(string) --*
                      Email address of the grantee.
                    - **ID** *(string) --*
                      The canonical user ID of the grantee.
                    - **Type** *(string) --* **[REQUIRED]**
                      Type of grantee
                    - **URI** *(string) --*
                      URI of the grantee group.
                  - **Permission** *(string) --*
                    Specifies the permission given to the grantee.
              - **Tagging** *(dict) --*
                The tag-set that is applied to the restore results.
                - **TagSet** *(list) --* **[REQUIRED]**
                  - *(dict) --*
                    - **Key** *(string) --* **[REQUIRED]**
                      Name of the tag.
                    - **Value** *(string) --* **[REQUIRED]**
                      Value of the tag.
              - **UserMetadata** *(list) --*
                A list of metadata to store with the restore results in S3.
                - *(dict) --*
                  A metadata key-value pair to store with an object.
                  - **Name** *(string) --*
                  - **Value** *(string) --*
              - **StorageClass** *(string) --*
                The class of storage used to store the restore results.
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass

    def select_object_content(
        self,
        Bucket,  # type: str
        Key,  # type: str
        Expression,  # type: str
        ExpressionType,  # type: str
        InputSerialization,  # type: Dict
        OutputSerialization,  # type: Dict
        SSECustomerAlgorithm=None,  # type: Optional[str]
        SSECustomerKey=None,  # type: Optional[str]
        SSECustomerKeyMD5=None,  # type: Optional[str]
        RequestProgress=None,  # type: Optional[Dict]
    ):
        # type: (...) -> Dict
        """
        This operation filters the contents of an Amazon S3 object based on a simple Structured Query Language (SQL) statement. In the request, along with the SQL expression, you must also specify a data serialization format (JSON or CSV) of the object. Amazon S3 uses this to parse object data into records, and returns only records that match the specified SQL expression. You must also specify the data serialization format for the response.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/SelectObjectContent>`_
        
        **Request Syntax**
        ::
          response = client.select_object_content(
              Bucket='string',
              Key='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              Expression='string',
              ExpressionType='SQL',
              RequestProgress={
                  'Enabled': True|False
              },
              InputSerialization={
                  'CSV': {
                      'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                      'Comments': 'string',
                      'QuoteEscapeCharacter': 'string',
                      'RecordDelimiter': 'string',
                      'FieldDelimiter': 'string',
                      'QuoteCharacter': 'string',
                      'AllowQuotedRecordDelimiter': True|False
                  },
                  'CompressionType': 'NONE'|'GZIP'|'BZIP2',
                  'JSON': {
                      'Type': 'DOCUMENT'|'LINES'
                  },
                  'Parquet': {}
              },
              OutputSerialization={
                  'CSV': {
                      'QuoteFields': 'ALWAYS'|'ASNEEDED',
                      'QuoteEscapeCharacter': 'string',
                      'RecordDelimiter': 'string',
                      'FieldDelimiter': 'string',
                      'QuoteCharacter': 'string'
                  },
                  'JSON': {
                      'RecordDelimiter': 'string'
                  }
              }
          )
          The response of this operation contains an :class:`.EventStream` member. When iterated the :class:`.EventStream` will yield events based on the structure below, where only one of the top level keys will be present for any given event.
        
        **Response Syntax**
        ::
            {
                'Payload': EventStream({
                    'Records': {
                        'Payload': b'bytes'
                    },
                    'Stats': {
                        'Details': {
                            'BytesScanned': 123,
                            'BytesProcessed': 123,
                            'BytesReturned': 123
                        }
                    },
                    'Progress': {
                        'Details': {
                            'BytesScanned': 123,
                            'BytesProcessed': 123,
                            'BytesReturned': 123
                        }
                    },
                    'Cont': {},
                    'End': {}
                })
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Payload** (:class:`.EventStream`) -- 
              - **Records** *(dict) --* 
                The Records Event.
                - **Payload** *(bytes) --* 
                  The byte array of partial, one or more result records.
              - **Stats** *(dict) --* 
                The Stats Event.
                - **Details** *(dict) --* 
                  The Stats event details.
                  - **BytesScanned** *(integer) --* 
                    The total number of object bytes scanned.
                  - **BytesProcessed** *(integer) --* 
                    The total number of uncompressed object bytes processed.
                  - **BytesReturned** *(integer) --* 
                    The total number of bytes of records payload data returned.
              - **Progress** *(dict) --* 
                The Progress Event.
                - **Details** *(dict) --* 
                  The Progress event details.
                  - **BytesScanned** *(integer) --* 
                    The current number of object bytes scanned.
                  - **BytesProcessed** *(integer) --* 
                    The current number of uncompressed object bytes processed.
                  - **BytesReturned** *(integer) --* 
                    The current number of bytes of records payload data returned.
              - **Cont** *(dict) --* 
                The Continuation Event.
              - **End** *(dict) --* 
                The End Event.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          The S3 bucket.
        :type Key: string
        :param Key: **[REQUIRED]**
          The object key.
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:
          The SSE Algorithm used to encrypt the object. For more information, see `Server-Side Encryption (Using Customer-Provided Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html>`__ .
        :type SSECustomerKey: string
        :param SSECustomerKey:
          The SSE Customer Key. For more information, see `Server-Side Encryption (Using Customer-Provided Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html>`__ .
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:
          The SSE Customer Key MD5. For more information, see `Server-Side Encryption (Using Customer-Provided Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html>`__ .
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type Expression: string
        :param Expression: **[REQUIRED]**
          The expression that is used to query the object.
        :type ExpressionType: string
        :param ExpressionType: **[REQUIRED]**
          The type of the provided expression (for example., SQL).
        :type RequestProgress: dict
        :param RequestProgress:
          Specifies if periodic request progress information should be enabled.
          - **Enabled** *(boolean) --*
            Specifies whether periodic QueryProgress frames should be sent. Valid values: TRUE, FALSE. Default value: FALSE.
        :type InputSerialization: dict
        :param InputSerialization: **[REQUIRED]**
          Describes the format of the data in the object that is being queried.
          - **CSV** *(dict) --*
            Describes the serialization of a CSV-encoded object.
            - **FileHeaderInfo** *(string) --*
              Describes the first line of input. Valid values: None, Ignore, Use.
            - **Comments** *(string) --*
              The single character used to indicate a row should be ignored when present at the start of a row.
            - **QuoteEscapeCharacter** *(string) --*
              The single character used for escaping the quote character inside an already escaped value.
            - **RecordDelimiter** *(string) --*
              The value used to separate individual records.
            - **FieldDelimiter** *(string) --*
              The value used to separate individual fields in a record.
            - **QuoteCharacter** *(string) --*
              Value used for escaping where the field delimiter is part of the value.
            - **AllowQuotedRecordDelimiter** *(boolean) --*
              Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.
          - **CompressionType** *(string) --*
            Specifies object\'s compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.
          - **JSON** *(dict) --*
            Specifies JSON as object\'s input serialization format.
            - **Type** *(string) --*
              The type of JSON. Valid values: Document, Lines.
          - **Parquet** *(dict) --*
            Specifies Parquet as object\'s input serialization format.
        :type OutputSerialization: dict
        :param OutputSerialization: **[REQUIRED]**
          Describes the format of the data that you want Amazon S3 to return in response.
          - **CSV** *(dict) --*
            Describes the serialization of CSV-encoded Select results.
            - **QuoteFields** *(string) --*
              Indicates whether or not all output fields should be quoted.
            - **QuoteEscapeCharacter** *(string) --*
              Th single character used for escaping the quote character inside an already escaped value.
            - **RecordDelimiter** *(string) --*
              The value used to separate individual records.
            - **FieldDelimiter** *(string) --*
              The value used to separate individual fields in a record.
            - **QuoteCharacter** *(string) --*
              The value used for escaping where the field delimiter is part of the value.
          - **JSON** *(dict) --*
            Specifies JSON as request\'s output serialization format.
            - **RecordDelimiter** *(string) --*
              The value used to separate individual records in the output.
        :rtype: dict
        :returns:
        """
        pass

    def upload_file(
        self,
        Filename=None,  # type: Optional[str]
        Bucket=None,  # type: Optional[str]
        Key=None,  # type: Optional[str]
        ExtraArgs=None,  # type: Optional[Dict]
        Callback=None,  # type: Optional[Callable]
        Config=None,  # type: Optional[TransferConfig]
    ):
        # type: (...) -> None
        """
        Upload a file to an S3 object.
        Usage::
            import boto3
            s3 = boto3.resource('s3')
            s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')
        Similar behavior as S3Transfer's upload_file() method,
        except that parameters are capitalized. Detailed examples can be found at
        :ref:`S3Transfer\'s Usage <ref_s3transfer_usage>`.
        :type Filename: str
        :param Filename: The path to the file to upload.
        :type Bucket: str
        :param Bucket: The name of the bucket to upload to.
        :type Key: str
        :param Key: The name of the key to upload to.
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            transfer.
        """
        pass

    def upload_fileobj(
        self,
        Fileobj=None,  # type: Optional[IO]
        Bucket=None,  # type: Optional[str]
        Key=None,  # type: Optional[str]
        ExtraArgs=None,  # type: Optional[Dict]
        Callback=None,  # type: Optional[Callable]
        Config=None,  # type: Optional[TransferConfig]
    ):
        # type: (...) -> None
        """
        Upload a file-like object to S3.
        The file-like object must be in binary mode.
        This is a managed transfer which will perform a multipart upload in
        multiple threads if necessary.
        Usage::
            import boto3
            s3 = boto3.client('s3')
            with open('filename', 'rb') as data:
                s3.upload_fileobj(data, 'mybucket', 'mykey')
        :type Fileobj: a file-like object
        :param Fileobj: A file-like object to upload. At a minimum, it must
            implement the `read` method, and must return bytes.
        :type Bucket: str
        :param Bucket: The name of the bucket to upload to.
        :type Key: str
        :param Key: The name of the key to upload to.
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            upload.
        """
        pass

    def upload_part(
        self,
        Bucket,  # type: str
        Key,  # type: str
        PartNumber,  # type: int
        UploadId,  # type: str
        Body=None,  # type: Optional[Union[Optional[bytes], Optional[IO]]]
        ContentLength=None,  # type: Optional[int]
        ContentMD5=None,  # type: Optional[str]
        SSECustomerAlgorithm=None,  # type: Optional[str]
        SSECustomerKey=None,  # type: Optional[str]
        SSECustomerKeyMD5=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Uploads a part in a multipart upload.
         **Note:** After you initiate multipart upload and upload one or more parts, you must either complete or abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you for the parts storage.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/UploadPart>`_
        
        **Request Syntax**
        ::
          response = client.upload_part(
              Body=b'bytes'|file,
              Bucket='string',
              ContentLength=123,
              ContentMD5='string',
              Key='string',
              PartNumber=123,
              UploadId='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'ETag': 'string',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServerSideEncryption** *(string) --* 
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
            - **ETag** *(string) --* 
              Entity tag for the uploaded object.
            - **SSECustomerAlgorithm** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
            - **SSECustomerKeyMD5** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
            - **SSEKMSKeyId** *(string) --* 
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Body: bytes or seekable file-like object
        :param Body:
          Object data.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
          Name of the bucket to which the multipart upload was initiated.
        :type ContentLength: integer
        :param ContentLength:
          Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.
        :type ContentMD5: string
        :param ContentMD5:
          The base64-encoded 128-bit MD5 digest of the part data. This parameter is auto-populated when using the command from the CLI. This parameted is required if object lock parameters are specified.
        :type Key: string
        :param Key: **[REQUIRED]**
          Object key for which the multipart upload was initiated.
        :type PartNumber: integer
        :param PartNumber: **[REQUIRED]**
          Part number of part being uploaded. This is a positive integer between 1 and 10,000.
        :type UploadId: string
        :param UploadId: **[REQUIRED]**
          Upload ID identifying the multipart upload whose part is being uploaded.
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        :type SSECustomerKey: string
        :param SSECustomerKey:
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass

    def upload_part_copy(
        self,
        Bucket,  # type: str
        CopySource,  # type: Union[str, Dict]
        Key,  # type: str
        PartNumber,  # type: int
        UploadId,  # type: str
        CopySourceIfMatch=None,  # type: Optional[str]
        CopySourceIfModifiedSince=None,  # type: Optional[datetime]
        CopySourceIfNoneMatch=None,  # type: Optional[str]
        CopySourceIfUnmodifiedSince=None,  # type: Optional[datetime]
        CopySourceRange=None,  # type: Optional[str]
        SSECustomerAlgorithm=None,  # type: Optional[str]
        SSECustomerKey=None,  # type: Optional[str]
        SSECustomerKeyMD5=None,  # type: Optional[str]
        CopySourceSSECustomerAlgorithm=None,  # type: Optional[str]
        CopySourceSSECustomerKey=None,  # type: Optional[str]
        CopySourceSSECustomerKeyMD5=None,  # type: Optional[str]
        RequestPayer=None,  # type: Optional[str]
    ):
        # type: (...) -> Dict
        """
        Uploads a part by copying data from an existing object as data source.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/UploadPartCopy>`_
        
        **Request Syntax**
        ::
          response = client.upload_part_copy(
              Bucket='string',
              CopySource='string' or {'Bucket': 'string', 'Key': 'string', 'VersionId': 'string'},
              CopySourceIfMatch='string',
              CopySourceIfModifiedSince=datetime(2015, 1, 1),
              CopySourceIfNoneMatch='string',
              CopySourceIfUnmodifiedSince=datetime(2015, 1, 1),
              CopySourceRange='string',
              Key='string',
              PartNumber=123,
              UploadId='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              CopySourceSSECustomerAlgorithm='string',
              CopySourceSSECustomerKey='string',
              RequestPayer='requester'
          )
        
        **Response Syntax**
        ::
            {
                'CopySourceVersionId': 'string',
                'CopyPartResult': {
                    'ETag': 'string',
                    'LastModified': datetime(2015, 1, 1)
                },
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'RequestCharged': 'requester'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CopySourceVersionId** *(string) --* 
              The version of the source object that was copied, if you have enabled versioning on the source bucket.
            - **CopyPartResult** *(dict) --* 
              - **ETag** *(string) --* 
                Entity tag of the object.
              - **LastModified** *(datetime) --* 
                Date and time at which the object was uploaded.
            - **ServerSideEncryption** *(string) --* 
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
            - **SSECustomerAlgorithm** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
            - **SSECustomerKeyMD5** *(string) --* 
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
            - **SSEKMSKeyId** *(string) --* 
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
            - **RequestCharged** *(string) --* 
              If present, indicates that the requester was successfully charged for the request.
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type CopySource: str or dict
        :param CopySource: **[REQUIRED]** The name of the source bucket, key name of the source object, and optional version ID of the source object.  You can either provide this value as a string or a dictionary.  The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version.  You can also provide this value as a dictionary.  The dictionary format is recommended over the string format because it is more explicit.  The dictionary format is: {\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}.  Note that the VersionId key is optional and may be omitted.
        :type CopySourceIfMatch: string
        :param CopySourceIfMatch:
          Copies the object if its entity tag (ETag) matches the specified tag.
        :type CopySourceIfModifiedSince: datetime
        :param CopySourceIfModifiedSince:
          Copies the object if it has been modified since the specified time.
        :type CopySourceIfNoneMatch: string
        :param CopySourceIfNoneMatch:
          Copies the object if its entity tag (ETag) is different than the specified ETag.
        :type CopySourceIfUnmodifiedSince: datetime
        :param CopySourceIfUnmodifiedSince:
          Copies the object if it hasn\'t been modified since the specified time.
        :type CopySourceRange: string
        :param CopySourceRange:
          The range of bytes to copy from the source object. The range value must use the form bytes=first-last, where the first and last are the zero-based byte offsets to copy. For example, bytes=0-9 indicates that you want to copy the first ten bytes of the source. You can copy a range only if the source object is greater than 5 MB.
        :type Key: string
        :param Key: **[REQUIRED]**
        :type PartNumber: integer
        :param PartNumber: **[REQUIRED]**
          Part number of part being copied. This is a positive integer between 1 and 10,000.
        :type UploadId: string
        :param UploadId: **[REQUIRED]**
          Upload ID identifying the multipart upload whose part is being copied.
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        :type SSECustomerKey: string
        :param SSECustomerKey:
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type CopySourceSSECustomerAlgorithm: string
        :param CopySourceSSECustomerAlgorithm:
          Specifies the algorithm to use when decrypting the source object (e.g., AES256).
        :type CopySourceSSECustomerKey: string
        :param CopySourceSSECustomerKey:
          Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.
        :type CopySourceSSECustomerKeyMD5: string
        :param CopySourceSSECustomerKeyMD5:
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        :type RequestPayer: string
        :param RequestPayer:
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        :rtype: dict
        :returns:
        """
        pass
