from django.db import models


class interpreter(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile_no = models.IntegerField()
    nic_no = models.IntegerField()
    address = models.CharField(max_length=200)
    calls_served = models.IntegerField()
    average_rating = models.FloatField()
    date_of_joining = models.DateField()

class customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile_no = models.IntegerField()
    nic_no = models.IntegerField()
    address = models.CharField(max_length=200)
    date_of_joining = models.DateField()

class company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    poc_name = models.CharField(max_length=50)
    poc_mobile_no = models.IntegerField()
    date_of_joining = models.DateField()