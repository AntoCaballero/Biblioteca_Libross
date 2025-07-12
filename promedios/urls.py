from django.urls import path
from . import views

urlpatterns = [

    path('libros-por-genero/', views.libros_por_genero, name='libros_por_genero'),
    path('promedio-puntuaciones-libro/', views.promedio_puntuaciones_libro, name='promedio_puntuaciones_libro'),
]
