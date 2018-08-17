# coding: utf-8
import boto3
session = boto3.Session(profile_name='local_machine')
session = boto3.Session(profile_name='local-machine')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
print key_path
print(key_path)
key = ec2.create_key_pair(KeyName=key_name)
get_ipython().run_line_magic('history', '')
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key, key_material)
    
with open(key_path, 'w') as key_file:
    key_file.write(ke.key_material)
    
    
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
    
    
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
get_ipython().run_line_magic('history', '')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
get_ipython().run_line_magic('history', '')
ec2.images.filter(Oweners=['amazon'])
list(ec2.imagesCollection(ec2.ServiceResource(), ec2.Image))
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-04681a1dbd79675a5')
img.name
get_ipython().run_line_magic('history', '')
img.name
ami_name='amzn2-ami-hvm-2.0.20180810-x86_64-gp2'
Filters = [{‘Name’: ‘name’, ‘Values’: [ami_name]}]
filters = [{'Name': 'name', 'Values':[ami_name]}]
list(ec2.images.filter(Owners['amazon'], Filters=filters))
ec2.images.filter(Owners=['amazon'], Filters=filters)
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
get_ipython().run_line_magic('history', '')
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
get_ipython().system('ping google.com')
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img
key
instances = ec2.create_instance(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
instances.terminate()
instances[0].terminate()
get_ipython().run_line_magic('history', '')
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances[0]
inst = instances[0]
inst.public_dns_name
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
get_ipython().run_line_magic('history', '')
inst.public_dns_name
inst.security_groups
# Look up the security group
# Authorize incoming connections from our public IP address on port 22 (The port ssh uses)
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 
'IpRanges': [{'CidrIp': '73.222.9.196/32}]}]
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 
'IpRanges': [{'CidrIp': '73.222.9.196/32}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP','IpRanges': [{'CidrIp': '73.222.9.196/32}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol': 'TCP','IpRanges': [{'CidrIp': '73.222.9.196/32'}]}])
get_ipython().run_line_magic('history', '')
sg.authorize_ingress(IpPermissions=[{'FromPort':80, 'ToPort':22, 'IpProtocol': 'TCP','IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':80, 'ToPort':80, 'IpProtocol': 'TCP','IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
