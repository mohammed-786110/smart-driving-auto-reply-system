from django.urls import path
from .views import add_contact, toggle_driving

urlpatterns = [
    path('add-contact/', add_contact, name='add_contact'),
    path('toggle-driving/', toggle_driving, name='toggle_driving'),
]