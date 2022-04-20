"""
텔레그램 봇 객체
"""

import http.client # HTTP 프로토콜의 클라이언트 역할
import json
import re

_TELEGRAM_API_HOST = "api.telegram.org" # 호스트 주소
_HEADERS = {'content-type' : 'application/json'}
_CONNECTION = http.client.HTTPSConnection(_TELEGRAM_API_HOST) # 호스트 주소 접속 객체 생성

class Bot:

    def __init__(self, URL):
        """
        인스턴스 초기화
        """
        self._URL = URL

    def find_method(self, command):
        if command == '/table' or command == '/task' :
            return '/sendMessage'

        elif command == '/photo':
            return '/sendPhoto'

        else: # 정규표현식으로 변경해야함
            return '/editMessageText'

    # def check_data(self, data):
    #     if data == '0'
    #         pass 
    #     elif data == 'vi'
    #         pass
    #     elif data == 'bo'
    #         pass
    #     elif data == 'st'
    #         pass
    #     elif data == 'ba'
    #         pass
    
    def ft_response(self, response, sender_name, command) -> None:
        """
        명령어에 맞춰서 문자를 반환하는 함수
        """

        with open(f'param{command}.json') as f:
            param = json.loads(f.read())
            param["text"] = f"호출자 : {sender_name}"

        _CONNECTION.request('POST', f'{self._URL}{response}', json.dumps(param) , _HEADERS)

        # 응답
        res = _CONNECTION.getresponse()

        # 강제 연결 종료 (비정상적인 요청 대비)#
        _CONNECTION.close()