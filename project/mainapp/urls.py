from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
      path('',views.home,name='home'), 
      path('mail-sending',views.sendmail,name='mail'),
      path('result/<str:id>',views.result,name='result')

]
