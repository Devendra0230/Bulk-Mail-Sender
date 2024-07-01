from django.urls import path

from . import views

urlpatterns = [
    path('',views.index ,name = 'index'),
    # path('assistant/', views.assistant, name='assistant'),
    path('voice/', views.voice_command, name='voice_command'),
    ]
