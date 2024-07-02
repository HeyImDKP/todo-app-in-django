# Generated by Django 4.2.12 on 2024-06-26 08:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('todo', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
