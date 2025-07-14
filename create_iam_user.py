import boto3
import json

# Create IAM client
iam = boto3.client('iam')

# Step 1: Ask for IAM username
user_name = input("Enter IAM username to create: ").strip()

# Step 2: Create the IAM user
try:
    iam.create_user(UserName=user_name)
    print(f"✅ User '{user_name}' created.")
except iam.exceptions.EntityAlreadyExistsException:
    print(f"⚠️ User '{user_name}' already exists.")

# Step 3: Attach AWS managed policy (e.g., S3 ReadOnly)
policy_arn = 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'

iam.attach_user_policy(
    UserName=user_name,
    PolicyArn=policy_arn
)
print(f"🔐 Policy attached: {policy_arn}")

# Step 4: Create access keys (programmatic access)
response = iam.create_access_key(UserName=user_name)
access_key = response['AccessKey']['AccessKeyId']
secret_key = response['AccessKey']['SecretAccessKey']

print("\n🔑 Access Key & Secret:")
print(f"🆔 Access Key : {access_key}")
print(f"🔐 Secret Key : {secret_key}")
