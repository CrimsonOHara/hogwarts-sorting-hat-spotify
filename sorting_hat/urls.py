from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hogwarts_house/', views.hogwarts_house, name='hogwarts_house'),
]
