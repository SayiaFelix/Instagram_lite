
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url('^$',views.homepage, name='homepage'),
    url('like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
    url('profile/(\d+)', views.user_profile, name='profile'),
    url('^new/profile', views.add_user_profile, name='add_profile'),
    # url(r'^search/', views.search_results, name='search_results'),
 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)