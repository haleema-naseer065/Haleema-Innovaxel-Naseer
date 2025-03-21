from django.urls import path
from .views import create_short_url

urlpatterns = [
    path('test-create/', create_short_url, name='test-create'),
]
