from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_length=100, decimal_places=2, max_digits=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.IntegerField()
    description = models.TimeField()
    size = models.DecimalField(decimal_places=2, max_digits=100)
    age_limited = models.BooleanField()
    buyer = models.ManyToManyField(Buyer, related_name='правобладатель')

    def __str__(self):
        return self.name

# Buyer.objects.create(name='Vasya', balance='1.1', age='20')

# python manage.py makemigrations blog
# python manage.py sqlmigrate blog 0001
# python manage.py migrate