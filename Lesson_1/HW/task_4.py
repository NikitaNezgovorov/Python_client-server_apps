"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""


def encode_decode(items):
    for i in items:
        el_bytes = i.encode(encoding='UTF-8', errors='strict')
        print(el_bytes)
        el_decode = el_bytes.decode(encoding='UTF-8', errors='strict')
        print(el_decode)


list_str = ["разработка", "администрирование", "protocol", "standard"]

encode_decode(list_str)