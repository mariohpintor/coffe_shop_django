from django.urls import path
from .views import ProductFormViews,ProductListView

urlpatterns = [
    path('',ProductListView.as_view(),name='list_product'),
    path('agregar/', ProductFormViews.as_view(), name = 'add_product'),
]
