from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField("Full Name :",max_length=200,null=True)
    # city = models.CharField(max_length=100,null=True,verbose_name="City :")
    GENDER = (
        ('Male','Male'), 
        ('Female','Female'),
        ('Others','Others')
    )
    gender = models.CharField(max_length=10, choices=GENDER, default='Male',verbose_name="Gender :")

    CITY = (
        ('','Select'),
        ('Baroda','Baroda'),
        ('Surat','Surat'),
        ('Ahmedabad','Ahmedabad')
    )
    city = models.CharField(max_length=100,choices =CITY, default='Baroda',verbose_name="City")
    contactno = models.IntegerField(null=True,verbose_name="Contact No. :")
    zipcode = models.IntegerField(null=True,verbose_name="Zip Code :")
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return  f"{self.name}"

    def ImageUrl(self):
        try:
            url = self.img.url
        except:
            url ='../static/images/noimg.jpg'            

        return url            

class PersonSalary(models.Model):
    userperson = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name="Person Name :", default=None, null=True)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.userperson} salary : {self.salary}"

class Contact(models.Model):
    name = models.CharField(max_length=200,null=True,verbose_name="Full Name :")        
    email = models.EmailField(max_length=200,verbose_name="Email :")
    PURPOSE=(
        ('Purpose1','Purpose1'),
        ('Purpose2','Purpose2')
    )
    purpose = models.CharField(choices=PURPOSE,max_length=200,verbose_name='Purpose :')
    msg = models.TextField(max_length=1000,null=True)


