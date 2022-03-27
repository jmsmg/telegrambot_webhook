"""
텔레그램 봇 객체
"""

import http.client # HTTP 프로토콜의 클라이언트 역할
import json
import os

_TELEGRAM_API_HOST = "api.telegram.org/" # 호스트 주소
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

    def send_message(self, teleRes:json) -> None:
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

        if teleRes['message']['text'] == '/table':
            _CONNECTION.request('POST', f'{_URL}/sendMessage', json.dumps(param) , _HEADERS)

        # 응답
            res = _CONNECTION.getresponse()

        # 강제 연결 종료 (비정상적인 요청 대비)#
            _CONNECTION.close()