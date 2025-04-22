from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *


# Create your views here.


class RegisterUser(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class = RegistragionSerialiazer
    permission_classes =[AllowAny]
