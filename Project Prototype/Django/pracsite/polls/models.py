from django.db import models


class interpreter(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=200)
    calls_served = models.IntegerField(blank = True, null=True)
    average_rating = models.FloatField(blank = True, null=True)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

class customer(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=200)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

class company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    PoC_Name = models.CharField(max_length=50)
    PoC_Mobile_No = models.IntegerField()
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

class content(models.Model):
    title = models.CharField(max_length=100)
    interpreter = models.ForeignKey(interpreter, on_delete=models.CASCADE)
    link = models.URLField(max_length=100)
    date_of_release = models.DateField()

    def __str__(self):
        return self.title

class student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    CITY_CHOICES = [
        ('karachi', 'Karachi'),
        ('lahore', 'Lahore'),
        ('islamabad', 'Islamabad'),
    ]
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('professional', 'Professional'),
    ]
    CLASS_CHOICES = [
        ('family', 'Family'),
        ('friend', 'Friend'),
        ('special educator', 'Special Educator'),
    ]
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length = 5, choices=GENDER_CHOICES)
    mobile_no = models.IntegerField()
    level = models.CharField(max_length = 20, choices=LEVEL_CHOICES)
    classification = models.CharField(max_length=50, choices=CLASS_CHOICES)
    occupation = models.CharField(max_length=20)
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    batch_no = models.IntegerField()
    trainer = models.ForeignKey(interpreter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class call(models.Model):
    Interpreter= models.ForeignKey(interpreter, on_delete=models.CASCADE)
    Customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Reason = models.CharField(max_length=250)
    CustomerRating = models.IntegerField()
    InterpreterRating = models.IntegerField()

class project(models.Model):
    Interpreter = models.ForeignKey(interpreter, on_delete=models.CASCADE)
    Client = models.ForeignKey(company, on_delete=models.CASCADE)
    Date = models.DateField()
    StartTime = models.DateField()
    EndTime = models.DateField()
    Payment = models.IntegerField()
    PaymentStatus = models.BooleanField(default=False)

class rate(models.Model):
    rate = models.IntegerField()
    StartDate = models.DateField()
    EndDate = models.DateField()

class transaction(models.Model):
    rate = models.ForeignKey(rate, on_delete=models.CASCADE)
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    