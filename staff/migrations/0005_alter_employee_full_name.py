# Generated by Django 4.0.1 on 2022-01-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_employee_department_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='full_name',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
