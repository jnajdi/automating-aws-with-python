# -*- coding: utf-8 -*-

"""Classes for S3 Buckets."""

from botocore.exceptions import ClientError
import mimetypes
from pathlib import Path


class BucketManager:
    """Manage an S3 Bucket."""

    def __init__(self, session):
        """Create a BucketManager object."""
        self.session = session
        self.s3 = session.resource('s3')

    def all_buckets(self):
        """Get an iterator for all buckets."""
        return self.s3.buckets.all()

    def all_objects(self, bucket):
        """Get an iterator for all objects in a bucket."""
        return self.s3.Bucket(bucket).objects.all()

    def init_bucket(self, bucket_name):
        """Create new bucket, or return existing one by name."""
        s3_bucket = None
        try:
            s3_bucket = self.s3.create_bucket(Bucket=bucket_name)
        except ClientError as exception:
            if exception.response['Error']['Code'] \
                    == 'BucketAlreadyOwnedByYou':
                s3_bucket = self.s3.Bucket(bucket_name)
            else:
                raise exception
        return s3_bucket

    @staticmethod
    def set_policy(bucket):
        """Set bucket policy to be readable by everyone."""
        policy = """
            {
              "Version":"2012-10-17",
              "Statement":[{
                "Sid":"PublicReadGetObject",
                    "Effect":"Allow",
                  "Principal": "*",
                  "Action":["s3:GetObject"],
                  "Resource":["arn:aws:s3:::%s/*"
                  ]
                }
              ]
            }
        """ % bucket.name

        policy = policy.strip()
        pol = bucket.Policy()
        pol.put(Policy=policy)

    @staticmethod
    def configure_website(bucket):
        """Configure s3 website hosting for bucket."""
        # Set the website configuration for the bucket
        website = bucket.Website()
        website.put(WebsiteConfiguration={
            'ErrorDocument': {
                'Key': 'error.html'
            },
            'IndexDocument': {
                'Suffix': 'index.html'
            }})

    @staticmethod
    def upload_file(bucket, path, key):
        """Upload path to s3_bucket at key."""
        content_type = mimetypes.guess_type(key)[0] or 'text/html'

        return bucket.upload_file(path, key,
                                  ExtraArgs={'ContentType': content_type})

    def sync(self, pathname, bucket_name):
        """Sync contents of path to bucket."""
        bucket = self.s3.Bucket(bucket_name)

        root = Path(pathname).expanduser().resolve()

        def handle_directory(target):

            for path in target.iterdir():
                if path.is_dir():
                    handle_directory(path)
                if path.is_file():
                    # print("Path: {} \n Key: {}".format(p, p.relative_to(root)))
                    relative_path = str(path.relative_to(root))
                    print("{0}: {1}".format(str(path), relative_path))
                    self.upload_file(bucket, str(path), relative_path)

        handle_directory(root)
