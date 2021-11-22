from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_form,name='employee_form'),
     path('<int:id>/',views.employee_form,name='employee_update'),
    path('employeelist/',views.employee_list,name='employee_list'),
    path('employeedelete/<int:id>/',views.employee_delete,name='employee_delete'),
]