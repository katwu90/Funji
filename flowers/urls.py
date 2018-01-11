from django.conf.urls import url
from . import views

app_name = 'flower'
urlpatterns = [
	# /flowers/
    url(r'^$', views.index, name='index'),

    # /flowers/50/
    url(r'^(?P<flower_id>[0-9]+)/$', views.detail, name='detail'),

    # # /flowers/cart
    # url(r'^cart/$', views.cart, name='cart'),
]
