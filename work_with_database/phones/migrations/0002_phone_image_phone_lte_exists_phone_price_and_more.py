# Generated by Django 5.0.6 on 2024-06-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.URLField(default=None, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=None, verbose_name='lte_exists'),
        ),
        migrations.AddField(
            model_name='phone',
            name='price',
            field=models.IntegerField(default=None, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(default=None, verbose_name='release_date'),
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=2, unique=True, verbose_name='slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(default=None, max_length=50, unique=True, verbose_name='name'),
        ),
    ]