from unicodedata import category
from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('cats/', categories),
    path('admin_pls/', red),
    path('go_on_xui/', go_on_hui, name='xui')
]
