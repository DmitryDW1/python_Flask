# Задание №1
# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте потоки.


import requests
from threading import Thread
from pathlib import Path
import time

urls = [
    'https://proglib.io/p/django-s-nulya-chast-1-pishem-mnogopolzovatelskiy-blog-dlya-kluba-lyubiteley-zadach-python-2022-06-06',
    'https://habr.com/ru/articles/749142/',
    'https://jino.ru/spravka/hosting/articles/django_app.html',
    'https://gb.ru/notification',
    'https://code.visualstudio.com/docs/python/editing#_importresolvefailure',
    'https://www.anekdot.ru/',
    'https://github.com/leshchenko1979/fast_bitrix24',
    'https://products.aspose.com/html/ru/net/generators/',
    'https://aclips.ru/grid-component-bitrix24/',
    'https://vk.com/'
]

PATH = Path('./Seminar4/homework/threads/')


def download(url):
    """
    Скачивание файлов по ссылке
    """
    if Path(PATH).exists() == False: 
        Path.mkdir(PATH)
        
    start_time = time.time()
    response = requests.get(url)
    filename = 'thread_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open((str(PATH) + '/' + filename), 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f'Скачивание файла по ссылке {url} завершено за {time.time() - start_time:.2f} секунд(ы)')
        

def create_threadings():
    """
    Создаются потоки
    """
    threads = []
    for url in urls:
        thread = Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
        
    for thread in threads:
            thread.join()
            
            
if __name__ == '__main__':
    create_threadings()