# AWS Automation Scripts (Python + Boto3)

This repository contains automation scripts for managing AWS infrastructure using Python and Boto3 SDK.

## ✅ Scripts Included

- `create_iam_user.py`: Create IAM users, attach policies, and generate access keys.
- `create_ec2_instances.py`: Launches multiple EC2 instances (Free Tier eligible) with custom volume size, group tagging, and unique Name tags for each instance. Includes wait + reload handling.
- `ec2_auto_stop.py`: Stops running EC2 instances tagged with `Group=DevOps-Batch` to reduce AWS cost in non-production environments.
- `filter_ec2_by_tag.py`: Filter EC2 instances by tag and state for reporting or action.

## 🔧 Tools Used

- Python 3.x
- Boto3 (AWS SDK for Python)
- AWS Free Tier

## 📦 Use Cases

- Developer onboarding
- Automated infra provisioning
- Cost optimization in staging/dev environments

