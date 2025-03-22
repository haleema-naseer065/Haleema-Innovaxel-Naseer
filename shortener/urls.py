from django.urls import path
from . import views

urlpatterns = [
    path('test-create/', views.create_short_url, name='create_short_url'),
    path('test-retrieve/<str:shortCode>/', views.retrieve_short_url, name='retireve_short_url'),
    path('test-delete/<str:shortCode>/', views.delete_short_url, name='delete_short_url'),
]
