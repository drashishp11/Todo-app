# Generated by Django 4.2 on 2023-04-15 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks_todo',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
