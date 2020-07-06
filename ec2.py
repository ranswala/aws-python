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
ec2_obj=boto3.resource('ec2')
for each_ec2 in ec2_obj.instances.all():
    print(each_ec2.id)
    count+=1
print(count)






