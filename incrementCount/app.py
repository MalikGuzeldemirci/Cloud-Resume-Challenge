import json
import boto3
import os

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
table = dynamodb.Table("counter-db")
    
def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    table = dynamodb.Table("counter-db")
    response = table.update_item(
        Key={
            "WebsiteName":"www.malikguzeldemirci.com"
        },
        UpdateExpression='ADD ' + 'VisitCount' + ' :incr',
        ExpressionAttributeValues={':incr':1},
        ReturnValues="UPDATED_NEW"
    )
    return  {       
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*" 
        },
    }





