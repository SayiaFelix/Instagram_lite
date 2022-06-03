from django.contrib import admin
from django.urls import re_path as url,include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('instagramu.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
]
admin.site.site_header= "Instagram Lite Administration"
admin.site.site_title="Instagram"
admin.site.index_title="Welcome to Instagram administration"
