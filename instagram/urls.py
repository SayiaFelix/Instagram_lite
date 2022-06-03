from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  

    # re_path('', views.main, name='main'),
    re_path('^$', views.homepage, name='homepage'),
    # re_path(r'^search/', views.search_results, name='search_results'),
   
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
