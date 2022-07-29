from . import views
from django.urls import path

urlpatterns = [
    path('', views.accesPage),
    path('',views.home,name='home'),
    path('#signin',views.home,name='signin'),
]
