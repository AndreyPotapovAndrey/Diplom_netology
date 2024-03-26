# Создание базы дынных в терминале проекта:
`psql createdb -U username namedb` - Переходим в клиент для создания базы данных от имени пользователя
'username' с названием 'namedb'

# Cкрипт создания DRF-проекта:
* *`django-admin startproject backend`* - Создание проекта под названием 'backend'
* *`python manage.py startapp automatic_purchases`* - Создание пиложения 'automatic_purchases'
* *`python -m venv venv`* - Создание 'виртуального окружения проекта'
* *`venv\Scripts\activate.bat`* - Активация 'виртуального окружения проекта' (Windows)
* *`source venv/bin/activate`* - Активация 'виртуального окружения проекта' (Linux, MacOS)
* *`pip install -r requirements.txt`* - Установить зависимости
* *`python manage.py makemigrations`* - Создаём файл миграций
* *`python manage.py migrate`* - Запускаем миграции
* *`python manage.py runserver`* - Запускаем сервер

# Команда запуска контейнера с redis (нужен для работы celery):
### *В терминале, находясь в папке `backend` ввести команду:*
`docker-compose up`

# Команда запуска celery:
### *В терминале, находясь в папке `backend`, ввести команду:*
`celery -A backend  worker --loglevel=info` - флаг `--loglevel=info` нужен для настройки уровня логирования 
при запуске рабочего процесса Celery. Этот флаг устанавливает уровень логирования на "info", что позволяет получать 
оперативные сообщения о работе, включая информацию о выполнении задач, старте и завершении работы рабочих процессов, 
а также другие важные операционные сообщения.

## Для того, чтобы ответ на запрос приходил не в консоль, а на указанную при регистрации пользователя электронную почту нужно:
### *В в файле settings.py изменить настройки следующим образом:*
* *`EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'`* - Раскомментировать и закомментировать 'django.core.mail.backends.console.EmailBackend'
* *`EMAIL_HOST = 'smtp.yandex.ru'`* - SMTP (Simple Mail Transfer Protocol) — это стандартный протокол для отправки электронных писем в Интернете.
* *`EMAIL_PORT = 465`* - Стандартный порт Яндекс-почты 
* *`EMAIL_HOST_USER = 'your_email@yandex.ru'`* - Замените 'your_email@yandex.ru' на ваш реальный адрес электронной почты на Яндексе
* *`EMAIL_HOST_PASSWORD = 'your_password'`* - Замените 'your_password' на ваш реальный пароль электронной почты на Яндексе
* *`EMAIL_PORT = 587`* - Стандартный порт Яндекс_почты
* *`EMAIL_USE_TLS = True`* - Обратите внимание, что в данном случае используется SSL (EMAIL_USE_SSL = True), а не TLS, что является стандартными настройками для Яндекс.Почты.

### Важно!
*Для того, чтобы ответы на запросы приходили на указанную при регистрации эл. почту, вместо пароля непосредственно от почтового ящика,*
*необходимо в личном кабинете Яндекс.Почты создать специальный "пароль для внешних приложений" и указать его в "EMAIL_HOST_PASSWORD = ..."*

## Инструкция для сборки docker-образа:
Чтобы собрать и запустить ваш Docker-образ с использованием docker-compose, следуйте этой пошаговой инструкции.
Это позволит вам запустить ваше Django-приложение вместе с зависимыми сервисами, такими как *PostgreSQL, Redis и Nginx*.

##### *Шаг 1: Подготовка*
Убедитесь, что у вас установлены Docker и Docker Compose на вашей машине. Ваш Dockerfile должен находиться 
в корне проекта, а docker-compose.yml - в соответствующей директории (если docker-compose.yml находится не в корне, 
убедитесь, что вы находитесь в правильной директории при запуске команд).

##### *Шаг 2: Создание .env файла*
Создайте файл .env в корне проекта (или в той же директории, что и docker-compose.yml, если он находится не в корне) и 
определите в нем необходимые переменные окружения, такие как DB_NAME, DB_USER, DB_PASSWORD, SECRET_KEY.

*Файл .env используется для хранения переменных окружения. Это позволяет отделить конфигурационные данные, 
такие как учетные данные для базы данных, ключи API и секретные ключи, от кода приложения.
Такой подход повышает безопасность и упрощает процесс конфигурации приложения 
в различных средах (разработка, тестирование, продакшн), поскольку не требуется изменять код приложения 
для изменения этих настроек.*

Пример содержимого файла .env:
* `DB_NAME=postgres`
* `DB_USER=postgres`
* `DB_PASSWORD=example`
* `SECRET_KEY=your_secret_key`

##### *Шаг 3: Сборка и запуск контейнеров*
Откройте терминал и перейдите в директорию, где находится ваш docker-compose.yml. 
Запустите сборку и запуск контейнеров командой:

*`docker-compose up --build`*

Ключ *`--build`* гарантирует, что Docker соберет образы заново, если это необходимо 
(например, после изменений в Dockerfile или в контексте сборки).

##### Шаг 4: Проверка работоспособности
После успешного запуска, ваше приложение должно быть доступно по адресу http://localhost 
(или http://localhost:8000, если вы настроили порты иначе).

## Дополнительные команды

### Остановка контейнеров: 
Вы можете остановить контейнеры, выполнив 
*`docker-compose down`*

Это остановит и удалит все контейнеры, определенные в docker-compose.yml. 
Для сохранения данных в базе данных убедитесь, что вы используете Docker volumes 
(как указано для PostgreSQL в docker-compose.yml).

### Выполнение миграций Django: 
#### Для выполнения миграций в Django используйте команду:
*`docker-compose run web python manage.py migrate`*

Здесь *`web`* - это имя вашего сервиса Django в docker-compose.yml.

### Сбор статических файлов: 
Если ваше приложение использует статические файлы, выполните:

*`docker-compose run web python manage.py collectstatic --no-input`*

### Следуя этим инструкциям, вы сможете собрать и запустить ваше приложение в Docker-контейнерах, используя docker-compose.

## Также может быть полезным:

*`docker system prune`* — это команда Docker, которая используется для удаления ненужных объектов или данных, 
таких как изображения, контейнеры, тома или сети.