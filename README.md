## Marlin - Get Ready To Rock!

<br>

# Создание и активация виртуальной среды Python
<pre>python -m venv env0</pre>
<pre>activate env0</pre>
<pre>pip install -r req.txt</pre>

# Создание и проведение миграций (VENV req)
> Нужно делать, если производились измения в моделях
<pre>python manage.py makemigrations</pre>
<pre>python manage.py migrate</pre>

аргс:
+    --fake &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Если накосячили с миграциями и не нужно делать изменения в самой БД


# Запуск веб-сервера (VENV req)
> отладка дев версии
<pre>python manage.py runserver</pre>

аргс:
+    0.0.0.0:80  &nbsp;&nbsp;&nbsp;&nbsp;Запускаем на определенном локальном адресе, Порт 80 
+    --no-reload     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Без перезагрузки в случае изменений в коде
+    --insecure     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Запуск без JS скриптов


# Запуск Jupyter-notebook из под джанги (VENV req)
<pre>python manage.py shell_plus --notebook</pre>
