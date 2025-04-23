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


class LoginUser(generics.GenericAPIView):
    permission_classes = [AllowAny]\
    

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=200)