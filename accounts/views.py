# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from .serializers import LoginSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # Generate token
            token, _ = Token.objects.get_or_create(user=user)

            return Response({
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                },
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# create LoginView class
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        if not user: 
            return  Response(
                {"detail":"invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # get or create auth token 
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
          "user": {
             "id": user.id,
             "email": user.email,
            },
            "token": token.key
        }, status=status.HTTP_200_OK)

# Happy coding ! 