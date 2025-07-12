from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Genero, Autor, Libro, Puntuacion
from .serializers import GeneroSerializer, AutorSerializer, LibroSerializer, PuntuacionSerializer
from django.shortcuts import get_object_or_404

# ---- GENERO ----
@api_view(['GET', 'POST'])
def genero_list_create(request):
    if request.method == 'GET':
        generos = Genero.objects.all()
        serializer = GeneroSerializer(generos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GeneroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def genero_detail(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'GET':
        serializer = GeneroSerializer(genero)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GeneroSerializer(genero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        genero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---- AUTOR ----
@api_view(['GET', 'POST'])
def autor_list_create(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def autor_detail(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---- LIBRO ----
@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def libro_list_create(request):
    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LibroSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(creador=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def libro_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'GET':
        serializer = LibroSerializer(libro, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        if libro.creador != request.user:
            return Response({'error': 'Solo el creador puede editar este libro.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = LibroSerializer(libro, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if libro.creador != request.user:
            return Response({'error': 'Solo el creador puede eliminar este libro.'}, status=status.HTTP_403_FORBIDDEN)
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---- PUNTUACION ----
@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def puntuacion_list_create(request):
    if request.method == 'GET':
        puntuaciones = Puntuacion.objects.all()
        serializer = PuntuacionSerializer(puntuaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PuntuacionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def puntuacion_detail(request, pk):
    puntuacion = get_object_or_404(Puntuacion, pk=pk)
    if request.method == 'GET':
        serializer = PuntuacionSerializer(puntuacion)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if puntuacion.usuario != request.user:
            return Response({'error': 'No puedes editar esta puntuación.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = PuntuacionSerializer(puntuacion, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if puntuacion.usuario != request.user:
            return Response({'error': 'No puedes eliminar esta puntuación.'}, status=status.HTTP_403_FORBIDDEN)
        puntuacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
