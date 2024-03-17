import requests
import time
import threading

'''
Многопоточный подход
'''

urls = [
    'https://proglib.io/p/django-s-nulya-chast-1-pishem-mnogopolzovatelskiy-blog-dlya-kluba-lyubiteley-zadach-python-2022-06-06',
    'https://habr.com/ru/articles/749142/',
    'https://jino.ru/spravka/hosting/articles/django_app.html',
    'https://gb.ru/notification',
    'https://code.visualstudio.com/docs/python/editing#_importresolvefailure'
]


def download(url):
    response = requests.get(url)
    filename = 'thread_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')
        
        
threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()