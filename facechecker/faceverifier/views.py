from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import LoginSerializer, UserRegisterSerializer, CheckUserImageSerializer
from .services.authentication import Authenticator
from .services.facechecker import FaceCheck

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
   
class CheckImageView(APIView):
    def post(self, request):
        serializer = CheckUserImageSerializer(data=request.data)
        
        if serializer.is_valid():
            faceCheck =FaceCheck()
            profile_picture = serializer.validated_data['profile_picture']

            verification = faceCheck.verificar_rosto(profile_picture)
            
            if verification is None:
                return Response({"message": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"message": f"O usuário verificado", "data": verification}, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        