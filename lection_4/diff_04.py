import asyncio
import aiohttp

import time

'''
Асинхронный подход. Скорость сравнима с многопроцессорным подходом,
но используется только один процесс, соответсвенно затрачивается 
меньше ресурсов машины
'''

urls = [
    'https://proglib.io/p/django-s-nulya-chast-1-pishem-mnogopolzovatelskiy-blog-dlya-kluba-lyubiteley-zadach-python-2022-06-06',
    'https://habr.com/ru/articles/749142/',
    'https://jino.ru/spravka/hosting/articles/django_app.html',
    'https://gb.ru/notification',
    'https://code.visualstudio.com/docs/python/editing#_importresolvefailure'
]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'async_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')
        
        
async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    
        
start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())