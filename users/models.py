from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, RegexValidator
from django.db import models


class User(AbstractUser):
    first_name = models.CharField("Имя", max_length=150, blank=True)
    last_name = models.CharField("Фамилия", max_length=150, blank=True)
    middle_name =models.CharField("Отчество", max_length=150, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    room = models.IntegerField("Номер комнаты", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    HOSTELS = [
        (1, "Первое общежитие"),
        (2, "Второе общежитие"),
        (3, "Третье общежитие"),
        (4, "Четвертое общежитие"),
    ]
    hostel_number = models.IntegerField("Номер общежития", null=True, blank=True, choices=HOSTELS, default=True)
    contract_number = models.IntegerField("Номер договора", null=True, blank=True)
    email = models.EmailField("Почта", blank=True, validators=[EmailValidator])
    phoneNumberRegex = RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    sso_points = models.IntegerField("Количество баллов ССО", null=True, blank=True)
    administrative_points = models.IntegerField("количество административных баллов", null=True, blank=True)
    is_verificated = models.BooleanField("Подвтержден ли пользователь", default=False,
                                         help_text="Подтвержден ли пользователь старостой этажа")
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"