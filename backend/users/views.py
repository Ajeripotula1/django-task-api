from django.shortcuts import render
from rest_framework import generics 
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
# Create your views here.
# class based view from DRF that is used to hangle creation of new user 
# generics.CreateAPIView: generic view that offers behavior for creating an obj (user in this case)
    # POST logic already handled 
    # validated incoming JSON data (unique username, all fields present, etc )
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # specify serializer used to validate the data for the user model 
    serializer_class =UserSerializer

# class LogoutView[APIView]

# class RegisterUserView(view.APIView):
#     '''API View to Create a new User'''
    
#     def post(self, request):
#         '''Handles POST request to register a new user'''
#         username = request.data.get('username')
#         password = request.data.get('password')
        
#         if not username or password:
#             return Response({'error':'Username and password required'}, status=status.HTTP_404_BAD_REQUEST)
#         if User.objects.filter(username=username).exists():
#             return Response({'error':'Username already exists'}, status=status.HTTP_404_BAD_REQUEST)
#         user =User.objects.create_user(username=username,password=paas)
        

