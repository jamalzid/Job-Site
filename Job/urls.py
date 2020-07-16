from django.urls import path,include
from . import views as v


app_name='Job'
urlpatterns = [
    path('',v.job_list,name='job_list'),
    
    path('add-job', v.add_job, name='add_job'),
    path('<slug:slug>',v.job,name='job'),
]
