from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    RetrieveAPIView,

)
from rest_framework.permissions import AllowAny
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from accounts.api.serializers import (
    UserCreateSerializer,
    # UserLoginSerializer

)
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]