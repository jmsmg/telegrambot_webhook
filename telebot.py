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
    
    def get_command(self, command:str) -> None:

        with open(f'param{command}.json') as f:
            param = json.loads(f.read())
        
            if command == '/table':
                self.send_message(param)
        
            elif command == '/photo':
                self.send_photo(param)

    def send_message(self, param) -> None:
        """
        명령어에 맞춰서 문자를 반환하는 함수
        """

        _CONNECTION.request('POST', f'{_URL}/sendMessage', json.dumps(param) , _HEADERS)

        # 응답
        res = _CONNECTION.getresponse()

        # 강제 연결 종료 (비정상적인 요청 대비)#
        _CONNECTION.close()


    def send_photo(self, param) -> None:
        """
        명령어에 맞춰서 사진 반환하는 함수
        """

        _CONNECTION.request('POST', f'{_URL}/sendPhoto', json.dumps(param) , _HEADERS)

        # 응답
        res = _CONNECTION.getresponse()

        # 강제 연결 종료 (비정상적인 요청 대비)#
        _CONNECTION.close()