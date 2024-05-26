from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='car_photos/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)