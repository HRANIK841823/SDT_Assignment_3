# Generated by Django 5.1 on 2024-09-06 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcategory',
            name='task',
        ),
    ]
