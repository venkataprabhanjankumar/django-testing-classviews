# Generated by Django 4.1 on 2022-08-18 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 18, 16, 36, 694788)),
        ),
    ]