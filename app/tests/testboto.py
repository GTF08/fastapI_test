import json
import boto3

cred = json.loads('{"url":"http://localhost:9001/api/v1/service-account-credentials","accessKey":"uYG5QTPcGRtF1B808zyO","secretKey":"mxTDfKReDtOtCbLIRXutjsH2EfsP9mq2j356eDf4","api":"s3v4","path":"auto"}')
api_url = 'http://localhost:9000'
ACCESS_KEY = cred["accessKey"]
SECRET_KEY = cred["secretKey"]
api_v = cred["api"]
BUCKET='testimages'

s3 = boto3.client(
    's3',
    endpoint_url = api_url,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
if BUCKET not in buckets:
    s3.create_bucket(Bucket=BUCKET)

def override_get_s3_client():
    return s3

def override_get_bucket():
    return BUCKET
