import asyncio
from pathlib import Path

'''
Разделение задач между корутинами для чтения содержимого каталога.
Работают одновременно, не мешая друг другу, каждая 
отвечает за чтение своего файла
'''

async def process_file(file_path):
    with open (file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(f'{f.name} содержит <<<{contents[:13]}...>>>')
        
        
        
async def main():
    dir_path = Path('.')
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    tasks = [asyncio.create_task(process_file(file_path)) for file_path in file_paths]
    await asyncio.gather(*tasks)
    
    
if __name__ == '__main__':
    asyncio.run(main())
