from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@shared_task  # Декоратор @shared_task превращает функцию send_email_task в задачу Celery.
# Это позволяет вызывать эту функцию асинхронно.
def send_email_task(subject, message, recipient):
    """
    A Celery task to send an email.
    """
    email = EmailMultiAlternatives(
        subject=subject,  # Тема
        body=message,  # Текст сообщения
        from_email=settings.EMAIL_HOST_USER,
        to=[recipient]  # Получатель
    )
    email.send()  # Отправляет созданное электронное письмо.
    # Этот метод асинхронно вызывается, когда задача Celery выполняется.


# from celery import shared_task
# from django.core.mail import send_mail
#
# @shared_task
# def send_email_task(to_email):
#     send_mail(
#         'Тема вашего письма',
#         'Содержание вашего письма.',
#         'from@example.com',
#         [to_email],
#         fail_silently=False,
#     )

