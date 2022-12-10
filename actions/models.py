from django.conf import settings
from django.db import models


class Action(models.Model):
    title = models.CharField("Заголовок", max_length=60, null=True, blank=True)
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="action",verbose_name="Пользователь")
    description = models.TextField("Описание", max_length=500)

    class Meta:
        verbose_name = "Активность"
        verbose_name_plural = "Активности"


class ActionImage(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name="images")
    title = models.CharField("Заголовок картинки", max_length=60, null=True, blank=True)
    image = models.ImageField()

    class Meta:
        verbose_name = "Картинка активности"
        verbose_name_plural = "Картинки активности"
