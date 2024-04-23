from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('app4966/', include('app4966.urls')), 
    path('accounts/', include('allauth.urls')),
]
