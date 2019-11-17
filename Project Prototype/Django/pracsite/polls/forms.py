from django import forms
from polls.models import *


class AddForm(forms.Form):
    #fields for interpreters, clients, content, students
    CATEGORY_CHOICES= [
    ('interpreters', 'Interpreters'),
    ('ind_cust', 'Individual Customer'),
    ('company', 'Company'),
    ('content', 'Content'),
    ('students', 'Students'),
    ('project', 'Project'),
    ('call', 'Call Record'),
    ]
    mode = forms.CharField(label='Category',
                           widget=forms.Select(choices=CATEGORY_CHOICES))


class InterpreterForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    gender = forms.CharField(label='Gender',
                             widget=forms.Select(choices=GENDER_CHOICES))
    mobile_no = forms.CharField(label='Mobile Number')
    nic_no = forms.CharField(label='CNIC Number')
    address = forms.CharField(label='Address')

    class Meta:
        model = interpreter
        fields = ('name', 'age', 'nic_no', 'address', 'mobile_no',
                  'gender', 'calls_served', 'average_rating', 'date_of_joining')


class CustomerForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    gender = forms.CharField(label='Gender',
                             widget=forms.Select(choices=GENDER_CHOICES))
    mobile_no = forms.CharField(label='Mobile Number')
    nic_no = forms.CharField(label='CNIC Number')
    address = forms.CharField(label='Address')

    class Meta:
        model = customer
        fields = ('name', 'age', 'nic_no', 'address', 'mobile_no',
                  'gender', 'date_of_joining')


class CompanyForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    address = forms.CharField(label='Address')
    poc_name = forms.CharField(label='PoC Name')
    poc_mobile_no = forms.CharField(label='PoC Mobile Number')

    class Meta:
        model = company
        fields = ('name', 'address', 'poc_name',
                  'poc_mobile_no', 'date_of_joining')


class ContentForm(forms.ModelForm):
    title = forms.CharField(label='Title')
    link = forms.CharField(label='Link')
    date_of_release = forms.DateField(label='Date of Release')
    

class StudentsForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    mobile_no = forms.CharField(label='Mobile Number')
    level = forms.CharField(label='Level')
    classification = forms.CharField(label='Classification')
    occupation = forms.CharField(label='Occupation')
    city = forms.CharField(label='City')
    batch_no = forms.IntegerField(label='Batch Number')


class ProjectForm(forms.ModelForm):
    interpreter_name = forms.CharField(label='Name')
    client_name = forms.CharField(label='Client')
    date = forms.DateField(label='Date')
    start_time = forms.TimeField(label='Start Time')
    end_time = forms.TimeField(label='End Time')
    payment = forms.CharField(label='Payment')
    payment_status = forms.BooleanField(label='Payment Status', required=False)

class CallForm(forms.ModelForm):
    name = forms.CharField(label='Name')

class SearchForm(forms.ModelForm):
    name = forms.CharField(label='Name/Title')
    CATEGORY_CHOICES= [
    ('interpreters', 'Interpreters'),
    ('ind_cust', 'Individual Customer'),
    ('company', 'Company'),
    ('content', 'Content'),
    ('students', 'Students'),
    ('project', 'Project'),
    ('call', 'Call Record'),
    ]
    mode = forms.CharField(label='Category', 
    widget=forms.Select(choices=CATEGORY_CHOICES))
