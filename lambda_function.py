"""
메인함수로 직접 구동되는 lambda_handler부분
"""
from telebot import Bot
import json


def lambda_handler(event, context):

    print("event :", event) # 들어오는 값 확인용
    print("context :", context) # 들어오는 값 확인용

    TeleRes = json.loads(event['body']) # 사용자에게서 들어오는 event['body']
    print(TeleRes)
    bot = Bot()

    bot.send_message(TeleRes)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }