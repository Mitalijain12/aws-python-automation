import boto3

# Connect to EC2
ec2 = boto3.resource('ec2')

# Configuration
count = 2  # Number of instances
group_name = "DevOps-Batch"
ami_id = 'ami-00b7ea845217da02c'  # <-- Replace with valid AMI ID
instance_type = 't2.micro'
key_name = 'my-key'  # <-- Replace with your key pair name
volume_size = 8  # in GB

# Launch instances

instances = ec2.create_instances(
    ImageId=ami_id,
    MinCount=count,
    MaxCount=count,
    InstanceType=instance_type,
    KeyName=key_name,
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'VolumeSize': volume_size,
                'DeleteOnTermination': True,
                'VolumeType': 'gp2'
            }
        }
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Group', 'Value': group_name}]
        }
    ]
)
# Add unique Name tag to each instance and print details
print("✅ EC2 Instances Created:\n")

for i, instance in enumerate(instances, start=1):
    # Wait for instance to be in a running state before tagging (optional but safe)
    instance.wait_until_running()
    instance.reload()  # Refresh instance state

    # Add unique Name tag
    name_tag = f'{group_name}-Server-{i}'
    instance.create_tags(Tags=[
        {'Key': 'Name', 'Value': name_tag}
    ])

    # Print details
    print(f"🔹 Instance {i}:")
    print(f"   Name     : {name_tag}")
    print(f"   Instance : {instance.id}")
    print(f"   State    : {instance.state['Name']}")
    print("-" * 40)
