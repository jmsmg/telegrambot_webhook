import boto3

# reference : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

# Get the service resource

class Connect_db:
    """
    dynamodb와 연결하는 클래스
    """

    def create_table(dynamodb=None):
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('aura_table') # table 이름

        table.put_item(
            Item={
                'table_number': 'v2',
                'bottle': 'jack daniels',
                'number_of_people': '3',
                'vacancy': False
            }
            )

        return None
    
    def read_table(dynamodb=None):
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('aura_table')
    
        response = table.get_item(
            Key={
                'table_number': 'v2'
            }
            )
        
        item = response['Item']

        return item
    
    def update_table(dynamodb=None):
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('aura_table')
        
        table.update_item(
            Key={
                'table_number': 'v2'
            },
            UpdateExpression='Set bottle = :bottle',
            ExpressionAttributeValues={
                ':bottle': 'alize'
            }
            )