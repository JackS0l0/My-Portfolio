# Generated by Django 5.1.5 on 2025-01-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_articles_adverttrendbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='advertTrendTxt',
            field=models.TextField(default='Trend', verbose_name='Məqalə başlığı Trend üçün'),
        ),
    ]
