# Generated by Django 5.0.3 on 2024-04-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_customuser_is_active_alter_employee_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name="employee",
            name="is_active",
            field=models.BooleanField(default=None),
        ),
    ]
