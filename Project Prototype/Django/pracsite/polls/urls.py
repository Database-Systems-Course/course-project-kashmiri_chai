from django.urls import path

from . import views
app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name="add_view"),
    path('search/', views.SearchView.as_view(), name="search_view"),
    path('interpreter/', views.InterpreterView.as_view(), name="interpreter_view"),
    path('ind_cust/', views.CustomerView.as_view(), name="ind_cust_view"),
    path('company/', views.CompanyView.as_view(), name="company_view"),
    path('content/', views.ContentView.as_view(), name="content_view"),
    path('students/', views.StudentsView.as_view(), name="students_view"),
    path('project/', views.ProjectView.as_view(), name="project_view"),
    path('call/', views.CallView.as_view(), name="call_view"),
    path('about/', views.AboutView.as_view(), name="about_view"),
]