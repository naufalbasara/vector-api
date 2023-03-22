from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=45)
    username = models.TextField(max_length=30)
    password = models.TextField()

class Product(models.Model):
    name = models.TextField(max_length=45)
    category = models.TextField(max_length=45)
    bldc = models.TextField(max_length=45)
    power = models.IntegerField()
    torque = models.IntegerField()
    top_speed = models.IntegerField()
    load_weight = models.IntegerField()
    range = models.IntegerField()
    usage = models.IntegerField()
    cycle_life = models.TextField(max_length=45)
    battery_capacity = models.IntegerField()
    battery_design = models.IntegerField()
    image = models.ImageField()
    last_edited = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    