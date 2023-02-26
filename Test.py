import boto3
import json

#sqs = boto3.resource('sqs')
#print('Hello World')
#queue = sqs.get_queue_by_name(QueueName='RedoxReceiveMessageQueue.fifo')
#print (queue.url)


payload = json.dumps({
       "id": 0,
       "petId": "Tiger",
        "quantity": 0,
        "shipDate": "2022-08-05T08:29:59.479Z",
        "status": "placed",
        "complete": True
})
response = client.send_message(
QueueUrl="https://sqs.ap-south-1.amazonaws.com/570088733634/DemoQueueForWriting.fifo",
MessageBody= payload, MessageGroupId="1") 


#session = boto3.Session(
#    aws_access_key_id='AKIAYJO7PXPBAU5LCDEE',
#    aws_secret_access_key='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',aws_session_token=None
    
#)
#client =session.client('sqs')

#response = client.send_message(
#QueueUrl="https://sqs.ap-south-1.amazonaws.com/570088733634/DemoQueueForWriting",
#MessageBody= payload) 
