# Generated by Django 3.2.6 on 2021-08-09 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apidemo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]
