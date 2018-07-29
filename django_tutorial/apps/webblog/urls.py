from django.urls import path
from . import views

app_name = 'webblog'

urlpatterns = [
    path('', views.index, name='index'),
]