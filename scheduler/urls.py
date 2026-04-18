from django.urls import path
from .views import add_contact, toggle_driving, contact_list

urlpatterns = [
    path('add-contact/', add_contact, name='add_contact'),
    path('toggle-driving/', toggle_driving, name='toggle_driving'),
    path('contact_list/', contact_list, name='contact_list')
]