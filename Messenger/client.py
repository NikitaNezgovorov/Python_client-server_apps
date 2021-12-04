# -*- coding: utf8 -*-
import sys
import json
import socket
import time
import logging
import logs.config_client_log
from сommon.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP_ADDRESS, \
    DEFAULT_PORT, ADDRESS, PORT

from сommon.utils import get_message, send_message

LOGGER = logging.getLogger('client')


class Client:
    def __init__(self):
        try:
            self.server_address = sys.argv[1]
            self.server_port = int(sys.argv[2])
            LOGGER.info(f'Запущен клиент с параметрами: адрес сервера: '
                        f'{self.server_address}, порт: {self.server_port}')
            if self.server_port < 1024 or self.server_port > 65535:
                LOGGER.critical(
                    f'Попытка запуска клиента с неподходящим номером порта: {self.server_port}. '
                    f'Допустимы адреса с 1024 до 65535. Клиент завершается.')
                sys.exit(1)
        except IndexError:
            self.server_address = DEFAULT_IP_ADDRESS
            self.server_port = DEFAULT_PORT

        self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.transport.connect((self.server_address, self.server_port))
        self.message_to_server = self.create_presence()
        send_message(self.transport, self.message_to_server)
        try:
            self.answer = self.server_answer(get_message(self.transport))
            LOGGER.info(f'Принят ответ от сервера {self.answer}')
        except(ValueError, json.JSONDecodeError):
            LOGGER.error('Не удалось декодировать полученную Json строку.')
        except ConnectionRefusedError:
            LOGGER.critical(f'Не удалось подключиться к серверу {self.server_address}:{self.server_port}, '
                            f'конечный компьютер отверг запрос на подключение.')

    @staticmethod
    def server_answer(message):
        LOGGER.debug(f'Разбор сообщения от сервера: {message}')
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return f'200 : OK\nADDRESS : {message[ADDRESS]}\nPORT : {message[PORT]}'
            return f'400 : {message[ERROR]}'

        raise ValueError

    def create_presence(self, account_name='Guest'):
        out = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: account_name
            },
            ADDRESS: self.server_address,
            PORT: self.server_port
        }
        LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
        return out


if __name__ == '__main__':
    Client()
