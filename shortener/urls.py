from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.create_short_url, name='create_short_url'),
    path('shorten/<str:shortCode>/', views.short_url, name='short_url'),
    path('statistics/<str:shortCode>/', views.stats_short_url, name='stats_short_url'),
]
