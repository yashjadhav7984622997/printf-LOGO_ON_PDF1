# pdf_logo/urls.py
from django.urls import path
from .views import add_logo_view

urlpatterns = [
    path('', add_logo_view, name='add_logo'),
]