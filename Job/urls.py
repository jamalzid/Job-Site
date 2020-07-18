from django.urls import path,include
from . import views as v
from . import api

app_name='Job'
urlpatterns = [
    path('',v.job_list,name='job_list'),
    path('<int:id>/apply', v.apply, name='apply'),
    path('add-job', v.add_job, name='add_job'),
    path('api/jobs', api.Job_api_list, name='Job_api_list'), 
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),
    path('<int:id>', v.job, name='job'),
]
