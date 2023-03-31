from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from knox.models import AuthToken

from user.api.serializers import CustomUserSerializer, RegisterSerializer, LoginSerializer

class CustomUserAPIView(APIView):

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

#usati da knox
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })