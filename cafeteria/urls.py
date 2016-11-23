from django.conf.urls import url, include
from cafeteria import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^categoria/$', views.CategoriaListView.as_view(), name='categoria-lista'),
    url(r'^categoria/(?P<pk>\d+)/detalle/$', views.CategoriaDetailView.as_view(), name='categoria-detalle'),
    url(r'^producto/$', views.ProductoListView.as_view(), name='producto-lista'),
    url(r'^producto/(?P<pk>\d+)/detalle/$', views.ProductoDetailView.as_view(), name='producto-detalle'),
    url(r'^producto/(?P<pk>\d+)/actualizar/$', views.ProductoUpdate.as_view(), name='producto-actualizar'),
    url(r'^producto/crear/$', views.ProductoCreate.as_view(), name='producto-crear'),
    url(r'^producto/(?P<pk>\d+)/eliminar/$', views.ProductoDelete.as_view(), name='producto-eliminar'),
    
    
    
    #url(r'^cafeteria/(?P<pk>\d+)/detalle/$', views.categoria_producto, name='categoria_producto'),
    #url(r'^cafeteria/nueva_categoria/$', views.agregar_categoria, name='agregar_categoria'),
    #url(r'^cafeteria/(?P<pk>[0-9]+)/edit/$', views.editar_categoria, name='editar_categoria'),
    #url(r'^producto/$', views.ProductoListView.as_view(), name='producto-list'),
    #url(r'^producto/(?P<pk>\d+)/detalle/$', views.ProductoDetailView.as_view(), name='producto-detail'),
    #url(r'^producto/(?P<pk>\d+)/update/$', views.ProductoUpdate.as_view(), name='producto-update'),
    #url(r'^producto/create/$', views.ProductoCreate.as_view(), name='producto-create'),
    #url(r'^producto/(?P<pk>\d+)/delete/$', views.ProductoDelete.as_view(), name='producto-delete'),
]