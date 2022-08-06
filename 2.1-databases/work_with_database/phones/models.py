from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=64, verbose_name='Модель')
    image = models.ImageField(upload_to='img/', verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    release_date = models.DateField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='LTE')
    slug = models.SlugField(max_length=64, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name
