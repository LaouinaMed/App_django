from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('listing', include('listing.urls')),
    path('profil', include('profil.urls')),
    path('compte/', include('compte.urls')),
]
