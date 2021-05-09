from __future__ import print_function
import boto3
import os

os.environ['AWS_PROFILE'] = "Boto3User"
os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

s3 = boto3.resource('s3')
                    # aws_access_key_id=ACCESS_ID,
                    # aws_secret_access_key=ACCESS_KEY)

for bucket in s3.buckets.all():
    print(bucket.name)