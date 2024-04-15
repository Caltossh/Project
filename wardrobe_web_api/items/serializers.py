from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)
    season = serializers.CharField(max_length=100)
    size = serializers.CharField(max_length=10)
    amount = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()

    def create(self, validated_data):
        return Item.objects.create(**validated_data)
