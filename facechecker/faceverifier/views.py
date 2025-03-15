from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import LoginSerializer, UserRegisterSerializer
from .services.authentication import Authenticator


class LoginView(APIView):
   def post(self, request):
       serializer = LoginSerializer(data=request.data)
       auth = Authenticator()
       return auth.authenticate(serializer)
  
class RegisterView(APIView):
   def post(self, request):
       serializer = UserRegisterSerializer(data=request.data)
      
       if serializer.is_valid():
           serializer.save()
           return Response({"message": "Usuário cadastrado com sucesso!"}, status=status.HTTP_201_CREATED)
      
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)