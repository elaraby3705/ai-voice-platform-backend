# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer

# views here

class RegisterView(APIView):
    def post(self, request ):
        serializer  = RegisterationSerializer(data= request.data)

        if serialize.is_vaild():
            user  = serializer.save()

            # generate token
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