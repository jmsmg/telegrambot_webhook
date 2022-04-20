"""
메인함수로 직접 구동되는 lambda_handler부분
"""
from telebot import Bot
import json
import os
from table_db import Connect_db

TOKEN = os.environ['TOKEN']
URL = f'/bot{TOKEN}'

def lambda_handler(event, context):

    print("event :", event) # 들어오는 값 확인용
    print("context :", context) # 들어오는 값 확인용
    
    tele_request = json.loads(event['body']) # 사용자에게서 들어오는 event['body']
    print(tele_request)

    # json 문법 체크
    if tele_request.get('callback_query'): # 버튼 눌렀을때
        data = tele_request["callback_query"]["data"]
        message_id = tele_request["callback_query"]["message"]["message_id"]
        sender_name = tele_request["callback_query"]["from"]["first_name"]
        command = f'button_data_{data}'

    elif tele_request.get('message'): # 메세지를 받았을때
        command = tele_request["message"]["text"]
        sender_name = tele_request["message"]["from"]["first_name"]
        
    bot = Bot(URL)
    
    api_method = bot.find_method(command)
    bot.ft_response(api_method, sender_name, command)
    # 콜백 쿼리 부분

    # DB 연결 부분
    
    connect_db = Connect_db()
    print(connect_db.read_table())
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }