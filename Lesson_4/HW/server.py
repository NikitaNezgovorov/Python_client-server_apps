# -*- coding: utf8 -*-
import socket
import sys
import json
import сommon.variables
from сommon.utils import get_message, send_message


class Server:
    def __init__(self):
        '''
        server.py -p 4321 -a 192.168.31.76
        '''

        try:
            if '-p' in sys.argv:
                self.listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            else:
                self.listen_port = сommon.variables.DEFAULT_PORT
            if self.listen_port < 1024 or self.listen_port > 65535:
                raise ValueError
        except IndexError:
            print('После параметра -\'p\' необходимо указать номер порта.')
            sys.exit(1)
        except ValueError:
            print(
                'В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
            sys.exit(1)

        # Затем загружаем какой адрес слушать

        try:
            if '-a' in sys.argv:
                self.listen_address = sys.argv[sys.argv.index('-a') + 1]
            else:
                self.listen_address = ''

        except IndexError:
            print(
                'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
            sys.exit(1)

        # Готовим сокет

        self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.transport.bind((self.listen_address, self.listen_port))

        # Слушаем порт

        self.transport.listen(сommon.variables.MAX_CONNECTIONS)

        while True:
            self.client, self.client_address = self.transport.accept()
            try:
                self.message_from_client = get_message(self.client)
                print(self.message_from_client)
                self.response = self.process_client_message(self.message_from_client)
                send_message(self.client, self.response)
                self.client.close()
            except (ValueError, json.JSONDecodeError):
                print('Принято некорректное сообщение от клиента.')
                self.client.close()

    def process_client_message(self, message):

        if сommon.variables.ACTION in message and message[сommon.variables.ACTION] == сommon.variables.PRESENCE and сommon.variables.TIME in message \
                and сommon.variables.USER in message and message[сommon.variables.USER][сommon.variables.ACCOUNT_NAME] == 'Guest':
            return {
                сommon.variables.RESPONSE: 200,
                сommon.variables.ADDRESS: self.listen_address,
                сommon.variables.PORT: self.listen_port
            }
        return {
            сommon.variables.RESPONSE: 400,
            сommon.variables.ERROR: 'Bad Request'
        }


if __name__ == '__main__':
    Server()
