# coding: utf-8
# fmt: off
from datetime import datetime
from typing import Dict
from typing import Optional
from botocore.waiter import Waiter


class BucketExists(Waiter):
    def wait(
        self,
        Bucket,  # type: str
        WaiterConfig=None,  # type: Optional[Dict]
    ):
        # type: (...) -> None
        """
        Polls :py:meth:`S3.Client.head_bucket` every 5 seconds until a successful state is reached. An error is returned after 20 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadBucket>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              Bucket='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 5
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 20
        :returns: None
        """
        pass


class BucketNotExists(Waiter):
    def wait(
        self,
        Bucket,  # type: str
        WaiterConfig=None,  # type: Optional[Dict]
    ):
        # type: (...) -> None
        """
        Polls :py:meth:`S3.Client.head_bucket` every 5 seconds until a successful state is reached. An error is returned after 20 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadBucket>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              Bucket='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 5
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 20
        :returns: None
        """
        pass


class ObjectExists(Waiter):
    def wait(
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
        WaiterConfig=None,  # type: Optional[Dict]
    ):
        # type: (...) -> None
        """
        Polls :py:meth:`S3.Client.head_object` every 5 seconds until a successful state is reached. An error is returned after 20 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject>`_
        
        **Request Syntax**
        ::
          waiter.wait(
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
              PartNumber=123,
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
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
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 5
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 20
        :returns: None
        """
        pass


class ObjectNotExists(Waiter):
    def wait(
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
        WaiterConfig=None,  # type: Optional[Dict]
    ):
        # type: (...) -> None
        """
        Polls :py:meth:`S3.Client.head_object` every 5 seconds until a successful state is reached. An error is returned after 20 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject>`_
        
        **Request Syntax**
        ::
          waiter.wait(
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
              PartNumber=123,
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
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
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 5
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 20
        :returns: None
        """
        pass
