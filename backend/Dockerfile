# Используем официальный образ Python как базовый
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Обновляем pip и setuptools
RUN pip install --upgrade pip setuptools

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]