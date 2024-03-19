import threading

'''
Гонка данных
'''

counter = 0


def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1
    print(f'Значение счётчика: {counter:_}')


threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()

print(f'Значение счётчика в финале: {counter:_}')