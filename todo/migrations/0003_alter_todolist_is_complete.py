# Generated by Django 4.2 on 2023-04-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_user_id_todolist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
