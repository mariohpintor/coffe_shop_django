from django.urls import path
from .views import ProductFormViews

urlpatterns = [
    path('agregar/', ProductFormViews.as_view(), name = 'add_product'),
]
