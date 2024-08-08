from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_length=100, decimal_places=2, max_digits=100)
    age = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.IntegerField()
    description = models.CharField(max_length=100)
    size = models.DecimalField(decimal_places=2, max_digits=100)
    age_limited = models.BooleanField()
    buyer = models.ManyToManyField(Buyer, related_name='правобладатель')

    def __str__(self):
        return self.title

# python manage.py makemigrations
# python manage.py sqlmigrate blog
# python manage.py migrate