from django.conf import settings
from django.db import models


class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор", related_name="news")
    title = models.CharField("Заголовок новости", max_length=15)
    description = models.TextField("Описание", max_length=400)
    date_published = models.DateTimeField("Дата публикации", auto_now=True)
    hostel_number = models.IntegerField("Номер общежития")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="newsimages/")

    class Meta:
        verbose_name = "Картинка новости"
        verbose_name_plural = "Картинки новостей"
