from django.urls import path
from .views import *

urlpatterns = [
    path('', MyView.as_view(), name='main_page'),
]