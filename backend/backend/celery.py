from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE для 'backend.settings'
# Указание на то, где находится модуль настроек нашего проекта (settings.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

# Загрузка настроек Celery из настроек Django
# Celery будет искать все настройки, начинающиеся с префикса "CELERY_"
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач из всех зарегистрированных приложений Django
app.autodiscover_tasks()