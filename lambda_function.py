"""
메인함수로 직접 구동되는 lambda_handler부분
"""
from telebot import Bot
import json
import os

TOKEN = os.environ['TOKEN']
URL = f'/bot{TOKEN}'

def lambda_handler(event, context):

    print("event :", event) # 들어오는 값 확인용
    print("context :", context) # 들어오는 값 확인용

    request = json.loads(event['body']) # 사용자에게서 들어오는 event['body']
    message_id = ""
    table_number = ""

    # json 문법 체크
    if request.get('callback_query'): # 버튼 눌렀을때
        command = request["callback_query"]["data"]
        message_id = request["callback_query"]["message"]["message_id"]
        sender_name = request["callback_query"]["from"]["first_name"]

    elif request.get('message'): # 메세지를 받았을때
        command = request["message"]["text"]
        sender_name = request["message"]["from"]["first_name"]

    # command 가공 부분
    if len(command) == 5 and (command[:4] == '/vip' or command[:4] == '/boo' or command[:4] == '/std' or command[:4] == '/bar'):
        table_number = command[1:]
        command = '/add'
        
    bot = Bot(URL, command, sender_name, message_id, table_number)

    command_file = bot.check_json()

    if request.get('callback_query') and command_file != None:
        bot.ft_response('/editMessageText', command_file)
    elif request.get('message') and command_file != None:
        bot.ft_response("/sendMessage", command_file)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }