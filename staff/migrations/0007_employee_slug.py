# Generated by Django 4.0.1 on 2022-01-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_rename_department_department_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]