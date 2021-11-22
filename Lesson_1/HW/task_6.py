"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet.universaldetector import UniversalDetector

file = 'text.txt'
STR_LIST = ['сетевое программирование', 'сокет', 'декоратор']

# Запись текстового файла
with open(file, 'w', encoding='UTF-8') as f:
    for i in STR_LIST:
        f.write(f'{i}\n')

# Проверка кодировки файла
detector = UniversalDetector()
with open(file, 'rb') as f:
    for line in f:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(detector.result)

# Чтение файла в Unicode
with open(file, 'r', encoding=detector.result['encoding']) as f:
    for line in f:
        print(line)
