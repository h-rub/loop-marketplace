from .serializers import LoginSerializer, UserSerializer

from datetime import datetime

from django.shortcuts import render

from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
            token, _ = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user)
            user_serializer = dict(user_serializer.data)
            user_serializer['token'] = str(token.key)
            return Response(user_serializer, status = status.HTTP_200_OK)
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
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        try:
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            user_serializer = dict(serializer.data)
            user_serializer['token'] = str(token.key)
            return Response(user_serializer, status = status.HTTP_200_OK)
        except:
            return Response(
            {   
                "error": "400 Bad Request",
                "message": f"Email '{serializer.validated_data['email']}' is already registered"
            }, 
            status = status.HTTP_400_BAD_REQUEST)

       
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            token = Token.objects.get(user=user)
            token.delete()
            return Response(
                {
                    "status": "200 OK",
                    "message": "You have successfully logged out"
                }
            )
        except Token.DoesNotExist:
            return Response(
                {
                    "error": "401 Unauthorized",
                    "message": "Unassociated token for the user"
                }, status = status.HTTP_401_UNAUTHORIZED
            )