from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistroView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', obtain_auth_token, name='login'),
]
