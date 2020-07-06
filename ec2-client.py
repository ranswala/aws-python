import sys
import os
import time

try:
    import boto3
    print("import done")
except exception as e:
    print(e)
    print("Install boto3")
    sys.exit(1)

time.sleep(3)
count = 0
ec2_obj=boto3.client('ec2')
for instance_id in ec2_obj.describe_instances()['Reservations']:
    x = instance_id['Instances']
    for id in x:
        print(id['InstanceId'])
        print(id['State'])







