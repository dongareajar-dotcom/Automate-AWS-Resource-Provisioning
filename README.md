# Automate AWS Resource Provisioning

## Overview
This project automates AWS resource creation using Python and boto3.

## Services Used
- AWS EC2
- AWS S3
- AWS IAM
- Python
- boto3

## Project Structure

create_s3.py
create_ec2.py
create_iam.py
requirements.txt

## Setup

1. Install Python
2. Install boto3

```bash
pip install boto3

#Configure AWS CLI
aws configure

#Run Scripts#
*Create S3 Bucket
python create_s3.py

*Create EC2 Instance
python create_ec2.py

*Create IAM User
python create_iam.py

*Skills Demonstrated*
AWS Automation
Python Scripting
boto3 SDK
Cloud Resource Provisioning
Infrastructure as Code Concepts
### Flow ###
        +------------------+
        |   Python Script  |
        |     (boto3)      |
        +--------+---------+
                 |
                 v
        +------------------+
        |      AWS API     |
        +--------+---------+
                 |
      +----------+----------+
      |                     |
      v                     v
+------------+      +--------------+
|   Amazon   |      |   Amazon     |
|     S3     |      |     EC2      |
+------------+      +--------------+

(Optional)
      |
      v
+------------+
|    IAM     |
+------------+
