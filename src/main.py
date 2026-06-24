import os
from dotenv import load_dotenv

# 1. Загружаем переменные из файла .env в окружение
load_dotenv()

def print_author():
    # 2. Читаем переменную AUTHOR из окружения
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

# Вызываем функцию для проверки
if __name__ == "__main__":
    print_author()
