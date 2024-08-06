# Generated by Django 5.0.7 on 2024-08-06 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_game_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
