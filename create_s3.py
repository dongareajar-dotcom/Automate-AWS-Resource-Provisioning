import boto3

s3 = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'sahil-automation-bucket-12345'

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket Created Successfully")
