
import boto3
import pprint

Region_names = []
ec2 = boto3.client('ec2')
region_all = ec2.describe_regions()
pprint.pprint(region_all['Regions'])

for each_region in region_all['Regions']:
    print(each_region['RegionName'])
    Region_names.append(each_region['RegionName'])
print(Region_names)

for each_reg in Region_names:
    ec2_obj = boto3.resource('ec2')
    for instance in ec2_obj.instances.all():
    print(instance.id,instance.state['Name'])



