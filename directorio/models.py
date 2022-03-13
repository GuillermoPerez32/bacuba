from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from mascotas.models import Municipio, Provincia

from django.core import mail
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created
# Create your models here.


class User(AbstractUser):

    adress          = models.CharField(max_length=255, blank=True, default="")
    phone           = models.CharField(max_length=15, blank=True, default="")
    imagen          = models.ImageField(upload_to='users/', blank=True, null=True)
    provincia       = models.CharField(max_length=100, blank=True, default="")
    municipio       = models.CharField(max_length=100, blank=True, default="")
    ci              = models.CharField(max_length=11, blank=True, default="")
    descripcion     = models.CharField(max_length=50, blank=True, default="")
    email           = models.EmailField(_('email address'), unique=True, default="")
    # REQUIRED_FIELDS = [
    #     'adress',
    #     'phone',
    #     'email',
    #     'first_name',
    #     'last_name',
    #     'imagen',
    #     'provincia',
    #     'municipio',
    #     'ci',
    #     'descripcion'
    # ]

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    print(reset_password_token.user.email)
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(
                reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string(
        'email/user_reset_password.html', context)
    email_plaintext_message = render_to_string(
        'email/user_reset_password.txt', context)

    mail.send_mail(
        # title:
        "Password Reset for {title}".format(title="BACuba"),
        # message:
        f'Your Token is:{reset_password_token.key}',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],

        fail_silently = False
    )

