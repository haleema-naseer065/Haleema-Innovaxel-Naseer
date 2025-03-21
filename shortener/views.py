from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer


@api_view(['POST'])
def create_short_url(request):
  url = request.data.get('url')
  shortCode = request.data.get('shortCode')

  if not url or not shortCode:
    return Response({'error': 'URL and shortCode are required.'},status = status.HTTP_400_BAD_REQUEST)

  if ShortURL.objects.filter(shortCode = shortCode).exists():
    return Response({'error':'ShortCode already exists'},status = status.HTTP_400_BAD_REQUEST)
  
  short_url = ShortURL.objects.create(url = url,shortCode = shortCode)
  serializer = ShortURLSerializer(short_url)

  return Response(serializer.data,status = status.HTTP_201_CREATED)