# Задание №4
# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте потоки.

import threading
from os import path, walk
from pathlib import Path

PATH = Path('./Seminar4/homework/threads/')

def process_file(file):
    """
    Подсчет количества слов в файлах
    """
    with open (file, 'r', encoding='utf-8') as f:
        contents = len((f.read()).split())
        print(f'Файл {f.name.split('\\')[-1]} в директории {PATH} содержит {contents} слов')
    

def threads_counter(user_dir):
    """
    Запуск потоков
    """
    threads = []
    for root, dirs, files in walk(user_dir):
        for file in files:
            file_path = path.join(root, file)
            t = threading.Thread(target=process_file, args=(file_path, ))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()
        
       
if __name__ == '__main__':
    threads_counter(PATH) 

    
    