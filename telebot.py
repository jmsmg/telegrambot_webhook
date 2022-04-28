"""
텔레그램 봇 객체
"""

import http.client # HTTP 프로토콜의 클라이언트 역할
import json
import os

_TELEGRAM_API_HOST = "api.telegram.org" # 호스트 주소
_HEADERS = {'content-type' : 'application/json'}
_CONNECTION = http.client.HTTPSConnection(_TELEGRAM_API_HOST) # 호스트 주소 접속 객체 생성

class Bot:
    def __init__(self, URL, command):
        """
        인스턴스 초기화
        """
        self._URL = URL
        self._command = command
    
    def check_json(self) -> None:
        if self._command == '/table':
            command_file = 'param/table.json'

        elif self._command == 'vip':
            command_file = 'param/button_data_vip.json'
        elif self._command == 'boo':
            command_file = 'param/button_data_boo.json'
        elif self._command == 'std':
            command_file = 'param/button_data_std.json'
        elif self._command == 'bar':
            command_file = 'param/button_data_bar.json'
        
        # TODO 정규표현식 add_bottle 처리
        elif self._command == 'add':
            command_file = 'param/add_bottle.json'
        
        return command_file


    def ft_response(self, response, command_file) -> None:
        """
        명령어에 맞춰서 문자를 반환하는 함수
        """
        with open(command_file) as f:
            param = json.loads(f.read())

        _CONNECTION.request('POST', f'{self._URL}{response}', json.dumps(param) , _HEADERS)

        # 응답
        res = _CONNECTION.getresponse()
            
        # 강제 연결 종료 (비정상적인 요청 대비)#
        _CONNECTION.close()