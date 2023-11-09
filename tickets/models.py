from django.db import models

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=50)
    date = models.DateField()
    
class Guest(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    
class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservation')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reservation')
