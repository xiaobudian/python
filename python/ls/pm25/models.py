from django.db import models

# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
        
class City(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=10)
   
class Town(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=10)
    
class Weather(models.Model):
#    pass
    date = models.CharField(max_length=20,blank=True)    

class Air(models.Model):
    time = models.CharField(max_length=20,blank=True)
    weather = models.ForeignKey(Weather)
