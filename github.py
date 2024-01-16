import datetime
import os
import schedule
import time

# Замените эти значения на свои данные
github_token = "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"
repo_url_with_token = f"https://Just-Working8888:{github_token}@github.com/Just-Working8888/Dashboard-V2.git"

def job():
    file_path = '/home/binniev/beka/script.py'

    # Добавление новой строки с текущей датой
    new_line = f"# New line for {datetime.datetime.now()}\n"
    with open(file_path, 'a') as file:
        file.write(new_line)

    # Изменить URL репозитория на версию с токеном (только первый раз)
    os.system(f'git -C /home/binniev/beka remote set-url origin {repo_url_with_token}')

    # Команды Git для добавления, коммита и пуша изменений
    os.system(f'git -C /home/binniev/beka add {file_path}')
    os.system(f'git -C /home/binniev/beka commit -m "Add new line for {datetime.datetime.now().date()}"')
    os.system('git -C /home/binniev/beka push')

# Запланировать выполнение функции job каждую минуту
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)