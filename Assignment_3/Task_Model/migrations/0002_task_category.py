# Generated by Django 5.1 on 2024-09-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Category', '0002_remove_taskcategory_task'),
        ('Task_Model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='Task_Category.taskcategory'),
        ),
    ]
