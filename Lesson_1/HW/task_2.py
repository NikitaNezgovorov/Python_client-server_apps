"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
 (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""


def convert_to_bytes(items):
    for i in items:
        el = eval(f"b'{i}'")
        print(el)
        print(f'type of element {i} after convert {type(el)}')
        print(f'length of element{i} in bytes {len(el)}')
        print("*" * 100)


LIST_STR = ["class", "function", "method"]

convert_to_bytes(LIST_STR)
