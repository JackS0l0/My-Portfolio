# Generated by Django 5.1.5 on 2025-01-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_advertleftbox_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='advertTrendTxt',
            field=models.TextField(default='Trend', verbose_name='Trend'),
        ),
    ]
