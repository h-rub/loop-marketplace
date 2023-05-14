from datetime import datetime

from django.shortcuts import render

from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LoginSerializer, UserSerializer

# Create your views here.
class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        user = authenticate(
                    request, 
                    email = serializer.validated_data['email'],
                    password = serializer.validated_data['password']
                )
        if user is not None:
            user.last_login = datetime.now()
            user.save()
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(
                {
                    "error": "401 Unauthorized",
                    "message": "The credentiales provided are not valid. Please review your information and try again."
                }, 
                status = status.HTTP_401_UNAUTHORIZED)


class SignUpView(APIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        try:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(
            {   
                "error": "400 Bad Request",
                "message": f"Email '{serializer.validated_data['email']}' is already registered"
            }, 
            status = status.HTTP_400_BAD_REQUEST)

       