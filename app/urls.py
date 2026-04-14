from django.urls import path
from app import views
urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('contacts2/', views.contacts2, name='contacts2'),
]