from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio),
    url(r'^cafeteria/(?P<pk>\d+)/$', views.categoria_producto, name='categoria_producto'),
]