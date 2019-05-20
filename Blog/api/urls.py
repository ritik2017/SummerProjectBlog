from django.conf.urls import url
from .views import BlogCreateApiView, BlogListsApi, BlogDeleteAPI, BlogUpdateApiView

urlpatterns = [
	url(r'create/$', BlogCreateApiView.as_view(), name='blog-create'),
	url(r'list/$', BlogListsApi.as_view(), name='blog-list'),
	url(r'update/(?P<pk>\d*)/$', BlogUpdateApiView.as_view(), name='blog-update'),
	url(r'delete/(?P<pk>\d*)/$', BlogDeleteAPI.as_view(), name='blog-delete'),
	]