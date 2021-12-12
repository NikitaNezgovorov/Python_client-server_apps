# -*- coding: utf8 -*-
import socket
import sys
import json
import сommon.variables
import logging
import logs.config_server_log
from сommon.utils import get_message, send_message

LOGGER = logging.getLogger('server')


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
                LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта {self.listen_port}. '
                                f'Допустимы адреса с 1024 до 65535.')
                sys.exit(1)
        except IndexError:
            LOGGER.critical('После параметра -\'p\' необходимо указать номер порта.')
            sys.exit(1)

        # Затем загружаем какой адрес слушать

        try:
            if '-a' in sys.argv:
                self.listen_address = sys.argv[sys.argv.index('-a') + 1]
            else:
                self.listen_address = ''

        except IndexError:
            LOGGER.critical('После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
            sys.exit(1)

        LOGGER.info(f'Запущен сервер, порт для подключений: {self.listen_port}, адрес,'
                    f' с которого принимаются подключения: {self.listen_address}. '
                    f'Если адрес не указан, принимаются соединения с любых адресов.')
        # Готовим сокет

        self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.transport.bind((self.listen_address, self.listen_port))

        # Слушаем порт

        self.transport.listen(сommon.variables.MAX_CONNECTIONS)

        while True:
            self.client, self.client_address = self.transport.accept()
            LOGGER.info(f'Установлено соединение с ПК {self.client_address}')
            try:
                self.message_from_client = get_message(self.client)
                LOGGER.debug(f'Получено сообщение {self.message_from_client}')
                print(self.message_from_client)
                self.response = self.process_client_message(self.message_from_client)
                LOGGER.info(f'Сформирован ответ клиенту {self.response}')
                send_message(self.client, self.response)
                LOGGER.debug(f'Соединение с клиентом {self.client_address} закрывается.')
                self.client.close()
            except (ValueError, json.JSONDecodeError):
                LOGGER.error(f'Не удалось декодировать Json строку, '
                             f'полученную от клиента {self.client_address}. Соединение закрывается.')
                self.client.close()

    def process_client_message(self, message):
        LOGGER.debug(f'Разбор сообщения от клиента : {message}')
        if сommon.variables.ACTION in message and message[
            сommon.variables.ACTION] == сommon.variables.PRESENCE and сommon.variables.TIME in message \
                and сommon.variables.USER in message and message[сommon.variables.USER][сommon.variables.ACCOUNT_NAME] \
                == 'Guest':
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
