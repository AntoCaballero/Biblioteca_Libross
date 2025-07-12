from django.urls import path
from . import views

urlpatterns = [
    # Géneros
    path('generos/', views.genero_list_create, name='genero-list-create'),
    path('generos/<int:pk>/', views.genero_detail, name='genero-detail'),

    # Autores
    path('autores/', views.autor_list_create, name='autor-list-create'),
    path('autores/<int:pk>/', views.autor_detail, name='autor-detail'),

    # Libros
    path('libros/', views.libro_list_create, name='libro-list-create'),
    path('libros/<int:pk>/', views.libro_detail, name='libro-detail'),

    # Puntuaciones
    path('puntuaciones/', views.puntuacion_list_create, name='puntuacion-list-create'),
    path('puntuaciones/<int:pk>/', views.puntuacion_detail, name='puntuacion-detail'),
]
