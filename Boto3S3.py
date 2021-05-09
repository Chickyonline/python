from __future__ import print_function

import boto3
import os

os.environ['AWS_PROFILE'] = "Boto3User"
os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

client = boto3.client('s3')
# # commented out after creating the bucket
# client.create_bucket(Bucket='sak-python-aws-s3')

# Now Upload files from local pc to S3
def upload_files (file_name, bucket, object_name=None, args=None):
    """
    file_name = Name of file on local PC
    bucket = bucket name
    object_name = Name of file on S3 bucket
    args = custom argument
    """
    if object_name is None:
        object_name = file_name

    upload_response = client.upload_file(file_name, bucket, object_name, ExtraArgs = args)
    print(upload_response)

# # Upload single file from local PC to S3
# upload_files('D:\\data\\Sak\\AWS\\AWS\\AWS\\boto3\\data\\pexels.jpeg', 'sak-python-aws-s3')

# # list all the files in the local PC directory
# import glob
# files = glob.glob('D:\\data\\Sak\\AWS\\AWS\\AWS\\boto3\\data/*')
# print(files)     # lists all files in the director

# # upload files in a loop
# args = {'ACL': 'public-read'}   # set permission for the objects uploaded
# for file in files:
#     upload_files(file, 'sak-python-aws-s3')
#     print(f'uploaded file : {file}')

# # List all the buckets in S3
# response = client.list_buckets()
# print(response['Buckets'])

# # Download files from s3
# list all the buckets in s3
s3 = boto3.resource('s3')
# print(list(s3.buckets.all()))       # outputs summary response
# print(client.list_buckets())        # outputs detailed response

# list objects inside a specific bucket
bucket = s3.Bucket('sak-python-aws-s3')
files = bucket.objects.all()
print(list(bucket.objects.all()))

for file in files:
    client.download_file('sak-python-aws-s3', file.key, file.key)

print(f'All files downloaded from bucket : {bucket}')
