"""
메인함수로 직접 구동되는 lambda_handler부분
"""

import http.client # HTTP 프로토콜의 클라이언트 역할
import json
import os
import answer

TELEGRAM_API_HOST = "api.telegram.org" # 호스트 주소
HEADERS = {'content-type' : 'application/json'}
CONNECTION = http.client.HTTPSConnection(TELEGRAM_API_HOST) # 호스트 주소 접속 객체 생성
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
<<<<<<< HEAD

    command_file = {
        '/table' : answer.table,
        '/vip' : answer.vip_button,
        '/boo' : answer.booth_button,
        '/std' : answer.std_button,
        '/bar' : answer.bar_button,
        '/add' : answer.add_bottle,
        '0' : answer.cancel
        }
    
    command_file.get(command)
=======
        
    bot = Bot(URL, command, sender_name, message_id, table_number)

    command_file = bot.check_json()
>>>>>>> e838db428581b75eab27482c53126270919d631a

    if request.get('callback_query') and command_file != None:
        response = '/editMessageText'
    elif request.get('message') and command_file != None:
        response = '/sendMessage'
    
    command_file["text"] = f'호출자 : {sender_name}'
    command_file["message_id"] = message_id
        
    CONNECTION.request('POST', f'{URL}{response}', json.dumps(command_file) , HEADERS)

    # 응답
    res = CONNECTION.getresponse()
            
    # 강제 연결 종료 (비정상적인 요청 대비)#
    CONNECTION.close()


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }