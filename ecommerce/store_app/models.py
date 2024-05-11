from django.db import models

# Create your models here.
class Product(models.Model):
  Name=models.CharField(max_length=900)
  Price=models.IntegerField(default=0)
  Description=models.CharField(max_length=300)
  Photo=models.ImageField(upload_to='images')
  
  def __str__(self):
    return self.Name