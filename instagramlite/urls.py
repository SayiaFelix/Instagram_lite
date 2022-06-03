from django.contrib import admin
from django.urls import re_path as url,include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('instagram.urls')),
]
