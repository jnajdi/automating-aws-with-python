import boto3
import click

from botocore.exceptions import ClientError


session = boto3.Session(profile_name='local-machine')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List bucket objects"
    for obj in s3.Bucket(bucket).objects.all():
        print (obj.key)

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    "Create and setup an S3 bucket"
    s3_bucket = None
    
    try:
        s3_bucket = s3.create_bucket(Bucket=bucket)
        print(s3_bucket)
    except ClientError as exception:
        if exception.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            s3_bucket = s3.Bucket(bucket)
        else:
            raise exception

    # Assign Policy
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
    """ % s3_bucket.name

    policy = policy.strip()
    pol = s3_bucket.Policy()
    pol.put(Policy=policy)


    #Set the website configuration for the bucket
    website = s3_bucket.Website()
    website.put(WebsiteConfiguration={
            'ErrorDocument': {
                'Key': 'error.html'
            },
            'IndexDocument': {
                'Suffix': 'index.html'
            }})

    return


if __name__ == '__main__':
    cli()
