# Generated by Django 4.0.2 on 2022-02-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='onhome',
            field=models.BooleanField(default=False),
        ),
    ]
