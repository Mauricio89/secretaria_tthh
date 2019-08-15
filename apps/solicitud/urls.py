from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.SolicitudList.as_view(), name='s_listar'),
    path('nuevo/', views.SolicitudCreate.as_view(), name='s_crear'),
    path('editar/<int:pk>/', views.SolicitudEditar.as_view(), name='s_editar'),
    path('eliminar/<int:pk>/', views.SolicitudEliminar.as_view(), name='s_eliminar'),
]