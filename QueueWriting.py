import boto3
import json

client = boto3.client(
    'sqs',
    aws_access_key_id='AKIA5DF2EZYG7KXNRA63',
    aws_secret_access_key='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', region_name="us-east-1"
)

payload = json.dumps({
       "id": 0,
       "petId": "Panda",
        "quantity": 0,
        "shipDate": "2022-08-05T08:29:59.479Z",
        "status": "placed",
        "complete": True
})
response = client.send_message(
QueueUrl="https://sqs.us-east-1.amazonaws.com/900186033677/RedoxReceiveMessageQueue.fifo",
MessageBody= payload, MessageGroupId="1") 