import json
import boto3

def lambda_handler(event, context):
    name = event['name']
    age = event['age']
    print("Name: " + name)
    print("Age: " + str(age))
    return {
        'statusCode': 200,
        'body': f'Hello {name}! You are {age} years old.'
    }
