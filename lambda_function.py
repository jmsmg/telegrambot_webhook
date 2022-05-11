"""
메인함수로 직접 구동되는 lambda_handler부분
"""

import http.client # HTTP 프로토콜의 클라이언트 역할
import json
import os
import answer
import table_db

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
    add_bottle = ""

    # json 문법을 체크하여 명령어가 들어오는지, 아니면 버튼을 눌렀을때인지 판별
    if request.get('callback_query'): # 버튼 눌렀을때
        data = request["callback_query"]["data"]
        message_id = request["callback_query"]["message"]["message_id"]
        sender_name = request["callback_query"]["from"]["first_name"]

    elif request.get('message'): # 메세지를 받았을때
        data = request["message"]["text"]
        sender_name = request["message"]["from"]["first_name"]

    command_file = {
        '/table' : answer.table,
        '/vip' : answer.vip_button,
        '/boo' : answer.booth_button,
        '/std' : answer.std_button,
        '/bar' : answer.bar_button,
        '/add' : answer.transfer_json(data[1:5]),
        '0' : answer.cancel,
        '1' : answer.complete,
        }

    command_file = command_file.get(data)
    print(command_file)

    # command 가공 부분
    # 테이블 번호 눌렀을때
    if len(data) == 5 and (data[:4] == '/vip' or data[:4] == '/boo' or data[:4] == '/std' or data[:4] == '/bar'):
        table_number = data[1:5]
        command_file = answer.transfer_json(table_number)
    # 바틀명 눌렀을떄
    elif len(data) > 5 and (data[:4] == '/vip' or data[:4] == '/boo' or data[:4] == '/std' or data[:4] == '/bar'):
        table_number = data[1:5]
        command_file = answer.transfer_json(table_number)
        add_bottle = data[6:]

    if request.get('callback_query') and command_file != None:
        response = '/editMessageText'
        command_file["message_id"] = message_id
    elif request.get('message') and command_file != None:
        response = '/sendMessage'

    command_file["text"] = f'''호출자 : {sender_name}
테이블 : {table_number} 
추가된 술 : {add_bottle} ''' # TODO 테이블 넘버(pk)에 일치하는 추가된 술 정보 출력하기

        
    CONNECTION.request('POST', f'{URL}{response}', json.dumps(command_file) , HEADERS)

    # 응답
    CONNECTION.getresponse()
            
    # 강제 연결 종료 (비정상적인 요청 대비)#
    CONNECTION.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
        }