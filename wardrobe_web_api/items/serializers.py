from rest_framework import serializers
from .models import Item, Category, Photo

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        return Item.objects.create(**validated_data)
    

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)
    

