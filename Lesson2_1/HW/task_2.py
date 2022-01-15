"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
import task_1
from ipaddress import ip_network


def host_range_ping(network):
    try:
        hosts = list(map(str, ip_network(network).hosts()))
    except ValueError as e:
        print(e)
    else:
        count = 255
        for host in task_1.host_ping(hosts):
            if not count:
                break
            count -= 1
            print(host)


if __name__ == '__main__':
    host_range_ping('192.168.1.0/28')
