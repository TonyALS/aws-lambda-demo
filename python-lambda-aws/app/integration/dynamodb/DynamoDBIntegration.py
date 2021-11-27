import uuid

import boto3


class DynamoDBIntegration:
    def __init__(self, dynamo_client=boto3.resource('dynamodb', region_name='sa-east-1',
                                                    aws_access_key_id='',
                                                    aws_secret_access_key='',
                                                    endpoint_url='http://localhost:4566'
                                                    )):
        self.dynamo_client = dynamo_client

    def create_table(self):
        self.dynamo_client.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'pk',
                    'KeyType': 'HASH',
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'pk',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    def get_table(self):
        table = self.dynamo_client.Table('users')
        return table

    def create_user(self, pk, username, email):
        table = self.dynamo_client.Table('users')
        table.put_item(
            Item={
                'pk': pk,
                'username': username,
                'email': email
            }
        )

    def get_user(self, pk):
        item = self.dynamo_client.Table('users').get_item(
            Key={
                'pk': pk
            }
        )
        return item

    def update_user(self, pk, new_username, new_email):
        table = self.dynamo_client.Table('users')
        table.update_item(
            Key={
                'pk': pk
            },
            UpdateExpression='SET username=:val1, email=:val2',
            ExpressionAttributeValues={
                ':val1': new_username,
                ':val2': new_email
            }
        )
