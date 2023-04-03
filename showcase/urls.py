from django.urls import path

from . import showcase

urlpatterns = [
    path('', showcase.get),
    path('something', showcase.get)
]
