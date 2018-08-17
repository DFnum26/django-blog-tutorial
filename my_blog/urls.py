from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^detail/(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>\d+)/(?P<month>\d+)/$', views.archives, name='archives'),
    url(r'^categories/(?P<category_id>\d+)/$', views.categories, name='categories'),
]
