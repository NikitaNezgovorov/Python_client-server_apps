# -*- coding: utf8 -*-
"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json

from chardet import UniversalDetector

file = 'orders.json'


def write_order_to_json(item, quantity, price, buyer, date):
    with open(file, 'r', encoding='UTF-8') as f_n:
        dict_to_json = json.load(f_n)
        print(dict_to_json)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    with open(file, 'w', encoding='UTF-8') as f_w:
        json.dump(dict_to_json, f_w, indent=4)


write_order_to_json('Стол', '50', '110', 'Nick', '21/11/2022')
write_order_to_json('Стул', '1', '120', 'Nick', '21/11/2022')
write_order_to_json('Кровать', '500', '12100', 'Nick', '21/11/2022')
write_order_to_json('Шкаф', '200', '100', 'Nick', '21/11/2022')
