# step : 1 (not advice )

import boto3

# client = boto3.client(
#     'ec2',
#     aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY,
# )
# step : 2

# default profile and default region

# import boto3
#
#
# ec2_client = boto3.client('ec2')
#
# response = ec2_client.describe_instances()
#
# print(response)

# default profile but specific region

# import boto3
#
# client = boto3.client('ec2',
#                           region_name="us-west-2")



# # step : 3
#
# import boto3
#
# session = boto3.session.Session(profile_name='test')
#
# client = session.client('ec2', region_name='us-east-1')

# s3 get data
# cretae ec2
# cretae s3



import boto3

# s3 = boto3.resource('s3')
#
# s3.meta.client.download_file('code-sharing-bucket', 'avinash/api.sentinel', '/home/ec2-user/api.sentinel')
#
#
#
# import boto3
# s3 = boto3.resource('s3')
# s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')



client = boto3.client('ec2')

response = client.run_instances(
    MaxCount=5,
    MinCount=5,
    ImageId='ami-0ca285d4c2cda3300',
InstanceType="t2.micro"
)




instancedata = client.describe_instances()

# print(instancedata['Reservations'])
instanceids =[]

for i in instancedata['Reservations']:
    for y in i['Instances']:
        print(y['InstanceId'])
        instanceids.append(y["InstanceId"])

print(instanceids)

response = client.terminate_instances(
    InstanceIds=instanceids
)

# # topics used :  variables, error handling,
#
# import boto3
#
# # below client we are accessing default profile and s3 service and region us-west-2
#
# s3_client = boto3.client('s3') # client connection
#
# # parameters used
# bucket_name = "avinash-jjtech-boto-examplebucket"
# bucket_location = "us-west-2"
#
# # creation of the bucket code
#
# try:
#     s3_create_bucket_response = s3_client.create_bucket(
#         ACL='private',
#         Bucket=bucket_name,
#         CreateBucketConfiguration={
#             'LocationConstraint': bucket_location
#         }
#     )
#     print(s3_create_bucket_response)
# except Exception as e:
#     print(e)
#
# # making the bucket private
# response = s3_client.put_public_access_block(
#     Bucket=bucket_name,
#     PublicAccessBlockConfiguration={
#         'BlockPublicAcls': True,
#         'IgnorePublicAcls': True,
#         'BlockPublicPolicy': True,
#         'RestrictPublicBuckets': True
#     }
# )


# topics used :  variables, error handling,

# import boto3
#
# # below client we are accessing default profile and s3 service and region us-west-2
#
# s3_client = boto3.client('s3') # client connection
# # parameters used
# bucket_name = "avinash-jjtech-boto-examplebucket"
# bucket_location = "us-west-2"
# try:
#     s3_create_bucket_response = s3_client.create_bucket(
#             ACL='private',
#             Bucket=bucket_name,
#             CreateBucketConfiguration={
#                 'LocationConstraint': bucket_location
#             }
#         )
#     print(s3_create_bucket_response)
# except Exception as e:
#     print(e)



# creation of the bucket code

# try:
#     s3_create_bucket_response = s3_client.create_bucket(
#         ACL='private',
#         Bucket=bucket_name,
#         CreateBucketConfiguration={
#             'LocationConstraint': bucket_location
#         }
#     )
#     print(s3_create_bucket_response)
# except Exception as e:
#
#     print(e)

# making the bucket private
# response = s3_client.put_public_access_block(
#     Bucket=bucket_name,
#     PublicAccessBlockConfiguration={
#         'BlockPublicAcls': True,
#         'IgnorePublicAcls': True,
#         'BlockPublicPolicy': True,
#         'RestrictPublicBuckets': True
#     }
# )




