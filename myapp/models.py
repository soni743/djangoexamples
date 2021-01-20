from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=100,null=True)
    contactno = models.IntegerField(null=True)
    zipcode = models.IntegerField(null=True)

    def __str__(self):
        return  f"{self.name}, city is {self.city}"

