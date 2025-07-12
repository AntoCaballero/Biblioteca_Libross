# 📚 Biblioteca Libros

Aplicación web desarrollada con Django y PostgreSQL que permite registrar, listar, puntuar, comentar y analizar libros. Pensado tanto para usuarios lectores como para desarrolladores que quieran explorar un backend API RESTful con autenticación por token y visualizaciones automatizadas.

## 🛠️ Tecnologías utilizadas

  - Python 3.11.9

  - Django 5.2.3

  - PostgreSQL 17

  - Pandas: 2.3.0

  - Matplotlib / Seaborn: para visualización

  - Django REST Framework: 3.16.0

  - Pillow, NumPy, psycopg2

## ⚙️ Instalación del proyecto

### 1. Crear y activar entorno virtual

python -m venv env
env\Scripts\activate       # En Windows

### 2. Instalar Django y crear proyecto

pip install django djangorestframework pandas scikit-learn matplotlib seaborn psycopg2 pillow
django-admin startproject promedio_libros
cd promedio_libros
python manage.py startapp libros

### 3. Instalar dependencias adicionales (opcional)

pip install djangorestframework-simplejwt numpy

### 4. Configurar la base de datos (PostgreSQL)

Crear una base de datos en PostgreSQL y actualizar settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'promedio_libros',
        'USER': 'postgres',
        'PASSWORD': '1602',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 5. Migraciones

python manage.py makemigrations
python manage.py migrate

### 6. Correr el servidor

python manage.py runserver

### 7. ¿Cómo funciona el programa?

El sistema permite:

  - Registrar libros con campos como título, autor, género y valoración.
  - Visualizar los libros registrados por usuarios autenticados.- Puntuar libros con una escala del 1 al 5 (con comentarios opcionales).
  - Analizar visualmente los datos: promedios, cantidades, usuarios más activos, etc.
  - Utilizar autenticación JWT y permisos según usuario.

### 8. API REST

El proyecto cuenta con una API RESTful desarrollada con Django REST Framework. A continuación se describen los principales endpoints y cómo usarlos.

### 📘 Libros
  - GET /api/libros/
    Retorna el listado completo de libros registrados. Requiere autenticación.

  - POST /api/libros/
    Permite registrar un nuevo libro. Requiere autenticación.

    Ejemplo de JSON:

    {
      "titulo": "Yo antes de ti",
      "fecha_lanzamiento": "2012-01-05",
      "genero": 9,
      "autor": 49,
      "book_url": "https://drive.google.com/file/d/10DTzqjNR24t4sFdyldEdO6AxJqxSrQkv"
    }

  - GET /api/libros/{id}/
    Muestra los detalles de un libro específico.

### 👤 Usuarios
  - POST /api/usuarios/registro/
    Registra un nuevo usuario.

    {
      "username": "usuario1",
      "email": "correo@example.com",
      "password": "contraseña123"
    }
  - POST /api/usuarios/login/
    Retorna el token JWT para autenticación.

    {
      "username": "usuario1",
      "password": "contraseña123"
    }
### ⭐ Puntuaciones
  - POST /api/puntuar/
    Permite calificar un libro ya existente. Requiere autenticación.son

    {
      "libro": 5,
      "puntuacion": 4,
      "comentario": "Muy útil"
    }

  - GET /api/puntuaciones/
    Listado de todas las puntuaciones registradas.

### 9. 📊 Estadísticas y visualizaciones

Generación automática de gráficos accesibles desde el navegador:

- `/promedios/libros-por-genero/` → Barras de cantidad por género
![Gráfico](http://127.0.0.1:8000/promedios/libros-por-genero/)

- `/promedios/promedio-puntuaciones-libro/` → Promedios de puntuaciones
![Gráfico](http://127.0.0.1:8000/promedios/promedio-puntuaciones-libro/)


### 10. 🧪 Pruebas con Postman

Podés utilizar Postman o cualquier herramienta REST para:

  - Registrar y loguear usuarios (obtener token JWT)

  - Subir libros con PDF

  - Puntuar libros existentes

  - Consultar visualizaciones desde los endpoints

### 11. 📄 Licencias
Este proyecto utiliza herramientas y librerías con licencias open source:

  - Django: BSD License

  - Python: PSF License

  - PostgreSQL: PostgreSQL License

  - Django REST Framework y SimpleJWT: MIT

  - Pandas, NumPy y Scikit-learn: BSD

  - Matplotlib: PSF

  - Seaborn: BSD

  - Pillow: PIL License
