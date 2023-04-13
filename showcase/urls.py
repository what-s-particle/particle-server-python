from django.urls import path

from . import showcase

urlpatterns = [
    path('', showcase.index),
    path('something', showcase.index)
]
