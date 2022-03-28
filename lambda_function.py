"""
메인함수로 직접 구동되는 lambda_handler부분
"""
from telebot import Bot
import json


def lambda_handler(event, context):

    print("event :", event) # 들어오는 값 확인용
    print("context :", context) # 들어오는 값 확인용

    tele_request = json.loads(event['body']) # 사용자에게서 들어오는 event['body']
    command = tele_request['message']['text']
    print(tele_request)
    
    # 보낸사람이름 : tele_request['message']['from']['first_name'])

    bot = Bot()

    bot.get_command(command)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }