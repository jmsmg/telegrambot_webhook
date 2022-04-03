from urllib import response
import boto3


def create_table(dynamodb=None):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('User') # table 이름
    response = table.put_item(
        item = {
            'no': 1,
            'name': '홍길동',
            'id':'hong'
        }
    )

    return response