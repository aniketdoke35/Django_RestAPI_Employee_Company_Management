
from django.contrib import admin
from django.urls import include, path
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
    path('api/v1/', include('api.urls')),
]
