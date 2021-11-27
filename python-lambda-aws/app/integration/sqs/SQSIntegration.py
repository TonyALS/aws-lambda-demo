import json

import boto3


class SQSIntegration:
    def __init__(self, sqs_client=boto3.client('sqs', region_name='sa-east-1',
                                               aws_access_key_id='',
                                               aws_secret_access_key='',
                                               endpoint_url="http://localhost:4566")):
        self.sqs_client = sqs_client
        self.queue_url = sqs_client.get_queue_url(QueueName='aws-lambda-queue')

    def receive_message(self):
        response = self.sqs_client.receive_message(QueueUrl=self.queue_url['QueueUrl'],
                                                   MaxNumberOfMessages=1,
                                                   WaitTimeSeconds=10)
        return response

    def send_message(self, message):
        return self.sqs_client.send_message(
            QueueUrl=self.queue_url['QueueUrl'],
            MessageBody=json.dumps(message),
            DelaySeconds=0,
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
