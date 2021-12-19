"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""

import locale
import os
import socket
import subprocess
from ipaddress import ip_address

address_list = ['yandex.ru', '8.8.8.8', '192.168.1.75', '192.168.1.223']


def address_check(host):
    try:
        checked_ip = str(ip_address(host))
    except ValueError:
        try:
            checked_ip = str(ip_address(socket.gethostbyname(host)))
        except socket.gaierror:
            print(f'Адрес хоста {host} задан неверно')
            return False
    return checked_ip


def host_ping(adr_list):
    result = []
    for host in adr_list:
        ip = address_check(host)
        if ip:
            with open(os.devnull, 'w') as DNULL:

                response = subprocess.call(
                    ['ping', '-n', '2', '-w', '2', ip], stdout=DNULL
                )
            if response == 0:
                result.append(('Доступен', str(host), f'[{ip}]'))
                continue

        result.append(('Недоступен', str(host), f'[{ip}]'))
    return result


if __name__ == '__main__':
    for i in host_ping(address_list):
        print(f'{i[0].ljust(11)} {i[1].ljust(15)} {i[2]}')
