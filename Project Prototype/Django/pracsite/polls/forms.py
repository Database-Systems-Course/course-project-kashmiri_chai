from django import forms

class AddForm(forms.Form):
    #fields for interpreters, clients, content, students
    CATEGORY_CHOICES= [
    ('interpreters', 'Interpreters'),
    ('ind_cust', 'Individual Customer'),
    ('company', 'Company'),
    ('content', 'Content'),
    ('students', 'Students'),
    ]
    mode = forms.CharField(label='Category', 
    widget=forms.Select(choices=CATEGORY_CHOICES))

class InterpreterForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = forms.CharField(label='Name')
    age = forms.CharField(label='Age')
    gender = forms.CharField(label='Gender',
    widget=forms.Select(choices=GENDER_CHOICES))
    mobile_no = forms.CharField(label='Mobile Number')
    nic_no = forms.CharField(label='CNIC Number')
    address = forms.CharField(label='Address')

class CustomerForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = forms.CharField(label='Name')
    age = forms.CharField(label='Age')
    gender = forms.CharField(label='Gender',
    widget=forms.Select(choices=GENDER_CHOICES))
    mobile_no = forms.CharField(label='Mobile Number')
    nic_no = forms.CharField(label='CNIC Number')
    address = forms.CharField(label='Address')

class CompanyForm(forms.Form):
    name = forms.CharField(label='Name')
    address = forms.CharField(label='Address')
    poc_name = forms.CharField(label='PoC Name')
    poc_mobile_no = forms.CharField(label='PoC Mobile Number')

class ContentForm(forms.Form):
    title = forms.CharField(label='Title')
    link = forms.CharField(label='Link')
    date_of_release = forms.DateField(label='Date of Release')
    

class StudentsForm(forms.Form):
    name = forms.CharField(label='Name')
    age = forms.CharField(label='Age')
    mobile_no = forms.CharField(label='Mobile Number')
    level = forms.CharField(label='Level')
    classification = forms.CharField(label='Classification')
    occupation = forms.CharField(label='Occupation')
    city = forms.CharField(label='City')
    batch_no = forms.CharField(label='Batch Number')

class SearchForm(forms.Form):
    name = forms.CharField(label='Name/Title')
    CATEGORY_CHOICES= [
    ('interpreters', 'Interpreters'),
    ('ind_cust', 'Individual Customer'),
    ('company', 'Company'),
    ('content', 'Content'),
    ('students', 'Students'),
    ]
    mode = forms.CharField(label='Category', 
    widget=forms.Select(choices=CATEGORY_CHOICES))
    
    
