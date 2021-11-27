#!/bin/bash
set -x
# Cria o SQS
awslocal sqs create-queue --endpoint-url=http://localstack:4566 --queue-name aws-lambda-queue
set +x