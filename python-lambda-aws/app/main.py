from integration.dynamodb.DynamoDBIntegration import DynamoDBIntegration
from integration.sqs.SQSIntegration import SQSIntegration


def lambda_test():
    sqs = SQSIntegration()
    message = {"name": "Tony Augusto"}
    # sqs.send_message(message)
    response = sqs.receive_message()
    print(response)
    dynamo = DynamoDBIntegration()
    # dynamo.create_table()
    table = dynamo.get_table()
    # dynamo.create_user('1', 'Tony', 'a@a.com')
    item = dynamo.get_user('1')
    dynamo.update_user('1', 'Joao', 'b@b.com')
    item2 = dynamo.get_user('1')
    print(table)


if __name__ == '__main__':
    lambda_test()
