from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item, Photo
from .serializers import ItemSerializer, PhotoSerializer

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


class ItemPhotosAPIView(APIView):
    def get(self, request, id):
        photos = Photo.objects.filter(item_id=id)
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)