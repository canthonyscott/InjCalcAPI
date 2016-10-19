from django.shortcuts import render
from oligos.models import Oligo
from oligos.serializers import OligoSerializer, UserSerializer
from oligos.permissions import IsOwnerOrNothing, IsStaffOrTargetUser
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

# Create your views here.
class OligoViewSet(viewsets.ModelViewSet):

    serializer_class = OligoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrNothing,)

    def get_queryset(self):
        user = self.request.user
        return Oligo.objects.filter(owner = user)

    queryset = Oligo.objects.get_queryset()

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def get_permissions(self):
        return (permissions.AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),
