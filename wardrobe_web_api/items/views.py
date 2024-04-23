from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Item, Photo
from .serializers import CategorySerializer, ItemSerializer, PhotoSerializer

class ItemView(APIView):
    def get(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    

class ItemDetailView(APIView):
    def get(self, request, id):
        try:
            item = Item.objects.get(id=id)
            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        item = Item.objects.get(pk=id)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        item = Item.objects.get(pk=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def item_photos(request, id):
    photos = Photo.objects.filter(item_id=id)
    photo_urls = [photo.image.url for photo in photos]

    return JsonResponse(photo_urls, safe=False)
    
# ------------------------------------------------------

class CategoryView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetailView(APIView):
    def get(self, request, id):
        try:
            item = Category.objects.get(id=id)
            serializer = CategorySerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        

def category_items(request, id):
    category = get_object_or_404(Category, id=id) 
    items = Item.objects.filter(category=category)
    serializer = ItemSerializer(items, many=True)
    
    return JsonResponse(serializer.data, safe=False)