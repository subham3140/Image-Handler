from django.urls import path
from . import views

app_name = 'flamApp'

urlpatterns = [
    path('', views.home, name='home'),
]