import os,sys
import time

try:
    import boto3
    print("boto3 imported sucessfully")
except Exception as e:
    print(e)
    print("boto3 error and try again")
    sys.exit(1)
time.sleep(3)

iam_obj = boto3.client('iam') # with what service you want to connect with resource method. Here we are using iam 
#print(dir(iam_obj))

x = iam_obj.list_users()
#print(x['Users'][0]['UserName'])
each_user = iam_obj.list_users()['Users']
for x in each_user:
    print(x['UserName'])














