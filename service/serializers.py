from django.db.models import Avg
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import Taxi, Order, StatusType, StatusDriver
from account.models import Profile

class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = '__all__'
        read_only_fields = ['profile']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['profile']

class StatusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusType
        fields = '__all__'

    avg_raiting = serializers.SerializerMethodField()

    def get_avg_raiting(self, obj):
        return StatusType.objects.all().aggregate(Avg('raiting'))
