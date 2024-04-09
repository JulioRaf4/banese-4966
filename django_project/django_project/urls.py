from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # Add this line to include the main app urls
    path('app4966/', include('app4966.urls')), # Add this line to include the app4966 app urls
]
