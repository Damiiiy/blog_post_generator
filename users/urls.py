from .views import *
from django.urls import path


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register')
]
