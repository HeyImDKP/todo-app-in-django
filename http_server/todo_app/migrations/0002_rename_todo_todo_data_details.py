# Generated by Django 4.2.12 on 2024-06-27 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo_data',
            old_name='todo',
            new_name='details',
        ),
    ]
