from django.db import models

# Create your models here.
class admin_info(models.Model):
    username = models.CharField(max_length=30,default='',null=False)
    password = models.CharField(max_length=30,default='',null=False)
    first_name = models.CharField(max_length=30,default='',null=False)
    last_name = models.CharField(max_length=30,default='',null=False)
    mobile_no = models.CharField(max_length=30,default='',null=False)
    
class client_info(models.Model):
    username = models.CharField(max_length=30,default='',null=False)
    password = models.CharField(max_length=30,default='',null=False)
    first_name = models.CharField(max_length=30,default='',null=False)
    last_name = models.CharField(max_length=30,default='',null=False)
    mis = models.CharField(max_length=30,default='',null=False)
    branch = models.CharField(max_length=30,default='',null=False)
    college_email = models.CharField(max_length=30,default='',null=False)
    mobile_no = models.CharField(max_length=30,default='',null=False)
    book1_id = models.CharField(max_length=30,default='',null=False)
    date_of_issue1 = models.CharField(max_length=30,default='',null=False)
    date_of_return1 = models.CharField(max_length=30,default='',null=False) 
    book2_id = models.CharField(max_length=30,default='',null=False)
    date_of_issue2 = models.CharField(max_length=30,default='',null=False)
    date_of_return2 = models.CharField(max_length=30,default='',null=False)

class books(models.Model):
    book_name = models.CharField(max_length=30,default='',null=False)
    author1 = models.CharField(max_length=30,default='',null=False)
    author2 = models.CharField(max_length=30,default='',null=False)
    author3 = models.CharField(max_length=30,default='',null=False)
    book_id = models.CharField(max_length=30,default='',null=False)
    Availability = models.CharField(max_length=30,default='',null=False)