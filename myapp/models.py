from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField("Full Name :",max_length=200,null=True)
    city = models.CharField(max_length=100,null=True)
    GENDER = (
        ('Male','Male'), 
        ('Female','Female'),
        ('Others','Others')
    )
    gender = models.CharField(max_length=10, choices=GENDER, default='Male')

    CITY = (
        ('Baroda','Baroda'),
        ('Surat','Surat'),
        ('Ahmedabad','Ahmedabad')
    )
    city = models.CharField(max_length=100,choices =CITY, default='Baroda')
    contactno = models.IntegerField(null=True)
    zipcode = models.IntegerField(null=True)

    def __str__(self):
        return  f"{self.name}"

class PersonSalary(models.Model):
    userperson = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name="Person Data :")
    salary = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.userperson} salary : {self.salary}"


