from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('instagramu.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    # path(r'tinymce/', include('tinymce.urls')),
   
]
admin.site.site_header= "Instagram Lite Administration"
admin.site.site_title="Instagram"
admin.site.index_title="Welcome to Instagram administration"
