from django.urls import path
from app import views
urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact2/', views.contact2, name='contact2'),
]