from django.contrib import admin
from django.urls import path,include
from .views import *
from django.views.generic import View,TemplateView,ListView,DetailView
from django.contrib.auth import views as auth_view


urlpatterns = [
	path('index/',Index.as_view(),name='index'),
	path('enquiry/',Enquiry.as_view(),name='enquiry'),
	path('content/<int:pk>',ContentView.as_view(),name='content'),
	path('contact/',ContactView.as_view(),name='contact'),
    path('desh/',AdminPannel.as_view(),name='golu'),
    path("login/", auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    path('data/',Deshboard.as_view(),name='data'),
    path('fee/<int:pk>',FeeDetails.as_view(),name='fee'),
   
]



