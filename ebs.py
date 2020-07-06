
import sys
import time

try:
    import boto3
    print( "boto3 installed")
except exception as e:
    print("Install boto3")
    sys.exist(1)

time.sleep(2)

vol_obj = boto3.resource('ec2','us-west-2')
for vols in vol_obj.volumes.all():
    if vols.state=='available':
         #print(vols)
         vid=vols.id
#         print(vid)
         v = vol_obj.Volume(vid)
         print(v)
#         v.delete()
#         print("Deleted " +vid)
         

     



