<div align="center">
    <h1>«Атомные привычки»</h1> 
    <p>
        В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
    </p>
   <p>Реализована бэкенд-часть SPA веб-приложения.</p>
</div>

---

## Описание

Настроена CORS.
Настроена интеграция с Телеграмом.
Реализована пагинацию.
Использованы переменные окружения.
Все необходимые модели описаны или переопределены.
Все необходимые эндпоинты реализовали.
Настроены все необходимые валидаторы.
Описанные права доступа заложены.
Настроена отложенная задача через Celery.
Проект покрыт тестами.
Код оформлен в соответствии с лучшими практиками.
Имеется список зависимостей.

---

<div align="center">
    <h3 align="center">
        <p>Использовались языки и инструменты:</p>
        <div>
            <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
            <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
            <img src="https://github.com/devicons/devicon/blob/master/icons/djangorest/djangorest-original-wordmark.svg" title="DRF" alt="DRF" width="40" height="40"/>&nbsp;
            <img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original-wordmark.svg" title="Redis" alt="DRF" width="40" height="40"/>
            <img src="https://badgen.net/badge/C/Celery/green?" title="Celery" alt="DRF" width="40" height="40"/>
        </div>
    </h3>
</div>

---

## Требования

брокер `Redis`

## Локальная установка проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Iv-EN/atomic-habits.git
```

2. Создайте и активируйте виртуальное пространство:

```bash
python3 -m venv venv
```

```bash
sourse venv/bin/activate
```

3. Обновите pip и установите зависимости:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

4. Выполните миграции:

```bash
python manage.py migrate 
```

## Запуск проекта

Для запуска проекта:

брокер `Redis` должен быть запущен

1. Запустите обработчик очереди
   Windows

```bash
celery -A config worker -l INFO -P eventlet
```

Linux

```bash
celery -A config worker -l INFO
```

2. Запустите планировщик Celery beat

```bash
celery -A config beat -l INFO  
```

3. Запустите проект

```bash
python3 manage.py runserver
```

Документация:

```
http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/
```

___

<h3 align="center">
    <p><img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="30" height="30" style="margin-right: 10px;">Автор: Евгений Иванов. </p>
</h3>
<p align="center">
     <div align="center"  class="icons-social" style="margin-left: 10px;">
            <a href="https://vk.com/engenivanov" target="blank" rel="noopener noreferrer">
                <img src="https://img.shields.io/badge/%D0%92%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%B5-blue?style=for-the-badge&logo=VK&logoColor=white" alt="В контакте Badge"/>
            </a>
            <a href="https://t.me/IvENauto" target="blank" rel="noopener noreferrer">
                <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
            </a>
    </div>
