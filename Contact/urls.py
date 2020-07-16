from django.urls import path, include
from . import views 


app_name = 'Contact'
urlpatterns = [
    path('', views.contact, name='contact'),
]