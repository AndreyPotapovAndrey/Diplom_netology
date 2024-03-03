from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django_rest_passwordreset.signals import reset_password_token_created
from automatic_purchases.models import ConfirmEmailToken, User
from .tasks import send_email_task  # Import the Celery task

new_user_registered = Signal()

new_order = Signal()

@receiver(reset_password_token_created)
# Декоратор @receiver позволяет "подписаться" на сигнал reset_password_token_created
# Т.е. функция password_reset_token_created будет вызвана каждый раз, когда генерируется токен для сброса пароля.

def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    # Sends an email with the password reset token.
    """
    sender: класс, отправивший сигнал.
    instance: экземпляр класса, который отправил сигнал.
    reset_password_token: объект токена, который был создан.
    ** kwargs: дополнительные ключевые аргументы.

    """

    # В момент генерации токена, создается объект
    # ResetPasswordToken, который содержит сам токен, ссылку на пользователя,
    # для которого он был создан, и другую метаинформацию,
    # такую как время создания. Этот объект используется для контроля процесса сброса пароля.


    subject = f"Password Reset Token for {reset_password_token.user}"
    # "reset_password_token.user" ссылается на атрибут объекта reset_password_token (user),
    # который представляет пользователя, связанного с данным токеном сброса пароля.
    # Объект reset_password_token создается библиотекой django-rest-passwordreset
    # в момент генерации токена сброса пароля.
    message = reset_password_token.key  # Сохраняем ключ токена сброса пароля в переменную message,
    # чтобы использовать его в теле письма.
    recipient = reset_password_token.user.email  # Извлекаем адрес электронной почты пользователя,
    # для которого был создан токен, и сохраняет его в переменной recipient.
    send_email_task.delay(subject, message, recipient)  # Use the Celery task
    # метод .delay(), который планирует отправку электронного письма.

@receiver(post_save, sender=User)
# @receiver - это декоратор, который используется для регистрации функции как обработчика сигнала.
# В данном случае, функция new_user_registered_signal будет зарегистрирована как обработчик сигнала.
# post_save - это сигнал, отправляемый после сохранения объекта в базу данных.
# В данном случае, он отправляется после сохранения объекта User.
# Сигнал должен быть обработан только если отправителем является модель User

def new_user_registered_signal(sender, instance, created, **kwargs):
    # Функция будет вызвана при активации сигнала.
    # created - булево значение, указывающее, был ли объект создан (True) или обновлен (False)
    """
    Sends an email with the confirmation token when a new user is registered.
    """
    if created and not instance.is_active:
    #  Проверяем, был ли пользователь только что создан(created равно True)
    #  и не активирован(instance.is_active равно False)
        token, _ = ConfirmEmailToken.objects.get_or_create(user_id=instance.pk)
    # Создается или получается токен подтверждения электронной почты для нового пользователя
    # Возвращаемое значение _ игнорируется
        subject = f"Password Reset Token for {instance.email}"
        message = token.key
        recipient = instance.email  # instance является экземпляром модели User,
        # который был только что сохранен (создан или обновлен) в базе данных.
        send_email_task.delay(subject, message, recipient)  # Use the Celery task

@receiver(new_order)
def new_order_signal(user_id, **kwargs):
    """
    Sends an email when a new order is placed.
    """
    user = User.objects.get(id=user_id)
    subject = "Order Status Update"
    message = "Your order has been placed."
    recipient = user.email
    send_email_task.delay(subject, message, recipient)  # Use the Celery task

# from typing import Type
#
# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import post_save
# from django.dispatch import receiver, Signal
# from django_rest_passwordreset.signals import reset_password_token_created
#
# from automatic_purchases.models import ConfirmEmailToken, User
#
# new_user_registered = Signal()
#
# new_order = Signal()

# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
#     """
#     Отправляем письмо с токеном для сброса пароля
#     When a token is created, an e-mail needs to be sent to the user
#     :param sender: View Class that sent the signal
#     :param instance: View Instance that sent the signal
#     :param reset_password_token: Token Model Object
#     :param kwargs:
#     :return:
#     """
#     # send an e-mail to the user
#
#     msg = EmailMultiAlternatives(
#         # title:
#         f"Password Reset Token for {reset_password_token.user}",
#         # message:
#         reset_password_token.key,
#         # from:
#         settings.EMAIL_HOST_USER,
#         # to:
#         [reset_password_token.user.email]
#     )
#     msg.send()


# @receiver(post_save, sender=User)
# def new_user_registered_signal(sender: Type[User], instance: User, created: bool, **kwargs):
#     """
#      отправляем письмо с подтрердждением почты
#     """
#     if created and not instance.is_active:
#         # send an e-mail to the user
#         token, _ = ConfirmEmailToken.objects.get_or_create(user_id=instance.pk)
#
#         msg = EmailMultiAlternatives(
#             # title:
#             f"Password Reset Token for {instance.email}",
#             # message:
#             token.key,
#             # from:
#             settings.EMAIL_HOST_USER,
#             # to:
#             [instance.email]
#         )
#         msg.send()
#
#
# @receiver(new_order)
# def new_order_signal(user_id, **kwargs):
#     """
#     отправяем письмо при изменении статуса заказа
#     """
#     # send an e-mail to the user
#     user = User.objects.get(id=user_id)
#
#     msg = EmailMultiAlternatives(
#         # title:
#         f"Обновление статуса заказа",
#         # message:
#         'Заказ сформирован',
#         # from:
#         settings.EMAIL_HOST_USER,
#         # to:
#         [user.email]
#     )
#     msg.send()

