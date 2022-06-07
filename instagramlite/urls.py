from django.contrib import admin
from django.urls import path,include
from instagramu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('instagramu.urls')),
    path('register/',views.register_user,name='register'),
    path('accounts/login/',views.login_user,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('tinymce/', include('tinymce.urls')),
   
]
admin.site.site_header= "Instagram Lite Administration"
admin.site.site_title="Instagram"
admin.site.index_title="Welcome to Instagram administration"
