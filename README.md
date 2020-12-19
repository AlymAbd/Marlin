# Marlin - Get Ready To Rock!

> Создание и активация виртуальной среды Python
python -m venv env0
activate env0
pip install -r req.txt


> Создание и проведение миграций (VENV req)
# Нужно делать, если производятся измения в моделях
python manage.py makemigrations
python manage.py migrate

аргс:
    --fake          #Если накосячили с миграциями и не нужно делать изменения в самой БД


> Запуск веб-сервера (VENV req)
# отладка дев версии
python manage.py runserver

аргс:
    --host 0.0.0.0  #Запускаем на определенном локальном адресе
    --port 80       #Порт 
    --no-reload     #Без перезагрузки в случае изменений в коде


> Запуск Jupyter-notebook из под джанги (VENV req)
python manage.py shell_plus --notebook