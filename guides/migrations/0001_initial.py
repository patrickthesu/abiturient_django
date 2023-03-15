# Generated by Django 4.1.3 on 2023-03-15 11:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите короткое название гайда', max_length=200, verbose_name='Название')),
                ('template', models.FileField(upload_to='guides/templates', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['html'])], verbose_name='Прикрепить шаблон')),
            ],
        ),
    ]