<div align="center">
    <h1>«Атомные привычки»</h1> 
    <p>
        В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
    </p>
   <p>Реализована бэкенд-часть SPA веб-приложения.</p>
</div>

---

## Описание

- Настроена CORS.
- Настроена интеграция с Телеграмом.
- Реализована пагинация.
- Использованы переменные окружения.
- Все необходимые модели описаны или переопределены.
- Все необходимые эндпоинты реализованы.
- Настроены все необходимые валидаторы.
- Описанные права доступа заложены.
- Настроена отложенная задача через Celery.
- Проект покрыт тестами.
- Код оформлен в соответствии с лучшими практиками.
- Имеется список зависимостей.
- Созданы образы и запущены контейнеры Docker.
- Создано и запущено мультиконтейнерное приложение.

---

<div align="center">
    <h3 align="center">
        <p>Использовались языки и инструменты:</p>
        <div>
            <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
            <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
            <img src="https://github.com/devicons/devicon/blob/master/icons/djangorest/djangorest-original-wordmark.svg" title="DRF" alt="DRF" width="40" height="40"/>&nbsp;
            <img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original-wordmark.svg" title="Redis" alt="Redis" width="40" height="40"/>
            <img src="https://badgen.net/badge/C/Celery/green?" title="Celery" alt="Celery" width="40" height="40"/>
            <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original-wordmark.svg" title="Docker" alt="Docker" width="40" height="40"/>
        </div>
    </h3>
</div>

---

Сейчас проект доступен на сервере 158.160.154.204:8000

Административная панель по адресу 

`http://158.160.154.204:8000/admin/`

Документация:

```
http://158.160.154.204:8000/redoc/
http://158.160.154.204:8000/swagger/
```

---

## Локальная установка проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Iv-EN/atomic-habits.git
```

2. В корне проекта создайте файл `.env` со следующими переменными:
   ```
   SECRET_KEY=... # секретный ключ django-проекта
   DEBUG=False # в режиме отладки рекомендуется указать True
   POSTGRES_DB=... # Имя базы данных
   POSTGRES_USER=... # имя пользователя БД
   POSTGRES_PASSWORD=... # пароль от БД
   DB_HOST=db
   DB_PORT=5432
   TELEGRAM_BOT_TOKEN=... # токен бота в телеграм
   CELERY_OPTIONS=-P eventlet # или не указывайте, если используете Linux
   ```

## Запуск проекта

Для локального запуска проекта:

1. Соберите и запустите контейнеры:
   ```bash
   docker-compose build  
   docker-compose up -d
   ```
   
2. Проверить состояние контейнеров можно командой
   ```bash
   docker ps
   ```
   если в ответе в колонке STATUS для всех контейнеров указано значение `Up`,
   значит всё работает как надо.\
   Пример ответа
   ```
   CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                    NAMES
   d1857a4baa89   ah_backend    "/entrypoint.sh cele…"   15 minutes ago   Up 15 minutes   8000/tcp                 ah_celery
   4b4872e21a1c   ah_backend    "/entrypoint.sh cele…"   15 minutes ago   Up 15 minutes   8000/tcp                 ah_celery_beat
   cb7e9d170028   ah_backend    "/entrypoint.sh pyth…"   15 minutes ago   Up 15 minutes   0.0.0.0:8000->8000/tcp   ah_backend
   99af7e83b2ee   postgres:16   "docker-entrypoint.s…"   2 hours ago      Up 15 minutes   5432/tcp                 ah_db
   f2209a353e8a   redis:7       "docker-entrypoint.s…"   2 hours ago      Up 15 minutes   6379/tcp                 ah_redis
   ```

3. Создайте супер пользователя:
   ```bash
   docker exec -it ah_backend python manage.py createsuperuser 
   ```
Панель администратора Django доступна по адресу:
```
http://127.0.0.1:8000/admin/
```

Документация:

```
http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/
```

---

Подготовка удалённого сервера:
1. Обновление системы на сервере:
   Откройте терминал и выполните команду для обновления списка пакетов:
   ```bash
      sudo apt update
   ```
   Выполните команду для обновления всех установленных пакетов до их последних версий:
   ```bash
      sudo apt upgrade
   ```
   
2. Установка Docker
   Чтобы установить Docker, воспользуйтесь инструкцией по установке с официального сайта: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository.

3. Настройка файрвола
   Сначала проверьте состояние файрвола с помощью команды:
   ```bash
      sudo ufw status
   ```
   Если файрвол отключен, активируйте его:
   ```bash
      sudo ufw enable
   ```
   Теперь откройте необходимые порты:
      Порт 80 для HTTP:
   ```bash
      sudo ufw allow 80/tcp
   ```
      Порт 443 для HTTPS:
   ```bash
      sudo ufw allow 443/tcp
   ```
   Откройте порт 22 для SSH:
   ```bash
      sudo ufw allow 22/tcp
   ```
   Проверьте настройки файрвола:
   ```bash
      sudo ufw status
   ```
   порты 80, 443, 22 должны находиться с состоянии ALLOW 
4. Установка Git:
   ```bash
      sudo apt update
      sudo apt install git
   ```
   создайте и перейдите в директорию, где хотите разместить код приложения
   например ```/var/www```
   Затем выполните команду для клонирования репозитория:
   ```bash
      git clone https://github.com/username/repository.git
   ```
5. Запуск контейнеров
   Перейдите в директорию, где находится ваш файл docker-compose.yml. Например:
   ```bash
      cd /var/www/repository
   ```
   Выполните команду для запуска контейнеров:
   ```bash
      docker-compose up -d
   ```
6. Создайте супер пользователяЖ
   ```bash
      docker-compose exec -it ah_backend bash
      python manage.py createsuperuser
   ```
   или зайдите под суперпользователем по умолчанию `admim@admin.ru` пароль `admin`


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
