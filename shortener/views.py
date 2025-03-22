from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer

@api_view(['POST'])
def create_short_url(request):
  try:
    url = request.data.get('url')
    shortCode = request.data.get('shortCode')

    if not url or not shortCode:
      return Response({'error': 'URL and shortCode are required.'},status = status.HTTP_400_BAD_REQUEST)

    if ShortURL.objects.filter(shortCode = shortCode).exists():
      return Response({'error':'ShortCode already exists'},status = status.HTTP_400_BAD_REQUEST)
    
    short_url = ShortURL.objects.create(url = url,shortCode = shortCode)
    serializer = ShortURLSerializer(short_url)

    return Response(serializer.data,status = status.HTTP_201_CREATED)
  
  except Exception as e:
    return Response({'error':'An unexpected error has occurred,'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def retrieve_short_url(request,shortCode):
  try:
    short_url = ShortURL.objects.get(shortCode = shortCode)
    short_url.access_count += 1
    short_url.save()

    serializer = ShortURLSerializer(short_url)

    return Response(serializer.data,status = status.HTTP_200_OK)

  except ShortURL.DoesNotExist:
    return Response({'error': shortCode + 'does not exist'},status = status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_short_url(request,shortCode):
  try:
    short_url = ShortURL.objects.get(shortCode= shortCode)
    short_url.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)

  except ShortURL.DoesNotExist:
    return Response({'error': shortCode + 'does not exist'},status = status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_short_url(request,shortCode):
  
  url = request.data.get('url')
  if not url:
    return Response({'error':'URL is required'},status = status.HTTP_400_BAD_REQUEST)
  
  try:
    short_url = ShortURL.objects.get(shortCode = shortCode)
    short_url.url = url
    short_url.updated_at = timezone.now()
    short_url.save()

    serializer = ShortURLSerializer(short_url)
    return Response(serializer.data,status = status.HTTP_200_OK)

  except ShortURL.DoesNotExist:
    return Response({'error':ShortCode + 'does not exist'},status = status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def url_statistics(request,shortCode):
  try:
    short_url = ShortURL.objects.get(shortCode = shortCode)
    serializer = ShortURLSerializer(short_url)

    return Response(serializer.data,status = status.HTTP_200_OK)
  
  except ShortURL.DoesNotExist:
    return Response({'error': shortCode + ' does not exist'},status = status.HTTP_404_NOT_FOUND)


