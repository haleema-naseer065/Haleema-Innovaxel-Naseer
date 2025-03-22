from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.create_short_url, name='create_short_url'),
    path('shorten/<str:shortCode>/', views.retrieve_short_url, name='retireve_short_url'),
    path('shorten/<str:shortCode>/', views.delete_short_url, name='delete_short_url'),
    path('shorten/<str:shortCode>/', views.update_short_url, name='update_short_url'),
    path('statistics/<str:shortCode>/', views.stats_short_url, name='stats_short_url'),
]
