from django.urls import path
from .views import *

urlpatterns = [
    path('', CartListView.as_view(), name='cart-list-create'),
    path('items/', CartItemCreateView.as_view(), name='cart-item-create'),
]

