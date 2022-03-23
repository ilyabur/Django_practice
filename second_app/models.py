from django.db import models

# Create your models here.

class Articles(models.Model): # создаем таблицу базы данных
    title = models.CharField("Заголовок", max_length=50) # заголовок
    anons = models.CharField("Анонс", max_length=250) # анонс статьи
    full_text = models.TextField("Статья") # статья
    date = models.DateTimeField("Дата публикации") # дата и время

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

