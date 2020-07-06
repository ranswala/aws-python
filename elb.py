import boto3
import time
import sys

elb_obj = boto3.client('elb','us-west-2')
count = 0
without_instance = []
with_instance = []

#elb = elb_obj.describe_load_balancers()['LoadBalancerDescriptions']
#print(elb)

for elb in elb_obj.describe_load_balancers()['LoadBalancerDescriptions']:
    if elb['Instances'] == []:
#        print(elb['LoadBalancerName'])
        without_instance.append(elb['LoadBalancerName'])
        count+=1
    else:
        x = elb['Instances']
        for id in x:
#            print(elb['LoadBalancerName'])
#            print(id['InstanceId'])
            with_instance.append(id['InstanceId'])
            count+=1

time.sleep(2)

print("Name of the elb with no instance attached =", without_instance)
print("Instanceids attached to elb =", with_instance)
print("Total number of elbs are:", count)

    
