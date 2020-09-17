from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContentSerializer
from .models import Content
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from api.permissions import IsOwnerOrReadOnly, IsAdminGroup, IsAuthorGroup


class ContentView(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (TokenAuthentication,)
  serializer_class = ContentSerializer
  queryset = Content.objects.all()
  #permission_classes = [IsOwnerOrReadOnly,]

  def perform_create(self, serializer):
    return serializer.save(owner=self.request.user)

  def get_permissions(self):
      permission_classes = []
      #print(self.action)
      if self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
          permission_classes = [IsOwnerOrReadOnly]
      elif self.action == 'retrieve':
          permission_classes = [IsAuthorGroup]
      elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
          permission_classes = [IsAdminGroup]

      return [permission() for permission in permission_classes]
