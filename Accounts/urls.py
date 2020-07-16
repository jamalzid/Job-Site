from django.urls import path
from . import views 


app_name = 'Accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('edite_profile/', views.edite_profile, name='edite_profile'),

    
    
]
