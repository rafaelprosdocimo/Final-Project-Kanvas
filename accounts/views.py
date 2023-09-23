from rest_framework.views import APIView, Request, Response, status
from .models import Account
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import AccountSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView


class AccountsView(CreateAPIView):
    serializer_class = AccountSerializer

    def perform_create(self, serializer: AccountSerializer) -> None:
        serializer.save()
