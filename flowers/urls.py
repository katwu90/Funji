from django.conf.urls import url
from . import views

app_name = 'flower'
urlpatterns = [
	# /flowers/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /flowers/50/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # # /flowers/cart
    # url(r'^cart/$', views.cart, name='cart'),
]
