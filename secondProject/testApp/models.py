from django.db import models

# Create your models here.
class Fruits(models.Model):
    fname=models.CharField(max_length=15)
    fprice=models.FloatField()
    fqty=models.IntegerField()
    fqlity=models.CharField(max_length=10)
    color=models.CharField(max_length=20)
