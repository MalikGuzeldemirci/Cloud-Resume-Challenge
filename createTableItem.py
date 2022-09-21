import boto3

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

table = dynamodb.Table('counter-db')

response = table.put_item(
Item = { 
     'WebsiteName': 'www.malikguzeldemirci.com'
        }
)
table.update_item(
        Key = {
             'WebsiteName': 'www.malikguzeldemirci.com'   
        },
        UpdateExpression = "ADD VisitCount :inc",
        ExpressionAttributeValues={
            ':inc': 0
        },
)
