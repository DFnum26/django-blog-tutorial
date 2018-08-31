from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^detail/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>\d+)/(?P<month>\d+)/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^tag/(?P<pk>\d+)/$', views.TagView.as_view(), name='tag'),
    url(r'^category/(?P<category_id>\d+)/$', views.CategoryView.as_view(), name='category'),
]
