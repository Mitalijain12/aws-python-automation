import boto3

# Connect to EC2 client
ec2 = boto3.client('ec2')

# Filter for running instances with specific tag
response = ec2.describe_instances(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:Group', 'Values': ['DevOps-Batch']}
    ]
)

# Extract all matching instance IDs
instance_ids = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Stop the instances
if instance_ids:
    print(f"🛑 Stopping Instances: {instance_ids}")
    ec2.stop_instances(InstanceIds=instance_ids)
else:
    print("✅ No running instances found with Group=DevOps-Batch")
