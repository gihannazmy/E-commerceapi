from django.urls import path
from .views import *


urlpatterns = [
    path('new/',new_order, name='new-order'),
    path('all/',all_orders, name='all-orders'),
    path('get-order/',get_order, name='get-order'),
    path('update-order/<str:pk>',update_order_status, name='update-order'),
    path('delete-order/<str:pk>',delete_order, name='delete-order'),
    
]