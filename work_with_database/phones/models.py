from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=50, unique=True, verbose_name='name', default=None)
    price = models.IntegerField(verbose_name='price', default=None)
    image = models.URLField(max_length=200, verbose_name='image', default=None)
    release_date = models.DateField(verbose_name='release_date', default=None)
    lte_exists = models.BooleanField(verbose_name='lte_exists', default=None)
    slug = models.SlugField(verbose_name='slug', unique=True, default=name)
