from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuario.urls')),
    path('usuario/', include('usuario.urls')),
    path('especialistas/', include('especialistas.urls')),
]
