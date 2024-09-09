from django.urls import path
from . import views

urlpatterns = [
    path('registration/platform/', views.index, name='index'),
    path('registration/platform/gemes/', views.index2, name='index2'),
    path('registration/platform/cart/', views.index3, name='index3'),
    path('registration/', views.index4, name='index4'),
]