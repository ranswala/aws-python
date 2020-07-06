import time
import sys

try:
    import boto3
    print("boto3 imported successfully")
except exception as e:
    print("import failed. Install boto3")
    sys.exist(1)

time.sleep(2)

s3_obj = boto3.resource('s3')
for buckets in s3_obj.buckets.all():
    print(buckets.name)

