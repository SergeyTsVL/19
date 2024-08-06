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
    description = models.CharField(max_length=1000)
    size = models.DecimalField(decimal_places=2, max_digits=100)
    age_limited = models.BooleanField()
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title


