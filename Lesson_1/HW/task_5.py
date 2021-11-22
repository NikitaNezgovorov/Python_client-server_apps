"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
 в строковый тип на кириллице.
"""
import platform
import subprocess
import chardet


def ping_url(urls):
    code = '-n' if platform.system() == 'Windows' else '-c'
    for url in urls:
        args = ['ping', code, '5', url]
        ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in ping.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('UTF-8')
            print(line.decode('UTF-8'))


URLS = ['yandex.ru', 'youtube.com']

ping_url(URLS)
