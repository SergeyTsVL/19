# Generated by Django 4.2.11 on 2024-08-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0009_alter_buyer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
