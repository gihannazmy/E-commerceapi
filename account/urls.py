
from django.urls import path
from .views import *


urlpatterns = [
    path('register/',register, name='register'),
    path('current/',current_user, name='current-user'),
    path('update/',update_user, name='update-user'),
    path('forget-password/',forgot_password, name='forget-password'),
    path('reset-password/<str:token>',reset_password, name='reset-password'),
   
   
]
