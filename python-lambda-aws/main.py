import boto3
import requests

AWS_CLIENT_ID = ""
AWS_CLIENT_SECRET = ""
REGION_DEFAULT = "sa-east-1"
BUCKET_NAME = "bucket-teste"
ENDPOINT_URL_DEFAULT = "http://localhost:4566"
SQS_QUEUE_URL = f"{ENDPOINT_URL_DEFAULT}/000000000000/queue-teste"


def boto_client():
    return boto3.client('sqs', aws_access_key_id=AWS_CLIENT_ID, aws_secret_access_key=AWS_CLIENT_SECRET,
                        region_name=REGION_DEFAULT,
                        endpoint_url=ENDPOINT_URL_DEFAULT)


def send_message():
    client = boto_client()
    return client.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody='hello world py',
        DelaySeconds=5,
        MessageAttributes={
            'string': {
                'StringValue': 'string',
                'BinaryValue': b'bytes',
                'StringListValues': [
                    'string',
                ],
                'BinaryListValues': [
                    b'bytes',
                ],
                'DataType': 'String'
            }
        },
        MessageSystemAttributes={
            'string': {
                'StringValue': 'string',
                'BinaryValue': b'bytes',
                'StringListValues': [
                    'string',
                ],
                'BinaryListValues': [
                    b'bytes',
                ],
                'DataType': 'String'
            }
        },
        MessageDeduplicationId='string',
        MessageGroupId='string'
    )


if __name__ == '__main__':
    sqs = boto3.client('sqs', aws_access_key_id=AWS_CLIENT_ID, aws_secret_access_key=AWS_CLIENT_SECRET,
                       region_name=REGION_DEFAULT,
                       endpoint_url=ENDPOINT_URL_DEFAULT)
    # send_message()

    response = sqs.receive_message(
        QueueUrl=SQS_QUEUE_URL,
        AttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=1,
        WaitTimeSeconds=1,
        ReceiveRequestAttemptId='string'
    )
    req_response = requests.get("http://localhost:8081/api")
    # requests.post("http://localhost:8081/api", json={"s": "dados enviados pela lambda"})
    for m in response['Messages']:
        requests.post("http://localhost:8081/api", json={"s": m['Body']})
        print(m['Body'])
    # print(response)
    # print(req_response)
