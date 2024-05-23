from django.urls import path
from .import views

urlpatterns = [
    path ('list' , views.store_list , name='store_list'),
    path ('<int:pk>' , views.store_detail_view , name='store_detail'),
]
