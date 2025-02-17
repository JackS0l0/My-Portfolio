# Generated by Django 5.1.5 on 2025-01-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articles_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='advertLeftBox',
            field=models.BooleanField(default=False, verbose_name='Sol qutu'),
        ),
        migrations.AddField(
            model_name='articles',
            name='advertRightBottomLeftBox',
            field=models.BooleanField(default=False, verbose_name='Sağ alt, sol qutu'),
        ),
        migrations.AddField(
            model_name='articles',
            name='advertRightBottomRightBox',
            field=models.BooleanField(default=False, verbose_name='Sağ alt, sağ qutu'),
        ),
        migrations.AddField(
            model_name='articles',
            name='advertRightTopBox',
            field=models.BooleanField(default=False, verbose_name='Sağ üst qutu'),
        ),
        migrations.AddField(
            model_name='articles',
            name='complated',
            field=models.BooleanField(default=False, verbose_name='Təhvil verildi'),
        ),
        migrations.AddField(
            model_name='articles',
            name='sale',
            field=models.BooleanField(default=False, verbose_name='Endirim'),
        ),
    ]
