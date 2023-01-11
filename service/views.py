from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import views, status
from rest_framework import authentication, permissions
from .permissions import IsAuthorPermission

from .models import Taxi, Order, StatusDriver, StatusType
from .serializers import TaxiSerializer, OrderSerializer, StatusTypeSerializer

class TaxiViewSet(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorPermission]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def perform_update(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def perform_destroy(self, serializer):
        serializer.save(profile=self.request.user.profile)

    @action(methods=['POST'], detail=True)
    def leave_status(self, request, pk=None):
        serializer = OrderSerializer(data=Order.objects.all())
        if serializer.is_valid():
            serializer.save(
                profile=request.user.profile,
                order=Order.objects.all()
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def perform_update(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def perform_destroy(self, serializer):
        serializer.save(profile=self.request.user.profile)

class StatusTypeViewSet(viewsets.ModelViewSet):
    queryset = StatusType.objects.all()
    serializer_class = StatusTypeSerializer
