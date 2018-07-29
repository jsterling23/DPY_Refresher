from django.urls import path
from . import views

app_name = 'prac_models'

urlpatterns = [
    path('', views.index, name='index'),
]
