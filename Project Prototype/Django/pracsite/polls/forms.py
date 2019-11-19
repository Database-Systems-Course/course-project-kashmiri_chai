from django import forms
from polls.models import *


class AddForm(forms.Form):
    # fields for interpreters, clients, content, students
    CATEGORY_CHOICES = [
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
    class Meta:
        model = interpreter
        fields = ('name', 'age', 'nic_no', 'address', 'mobile_no',
                  'gender', 'date_of_joining')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('name', 'age', 'nic_no', 'address', 'mobile_no',
                  'gender', 'date_of_joining')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ('name', 'address', 'poc_name',
                  'poc_mobile_no', 'date_of_joining')


class ContentForm(forms.ModelForm):
    class Meta:
        model = content
        fields = ('title', 'interpreter', 'link', 'date_of_release')


class StudentsForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('name', 'age', 'gender', 'mobile_no', 'city',
                  'level', 'classification', 'occupation', 'batch_no', 'trainer')


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

class SearchForm(forms.Form):
    name = forms.CharField(label='Name/Title')
    CATEGORY_CHOICES = [
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
