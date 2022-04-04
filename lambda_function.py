"""
메인함수로 직접 구동되는 lambda_handler부분
"""
from telebot import Bot
import json
import os
from table_db import create_db

TOKEN = os.environ['TOKEN']
URL = f'/bot{TOKEN}'

def lambda_handler(event, context):

    print("event :", event) # 들어오는 값 확인용
    print("context :", context) # 들어오는 값 확인용
    
    tele_request = json.loads(event['body']) # 사용자에게서 들어오는 event['body']
    command = tele_request["message"]["text"]
    sender_name = tele_request["message"]["from"]["first_name"]
    
    bot = Bot(URL, command)

    if command == '/table' or command == '/task' :
        bot.ft_response("/sendMessage", sender_name)

    elif command == '/photo':
        bot.ft_response("/sendPhoto", sender_name)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }