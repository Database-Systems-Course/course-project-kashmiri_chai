from django.db import models
import datetime

timeChoices = [(datetime.time(x, y), "{0}:{1}".format(x if x > 9 else "0"+str(
    x), y if y > 9 else "0"+str(y))) for x in range(0, 24) for y in range(0, 60, 30)]

RATING = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]

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

ADDRESS_CHOICES = [
    ('Baldia Town', 'Baldia Town',),
    ('Bin Qasim Town', 'Bin Qasim Town'),
    ('Gadap Town', 'Gadap Town'),
    ('Gulberg Town', 'Gulberg Town'),
    ('Gulshan Town', 'Gulshan Town'),
    ('Jamshed Town', 'Jamshed Town'),
    ('Kemari Town', 'Kemari Town'),
    ('Korangi Town', 'Korangi Town'),
    ('Landhi Town', 'Landhi Town'),
    ('Liaquatabad Town', 'Liaquatabad Town'),
    ('Lyari Town', 'Lyari Town'),
    ('Malir Town', 'Malir Town'),
    ('New Karachi Town', 'New Karachi Town'),
    ('North Nazimabad Town', 'North Nazimabad Town'),
    ('Orangi Town', 'Orangi Town'),
    ('Saddar Town', 'Saddar Town'),
    ('Shah Faisal Town', 'Shah Faisal Town'),
]

PAYMENT_CHOICES = [
    ('cash', 'Cash'),
    ('bank transfer', 'Bank Transfer'),
    ('cheque', 'Cheque'),

]

REASON_CHOICES = [
    ('personal', 'Personal'),
    ('govt/admin', 'Governmental/Administrative'),
    ('job', 'Employment Related'),
    ('emergency', 'Emergency'),
    ('food', 'Food Delivery/Order'),
    ('education', 'Educational Institution'),
    ('finance', 'Financial Institution'),
    ('info', 'Request for Information'),
]


class interpreter(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=200)
    calls_served = models.IntegerField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name


class customer(models.Model):
    name = models.CharField(max_length=50)
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
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_no = models.IntegerField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    classification = models.CharField(max_length=50, choices=CLASS_CHOICES)
    occupation = models.CharField(max_length=20)
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    trainer = models.ForeignKey(interpreter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class call(models.Model):
    Interpreter = models.ForeignKey(interpreter, on_delete=models.CASCADE)
    Customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    StartTime = models.TimeField(choices=timeChoices)
    EndTime = models.TimeField(choices=timeChoices)
    Reason = models.CharField(max_length=250, choices=REASON_CHOICES)
    Comments = models.CharField(max_length=200, blank=True)
    CustomerRating = models.IntegerField(choices=RATING)
    InterpreterRating = models.IntegerField(choices=RATING)

    def __str__(self):
        return self.Customer + " called " + self.Interpreter + " for " + self.Rea


class rate(models.Model):
    rate = models.IntegerField()
    StartDate = models.DateField()
    EndDate = models.DateField()

    def __str__(self):
        return self.rate + " from " + self.StartDate + " to " + self.EndDate


class project(models.Model):
    Interpreter = models.ManyToManyField(interpreter)
    Client = models.ForeignKey(company, on_delete=models.CASCADE)
    Date = models.DateField()
    StartTime = models.TimeField(choices=timeChoices)
    EndTime = models.TimeField(choices=timeChoices)
    Location = models.CharField(max_length=200)
    Purpose = models.CharField(max_length=200)
    Payment = models.IntegerField()
    PaymentStatus = models.BooleanField(default=False)


class transaction(models.Model):
    rate = models.OneToOneField(rate, on_delete=models.CASCADE)
    project = models.OneToOneField(project, on_delete=models.CASCADE)
    client = models.OneToOneField(company, on_delete=models.CASCADE)
    dueDate = models.DateField()
    ModeOfPayment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
