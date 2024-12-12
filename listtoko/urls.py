from django.urls import path

from . import views

urlpatterns = [
    path('', views.listtoko, name='listtoko'),
    path('<slug:vendor_slug>/', views.vendor_detail, name='vendor_detail'),
]