# coding: utf-8
import boto3
from pprint import pprint
session = boto3.Session(profile_name='local-machine')
s3 = session.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket)
#
# new_bucket = s3.create_bucket(Bucket='automating-aws-jnajdi')
# s3.list_buckets()
# for bucket in s3.list_buckets():
#     print (bucket)
#
# for bucket in s3.buckets.all():
#     print (bucket)
#
#
# ec2_client = session.client('ec2')
# get_ipython().run_line_magic('history', '')
