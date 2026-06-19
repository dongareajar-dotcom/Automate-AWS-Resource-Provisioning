import boto3

iam = boto3.client('iam')

response = iam.create_user(
    UserName='developer-user'
)

print("IAM User Created")
