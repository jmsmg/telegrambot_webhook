import http.client # HTTP 프로토콜의 클라이언트 역할
import json

# 변수 설정 시작 #

TELEGRAM_API_HOST = 'api.telegram.org' # 호스트 주소
TOKEN = '##'

# 변수 설정 끝 #

## 호스트 주소 접속 객체 생성 ##
connection = http.client.HTTPSConnection(TELEGRAM_API_HOST)

# sendmessage 함수 url #
url = f'/bot{TOKEN}'

headers = {'content-type' : 'application/json'}

# 파라미터 #
param = {
    'chat_id':'###',
    'text':'hello'
}

# http #

## 요청 ##
connection.request('POST', f'{url}/sendMessage', json.dumps(param) , headers)
## 요청 끝 ##

## 응답 ##
res = connection.getresponse()
## 응답 끝 ##

## response body 출력 ##
print(json.dumps(json.loads(res.read().decode()), indent=4))
print('상태코드 : ', res.status)
print('메시지 : ', res.msg)

# 연결 종료 #
connection.close()