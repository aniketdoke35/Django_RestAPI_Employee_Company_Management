from django.db import models

# Create your models here.ca

#company Model
class Company(models.Model):
    Comapany_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100 ,choices=(('IT','IT'),
                                                     ('Non IT','Non IT'),
                                                     ('Mobiles phone','Mobile phone')
                                                     ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):

       return self.name + " - "+  self.location


#Employee Models
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    about = models.CharField(max_length=200)
    position = models.CharField(max_length=50,choices=(
        ('manager','manager'),
        ('software developer','software developer'),
        ('project leader','project leader')
        ))
    
    Company=models.ForeignKey(Company,on_delete=models.CASCADE)