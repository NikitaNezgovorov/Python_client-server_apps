"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""


def test_to_convert_to_bytes(items):
    for i in items:
        try:
            el = eval(f"b'{i}'")
        except SyntaxError:
            print(f'Error to convert: "{i}"')


LIST_STR = ["attribute", "класс", "функция", "type"]

test_to_convert_to_bytes(LIST_STR)
