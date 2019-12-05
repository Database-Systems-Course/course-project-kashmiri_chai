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
        fields = ('name', 'age', 'address', 'mobile_no',
                  'gender', 'date_of_joining')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('name', 'address', 'mobile_no',
                  'gender', 'date_of_joining')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ('name', 'address', 'PoC_Name',
                  'PoC_Mobile_No', 'date_of_joining')


class ContentForm(forms.ModelForm):
    class Meta:
        model = content
        fields = ('title', 'interpreter', 'link', 'date_of_release')


class StudentsForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('name', 'age', 'gender', 'mobile_no', 'city',
                  'level', 'classification', 'occupation', 'trainer')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ('Interpreter', 'Client', 'Date', 'StartTime', 'Location', 'Purpose',
                  'EndTime', 'Payment', 'PaymentStatus')


class CallForm(forms.ModelForm):
    class Meta:
        model = call
        fields = ('Interpreter', 'Customer', 'StartTime', 'EndTime',
                  'Reason', 'Comments', 'CustomerRating', 'InterpreterRating')


class SearchForm(forms.Form):
    CATEGORY_CHOICES = [
        ('interpreters', 'Interpreters'),
        ('ind_cust', 'Individual Customers'),
        ('company', 'Companies'),
        ('content', 'Content'),
        ('students', 'Students'),
        ('project', 'Projects'),
        ('call', 'Call Records'),
    ]
    mode = forms.CharField(label='SELECT * FROM',
                           widget=forms.Select(choices=CATEGORY_CHOICES,
                                               attrs={"onChange": 'populate()',
                                                      "id": "modeField"}))

    searchBy = forms.CharField(label="WHERE",
                               widget=forms.Select(attrs={"id": "searchBy", "width": "100px"}))

    name = forms.CharField(label='LIKE', required=False, widget=forms.TextInput(attrs={"onChange": 'validate()',
                                                                                    "id": "id_name"}))


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
