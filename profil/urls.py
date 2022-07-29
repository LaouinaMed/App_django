from . import views
from django.urls import path

urlpatterns = [
    path('/<str:pk>',views.home,name='profil'),
]
