from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models


class User(AbstractUser):
    first_name = models.CharField("Имя", max_length=150, blank=True)
    last_name = models.CharField("Фамилия", max_length=150, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    room = models.IntegerField("Номер комнаты", null=True, blank=True)
    hostel_number = models.IntegerField("Номер общежития", null=True, blank=True)
    contract_number = models.IntegerField("Номер договора", null=True, blank=True)
    email = models.EmailField("Почта", blank=True, validators=[EmailValidator])
    phone_number = models.IntegerField("Номер телефона", null=True, blank=True)
    sso_points = models.IntegerField("Количество баллов ССО", null=True, blank=True)
    administrative_points = models.IntegerField("количество административных баллов", null=True, blank=True)
    is_verificated = models.BooleanField("Подвтержден ли пользователь", default=False,
                                         help_text="Подтвержден ли пользователь старостой этажа")
