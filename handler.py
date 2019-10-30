import json
import boto3

client = boto3.client('ssm')

def get_secret(key):
	resp = client.get_parameter(
		Name=key,
		WithDecryption=True
	)
	return resp['Parameter']['Value']

def handle(event, context):

    response = {
        "statusCode": 200,
        "body": json.dumps(get_secret('mysecretkey'))
    }

    return response