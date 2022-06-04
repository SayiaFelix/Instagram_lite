from django.contrib import admin
from django.urls import path,include
from follows import views as user_views
from instagramu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/',user_views.register,name='register'),
    path('', include('instagramu.urls')),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('accounts/login/',views.login_user,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('tinymce/', include('tinymce.urls')),
   
]
admin.site.site_header= "Instagram Lite Administration"
admin.site.site_title="Instagram"
admin.site.index_title="Welcome to Instagram administration"
