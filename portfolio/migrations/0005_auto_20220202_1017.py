# Generated by Django 3.2.8 on 2022-02-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20220201_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='mobile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='others',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='web',
            field=models.BooleanField(default=False),
        ),
    ]
