import json
import boto3

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
table = dynamodb.Table("counter-db")
client = boto3.client('lambda')
    
def lambda_handler(event, context):
    
    emptyObj = {}
    invoke_response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-1:303443706848:function:cloud-resume-challenge-incrementCount-uZiQeKwxFpi8',
        InvocationType ='RequestResponse',
        Payload = json.dumps(emptyObj)
    )
    response = table.get_item(
        Key={
            'WebsiteName': 'www.malikguzeldemirci.com'
        }
    )
    body = response['Item']['VisitCount']
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*" 
        },
        "body": json.dumps(
            {
                "VisitCount":str(body)
            }
        ),
    }
    
        
       
    
