from django.urls import path
from . import views
urlpatterns = [
    path('', views.carga_files, name= 'carga_files' ),
    path('consulta', views.consulta_page),
    path('consulta_facturacion', views.consultaFacturacion, name = 'consulta_facturacion'),
    path('buscar', views.buscar),
    path('view-catg', views.consulta_Categorias, name = 'categorias'),
    path('view-clientes', views.consulta_clientes, name = 'clientes'),
    path('view-instances', views.consulta_instancias, name = 'instancias'),
    path('view-recursos', views.consulta_recursos, name = 'recursos'),
    path('view-config', views.consulta_configuraciones, name = 'configuraciones'),
    path('creacion', views.creacion_page),
    path('crear_recurso', views.crear_recurso, name = 'crear_recurso'),
    path('crear_config', views.crear_config, name = 'crear_config'),
    path('crear_cliente', views.crear_Cliente, name = 'crear_clientes'),
    path('crear_instance', views.crear_Instance, name = 'crear_instance'),
    path('crear_categ', views.crear_Categoria, name = 'crear_categ'),
]