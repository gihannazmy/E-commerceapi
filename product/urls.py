
from django.urls import path
from .views import *


urlpatterns = [
    path('',get_all_products, name='products'),
    path('<str:pk>/', get_by_id_product, name='get_by_id'),
    path('new/',new_product, name='new-product'),
    path('update/<str:pk>/', update_product, name='update-product'),
    path('delete/<str:pk>/', delete_product, name='delete-product'),
    path('<str:pk>/new-review/', new_reveiw, name='new-review'),
    path('<str:pk>delete-review/',delete_review, name='delete-review'),
]
