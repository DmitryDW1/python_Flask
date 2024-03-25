# Задание №6
# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте асинхронный подход.

import asyncio
from pathlib import Path
from os import path, walk
import time


PATH = Path('./Seminar4/homework/async/')

async def process_file(file):
    start_time = time.time()
    
    with open (file, 'r', encoding='utf-8') as f:
        contents = len((f.read()).split())
        print(f'Файл {f.name.split('\\')[-1]} в директории {PATH} содержит {contents} слов')
        print(f'Посчитано за {time.time() - start_time:.2f} секунды')
        
async def main(user_dir):
    tasks = []
    for root, dirs, files in walk(user_dir):
        for file in files:
            file_path = path.join(root, file)
            task = asyncio.ensure_future(process_file(file_path))
            tasks.append(task)
    await asyncio.gather(*tasks)
    
if __name__ == '__main__':
    asyncio.run(main(PATH))