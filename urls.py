from django.urls import path
from .views import Index, bbc

urlpatterns = [
    path('', Index, name='Index'),
    path('bbc/', bbc, name='BBC')

]
