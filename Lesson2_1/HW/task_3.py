"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам,
представленным в табличном формате (использовать модуль tabulate).
"""
from tabulate import tabulate
from task_1 import host_ping
from ipaddress import ip_network


def host_range_ping_tab(network):
    table = [('Доступные', 'Недоступные')]
    sort = [[], []]
    try:
        hosts = list(map(str, ip_network(network).hosts()))
    except ValueError as e:
        print(e)
    else:
        result = host_ping(hosts)
        for host in result:
            if len(host[0]) == 8:
                sort[0].append(f'{host[1].ljust(15)} {host[2]}')
            else:
                sort[1].append(f'{host[1].ljust(15)} {host[2]}')
        table.extend(list(zip(*sort)))
        if len(sort[0]) > len(sort[1]):
            for item in sort[0][len(sort[1]):]:
                table.append((item, None))
        elif len(sort[0]) < len(sort[1]):
            for item in sort[1][len(sort[0]):]:
                table.append((None, item))
        print(tabulate(table, headers='firstrow', stralign='center',
                       tablefmt='pipe'))


if __name__ == '__main__':
    host_range_ping_tab('192.168.1.0/28')
