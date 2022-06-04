from django.contrib import admin
from django.urls import path,include
from follows import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('', include('instagramu.urls')),
    path('tinymce/', include('tinymce.urls')),
   
]
admin.site.site_header= "Instagram Lite Administration"
admin.site.site_title="Instagram"
admin.site.index_title="Welcome to Instagram administration"
