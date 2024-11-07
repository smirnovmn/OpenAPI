from django.shortcuts import render
from djoser.views import UserViewSet

from .serializers import CustomUserSerializer
from .models import CustomUser

# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с пользователями.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        """
        Переопределение метода для создания нового пользователя с дополнительными данными.
        """
        serializer.save()