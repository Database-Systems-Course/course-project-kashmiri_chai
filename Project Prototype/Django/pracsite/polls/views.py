from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib import messages

from polls.models import *
from polls.forms import *

username = "admin"
psw = "admin"
isLoggedIn = False
resultMode = ""
resultName = ""
resultSearchBy = ""

class LogoutView(TemplateView):
    #Not really a view, just used to redirect to the login page.
    template_name = 'polls/login.html'
    def get(self, request):
        global isLoggedIn
        isLoggedIn = False
        return redirect('polls:login_view')
        
class IndexView(TemplateView):
    global isLoggedIn
    template_name = 'polls/index.html'
    def get(self , request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        else:
            return render(request, 'polls/index.html', {})


class AddView(TemplateView):
    template_name = 'polls/add.html'
    def get(self, request):
        if not isLoggedIn:
            return redirect('polls:login_view')
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
            elif mode == "project":
                return redirect('polls:project_view')
            elif mode == "call":
                return redirect('polls:call_view')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class SearchView(TemplateView):
    template_name = 'polls/search.html'
    def get(self , request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        form = SearchForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        global resultMode
        global resultName
        global resultSearchBy
        form = SearchForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            resultMode = form.cleaned_data['mode']
            resultName = form.cleaned_data['name']
            resultSearchBy = form.cleaned_data['searchBy']
            print("SELECT * FROM "+resultMode+" WHERE "+resultSearchBy+" LIKE "+resultName)
            return redirect('polls:results_view')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class InterpreterView(TemplateView):
    template_name = 'polls/interpreter.html'
    def get(self, request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        form = InterpreterForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = InterpreterForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            form.save()
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)
    
    def __str__(self):
        return self.name

class CustomerView(TemplateView):
    template_name = 'polls/customer.html'
    def get(self , request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        form = CustomerForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            form.save()
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class CompanyView(TemplateView):
    template_name = 'polls/company.html'
    def get(self , request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        form = CompanyForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            form.save()
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class ContentView(TemplateView):
    template_name = 'polls/content.html'
    def get(self , request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        form = ContentForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ContentForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            form.save()
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class StudentsView(TemplateView):
    template_name = 'polls/students.html'
    def get(self , request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        form = StudentsForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = StudentsForm(request.POST)
        if form.is_valid():
            #extract data from form
            form.save()
            print(form.cleaned_data)
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class ProjectView(TemplateView):
    template_name = 'polls/project.html'
    def get(self , request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        form = ProjectForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            #extract data from form
            form.save()
            print(form.cleaned_data)
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class CallView(TemplateView):
    template_name = 'polls/call.html'
    def get(self , request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        form = CallForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = CallForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            form.save()
            return redirect('polls:index')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class AboutView(TemplateView):
    template_name = 'polls/about.html'
    def get(self , request):
        if not isLoggedIn:
            return redirect('polls:login_view')
        else:
            return render(request, 'polls/about.html', {})
            

class LoginView(TemplateView):
    template_name = 'polls/login.html'
    def get(self , request):
        form = LoginForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        global isLoggedIn
        form = LoginForm(request.POST)
        if form.is_valid():
            #extract data from form
            print(form.cleaned_data)
            if (form.cleaned_data['username'] == username and 
            form.cleaned_data['password'] == psw):
                #set flag
                isLoggedIn = True
                list(messages.get_messages(request))
                return redirect('polls:index')
            else:
                #display error
                messages.add_message(request, messages.ERROR, 'Incorrect Username or Password!')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class ResultsView(ListView):
    global resultMode
    global resultName

    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        context['resultMode'] = resultMode
        print("Result mode: " + resultMode)
        return context
    
    def get_queryset(self, **kwargs):
        if resultMode == "interpreters":
            if resultSearchBy == "name":
                return interpreter.objects.filter(name__icontains = resultName)
            elif resultSearchBy == "age":
                return interpreter.objects.filter(age__icontains = resultName)
            elif resultSearchBy == "gender":
                return interpreter.objects.filter(gender__icontains = resultName)
            elif resultSearchBy == "mobile_no":
                return interpreter.objects.filter(mobile_no__icontains = resultName)
            elif resultSearchBy == "address":
                return interpreter.objects.filter(address__icontains = resultName)
            elif resultSearchBy == "calls_served":
                return interpreter.objects.filter(calls_served__icontains = resultName)
            elif resultSearchBy == "average_rating":
                return interpreter.objects.filter(average_rating__icontains = resultName)
            elif resultSearchBy == "date_of_joining":
                return interpreter.objects.filter(date_of_joining__icontains = resultName)



        elif resultMode == "ind_cust":
            if resultSearchBy == "name":
                return customer.objects.filter(name__icontains = resultName)
            elif resultSearchBy == "gender":
                return customer.objects.filter(gender__icontains = resultName)
            elif resultSearchBy == "mobile_no":
                return customer.objects.filter(mobile_no__icontains = resultName)
            elif resultSearchBy == "address":
                return customer.objects.filter(address__icontains = resultName)
            elif resultSearchBy == "date_of_joining":
                return customer.objects.filter(date_of_joining__icontains = resultName)



        elif resultMode == "company":
            if resultSearchBy == "name":
                return company.objects.filter(name__icontains = resultName)
            elif resultSearchBy == "address":
                return company.objects.filter(address__icontains = resultName)
            elif resultSearchBy == "PoC_Name":
                return company.objects.filter(PoC_Name__icontains = resultName)
            elif resultSearchBy == "PoC_Mobile_No":
                return company.objects.filter(PoC_Mobile_No__icontains = resultName)
            elif resultSearchBy == "date_of_joining":
                return company.objects.filter(date_of_joining__icontains = resultName)



        elif resultMode == "content":
            if resultSearchBy == "name":
                return content.objects.filter(title__icontains = resultName)
            elif resultSearchBy == "interpreter":
                return content.objects.filter(interpreter__name__icontains = resultName)
            elif resultSearchBy == "link":
                return content.objects.filter(link__icontains = resultName)
            elif resultSearchBy == "date_of_release":
                return content.objects.filter(date_of_release__icontains = resultName)
            



        elif resultMode == "students":
            if resultSearchBy == "name":
                return student.objects.filter(name__icontains = resultName)
            elif resultSearchBy == "age":
                return student.objects.filter(age__icontains = resultName)
            elif resultSearchBy == "gender":
                return student.objects.filter(gender__icontains = resultName)
            elif resultSearchBy == "mobile_no":
                return student.objects.filter(mobile_no__icontains = resultName)
            elif resultSearchBy == "address":
                return student.objects.filter(address__icontains = resultName)
            elif resultSearchBy == "level":
                return student.objects.filter(level__icontains = resultName)
            elif resultSearchBy == "classification":
                return student.objects.filter(classification__icontains = resultName)
            elif resultSearchBy == "occupation":
                return student.objects.filter(occupation__icontains = resultName)
            elif resultSearchBy == "city":
                return student.objects.filter(city__icontains = resultName)
            elif resultSearchBy == "trainer":
                return student.objects.filter(trainer__name__icontains = resultName)


            
        elif resultMode == "project":
            if resultSearchBy == "Interpreter":
                return project.objects.filter(Interpreter__name__icontains = resultName)
            elif resultSearchBy == "Client":
                return project.objects.filter(Client__name__icontains = resultName) 
            elif resultSearchBy == "Date":
                return project.objects.filter(Date__icontains = resultName)
            elif resultSearchBy == "StartTime":
                return project.objects.filter(StartTime__icontains = resultName)
            elif resultSearchBy == "EndTime":
                return project.objects.filter(EndTime__icontains = resultName)
            elif resultSearchBy == "Location":
                return project.objects.filter(Location__icontains = resultName)
            elif resultSearchBy == "Purpose":
                return project.objects.filter(Purpose__icontains = resultName)
            elif resultSearchBy == "Payment":
                return project.objects.filter(Payment__icontains = resultName)
            elif resultSearchBy == "PaymentStatus":
                return project.objects.filter(PaymentStatus__icontains = resultName)


        elif resultMode == "call":
            if resultSearchBy == "Interpreter":
                return call.objects.filter(Interpreter__name__icontains = resultName)
            elif resultSearchBy == "Customer":
                return call.objects.filter(Customer__name__icontains = resultName) 
            elif resultSearchBy == "StartTime":
                return call.objects.filter(StartTime__icontains = resultName)
            elif resultSearchBy == "EndTime":
                return call.objects.filter(EndTime__icontains = resultName)
            elif resultSearchBy == "Reason":
                return call.objects.filter(Reason__icontains = resultName)
            elif resultSearchBy == "Comments":
                return call.objects.filter(Comments__icontains = resultName)
            elif resultSearchBy == "CustomerRating":
                return call.objects.filter(CustomerRating__icontains = resultName)
            elif resultSearchBy == "InterpreterRating":
                return call.objects.filter(InterpreterRating__icontains = resultName)
    
    def render_to_response(self, context):
        if not isLoggedIn:
            print("Tried accessing page illegally. Redirected to Login page!!")
            return redirect('polls:login_view')

        return super(ResultsView, self).render_to_response(context)
    


    