import boto3
ec2 = boto3.client('ec2', 'us-west-2')

custom_filter = [{
    'Name':'tag:Owner',
    'Values': ['Srib']}]

reservations = ec2.describe_instances(Filters=custom_filter)
instances = []
for reservation in reservations['Reservations']:
     for instance in reservation['Instances']:
         instances.append(instance)
#print(instances)

environments = []
for instance in instances:
    for tag in instance['Tags']:
        if tag['Key'] == 'Name':
            environments.append(tag['Value'])
print(environments)

value = input("enter the name of instance to start or stop")
ec2 = boto3.resource('ec2') # Here I forgot to add the us-west-2 region, so it took default region as ap-south-1 from where I running this script.

for i in environments:
    if i == value:
        ec2.instances.stop()  # this command got executed in all the servers.
Print("Instance stopped is" , value)
