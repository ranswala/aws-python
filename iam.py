import os,sys
import time

try:
    import boto3
    print("boto3 imported sucessfully")
except Exception as e:
    print(e)
    print("boto3 error and try again")
    sys.exit(1)
time.sleep(5)

iam_obj = boto3.resource('iam') # with what service you want to connect with resource method. Here we are using iam 
#for user in iam_obj.users.all():
#    print(user.name)
for user in iam_obj.users.all():
    print(user)





