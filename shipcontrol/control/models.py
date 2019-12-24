import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Ship(models.Model):
    name = models.CharField(max_length=30, unique=True)
    flag = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Master(models.Model):
    master = models.ForeignKey(User, related_name='master', on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, related_name='ships', on_delete=models.CASCADE)    
class Cargo(models.Model):
    cargo = models.CharField(max_length=100)
    ship = models.ForeignKey(Ship, related_name='shipname', on_delete=models.CASCADE)
class Remark(models.Model):
    statement = models.TextField(null=True,max_length=4000)
    cargo = models.ForeignKey(Cargo, related_name='cargoinformation', on_delete=models.CASCADE)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    psc = models.ForeignKey(User, related_name='psc', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
class Information(models.Model):
    captain = models.ForeignKey(Master, related_name='captain', on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, related_name='shipinfo', on_delete=models.CASCADE)
    imo = models.CharField(max_length=10)
    mmsi = models.CharField(max_length=10)
    callsign = models.CharField(max_length=7)
    gross = models.CharField(max_length=50)
    deadweight = models.CharField(max_length=50)
    buildyear = models.CharField(max_length=4)
class Engineer(models.Model):
    national = models.CharField(max_length=50)
    limit = models.CharField(max_length=50)

   

