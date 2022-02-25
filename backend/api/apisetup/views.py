from django import views
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser,IsAuthenticateOrReadOnly,DjangoModelPermission,DjangoModelPermissionOrAnonReadOnly
# from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser,IsAuthenticateOrReadOnly,DjangoModelPermission,DjangoModelPermissionOrAnonReadOnly


def index(request):
    pass
# Create your views here.
class StudentModelViewSet(views.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes =[IsAuthenticated]
    # permission_classes =[AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticateOrReadOnly]
    # permission_classes = [DjangoModelPermissionOrAnonReadOnly]