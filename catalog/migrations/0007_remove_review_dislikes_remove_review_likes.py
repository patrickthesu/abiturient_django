# Generated by Django 4.1.3 on 2023-03-15 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_faculty_dean'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='review',
            name='likes',
        ),
    ]