# Generated by Django 4.2.11 on 2024-08-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0008_delete_registration_buyer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
