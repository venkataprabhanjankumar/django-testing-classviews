# Generated by Django 4.1 on 2022-08-18 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 12, 48, 4, 602716, tzinfo=datetime.timezone.utc)),
        ),
    ]
