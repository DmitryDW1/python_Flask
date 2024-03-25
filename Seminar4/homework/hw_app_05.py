# Задание №5
# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте процессы.

import multiprocessing
from pathlib import Path
from os import walk, path
import time

PATH = Path('./Seminar4/homework/threads/')

def process_file(file):
    """
    Чтение файла и подсчёт количеста слов
    """
    start_time = time.time()
    
    with open (file, 'r', encoding='utf-8') as f:
        contents = len((f.read()).split())
        print(f'Файл {f.name.split('\\')[-1]} в директории {PATH} содержит {contents} слов')
        print(f'Посчитано за {time.time() - start_time:.2f} секунды')
        
    

def process_counter(user_dir):
    """
    Запуск процессов
    """
    processes = []
    for root, dirs, files in walk(user_dir):
        for file in files:
            file_path = path.join(root, file)
            p = multiprocessing.Process(target=process_file, args=(file_path, ))
            processes.append(p)
            p.start()
    
    for p in processes:
        p.join()
       
if __name__ == '__main__':
    process_counter(PATH) 