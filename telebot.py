"""
텔레그램 봇 객체
"""

import http.client # HTTP 프로토콜의 클라이언트 역할
import json
import os

_TELEGRAM_API_HOST = "api.telegram.org" # 호스트 주소
_TOKEN = os.environ['TOKEN']
_URL = f'/bot{_TOKEN}'
_HEADERS = {'content-type' : 'application/json'}
_CONNECTION = http.client.HTTPSConnection(_TELEGRAM_API_HOST) # 호스트 주소 접속 객체 생성

class Bot:
    def __init__(self):
        """
        인스턴스 초기화
        """
        self._URL = _URL

    def send_message(self, command:string) -> None:
        """
        명령어에 맞춰서 문자를 반환하는 함수
        """
        param = {
            'chat_id' : os.environ['CHAT_ID'],
            'text' : '테이블판',
            "reply_markup": {
                "inline_keyboard": [[
                    {
                        "text": "VIP",
                        "callback_data": "A1"            
                    }, 
                    {
                        "text": "B",
                        "callback_data": "C1"            
                    }]
                ]
            }
        }

        if command == '/table':
            _CONNECTION.request('POST', f'{_URL}/sendMessage', json.dumps(param) , _HEADERS)

        # 응답
            res = _CONNECTION.getresponse()

        # 강제 연결 종료 (비정상적인 요청 대비)#
            _CONNECTION.close()

    def send_photo(self, command:string) -> None:
        """
        명령어에 맞춰서 사진 반환하는 함수
        """
        param = {
            'chat_id' : os.environ['CHAT_ID'],
            'photo' : 'https://avatars.githubusercontent.com/u/77792994?v=4'
        }

        if command == '/photo':
            _CONNECTION.request('POST', f'{_URL}/sendPhoto', json.dumps(param) , _HEADERS)

        # 응답
            res = _CONNECTION.getresponse()

        # 강제 연결 종료 (비정상적인 요청 대비)#
            _CONNECTION.close()
    