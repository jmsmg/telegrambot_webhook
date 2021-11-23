import http.client # HTTP 프로토콜의 클라이언트 역할
import json
import os # lambda 환경변수


# 전역변수 설정 시작 #
TELEGRAM_API_HOST = 'api.telegram.org' # 호스트 주소
TOKEN = os.environ['TOKEN']
URL = f'/bot{TOKEN}'
headers = {'content-type' : 'application/json'}
connection = http.client.HTTPSConnection(TELEGRAM_API_HOST) # 호스트 주소 접속 객체 생성
# 전역변수 설정 끝 #

def lambda_handler(event, context):

    request_body = json.loads(event['body'])
    # 파라미터 #
    param = {
        'chat_id' : os.environ['CHAT_ID'],
        'text' : request_body['message']['text']
    }

    ## 요청 ##
    connection.request('POST', f'{URL}/sendMessage', json.dumps(param) , headers)
    ## 요청 끝 ##

    ## 응답 ##
    res = connection.getresponse()
    ## 응답 끝 ##

    # 강제 연결 종료 (비정상적인 요청 대비)#
    connection.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }