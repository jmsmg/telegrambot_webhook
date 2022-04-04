import boto3

# reference : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

def create_db(dynamodb=None):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('aura_table') # table 이름
    response = table.put_item(
        item = {
            'no': 1,
            'name': '홍길동',
            'id':'hong'
        }
    )

    return response