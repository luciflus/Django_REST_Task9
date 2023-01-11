from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from service.serializers import StatusTypeSerializer
from .serializers import ProfileRegisterSerializer
from .models import Profile, User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class ProfileRegisterAPIView(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer

    def create_profile(self, request, is_sender):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save(is_sender=is_sender)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'], detail=False)
    def driver(self, request, pk=None):
        return self.create_profile(request, True)

    @action(methods=['POST'], detail=False)
    def passenger(self, request, pk=None):
        return self.create_profile(request, False)



