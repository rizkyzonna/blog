from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$',views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/kategori/bola', views.bola, name='bola'),
	url(r'^post/kategori/umum', views.umum, name='umum'),
	#url(r'^post/test', views.test, name='test'),
	]