import boto3

# Connect to EC2 client
ec2 = boto3.client('ec2')

# Input filter
tag_key = 'Group'
tag_value = 'DevOps-Batch'

# Describe EC2 instances with tag
response = ec2.describe_instances(
    Filters=[
        {'Name': f'tag:{tag_key}', 'Values': [tag_value]}
    ]
)

# Extract details
print(f"🔍 EC2 Instances with tag '{tag_key}={tag_value}':\n")

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        instance_type = instance['InstanceType']
        name_tag = ""

        # Find Name tag (if available)
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                name_tag = tag['Value']

        print(f"🆔 Instance ID : {instance_id}")
        print(f"🏷️ Name       : {name_tag}")
        print(f"📦 Type       : {instance_type}")
        print(f"⚙️ State      : {state}")
        print("-" * 40)
