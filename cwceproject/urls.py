
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('crud.urls', namespace='crud')),
    path('admin/', admin.site.urls),
]