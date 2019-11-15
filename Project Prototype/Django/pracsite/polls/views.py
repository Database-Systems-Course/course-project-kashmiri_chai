from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from polls.forms import *

class IndexView(TemplateView):
    template_name = 'polls/index.html'

class AddView(TemplateView):
    template_name = 'polls/add.html'
    def get(self, request):
        form = AddForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = AddForm(request.POST)
        if form.is_valid():
            #extract data from form
            mode = form.cleaned_data['mode']
            print(mode)
            if mode == "interpreters":
                return redirect('polls:interpreter_view')
            elif mode == "ind_cust":
                return redirect('polls:ind_cust_view')
            elif mode == "company":
                return redirect('polls:company_view')
            elif mode == "content":
                return redirect('polls:content_view')
            elif mode == "students":
                return redirect('polls:students_view')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class SearchView(TemplateView):
    template_name = 'polls/search.html'
    def get(self , request):
        form = SearchForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class InterpreterView(TemplateView):
    template_name = 'polls/interpreter.html'
    def get(self , request):
        form = InterpreterForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = InterpreterForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class CustomerView(TemplateView):
    template_name = 'polls/customer.html'
    def get(self , request):
        form = CustomerForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class CompanyView(TemplateView):
    template_name = 'polls/company.html'
    def get(self , request):
        form = CompanyForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class ContentView(TemplateView):
    template_name = 'polls/content.html'
    def get(self , request):
        form = ContentForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ContentForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class StudentsView(TemplateView):
    template_name = 'polls/students.html'
    def get(self , request):
        form = StudentsForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = StudentsForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)
