# Создание базы дынных в терминале проекта:
**psql createdb -U username namedb** - `Переходим в клиент для создания базы данных от имени пользователя
'username' с названием 'namedb'`
# Cкрипт создания DRF-проекта:
## *В терминале, находясь в папке backend последовательно ввести команды:*
* **django-admin startproject backend** - `Создание проекта под названием 'backend'`
* **python manage.py startapp automatic_purchases** - `Создание пиложения 'automatic_purchases'`
* **python -m venv venv** - `Создание 'виртуального окружения проекта'`
* **venv\Scripts\activate.bat** - `Активация 'виртуального окружения проекта' (Windows)`
* **source venv/bin/activate** - `Активация 'виртуального окружения проекта' (Linux, MacOS)`
* **pip install -r requirements.txt** - `Установить зависимости`
* **python manage.py makemigrations** - `Создаём файл миграций`
* **python manage.py migrate** - `Запускаем миграции`
* **python manage.py runserver** - `Запускаем сервер`
# Команда запуска контейнера с redis (нужен для работы celery):
## *В терминале, находясь в папке Diplom_netology (корневая папка), ввести команду:*
* **docker-compose up**
# Команда запуска celery:
## *В терминале, находясь в папке backend, ввести команду:*
* **celery -A backend  worker --loglevel=info** - `флаг --loglevel=info нужен для настройки уровня логирования 
при запуске рабочего процесса Celery. Этот флаг устанавливает уровень логирования на "info", что позволяет получать 
оперативные сообщения о работе, включая информацию о выполнении задач, старте и завершении работы рабочих процессов, 
а также другие важные операционные сообщения. `


