from django.urls import path, include
from . import views


# usuario/
urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name='login'),
]
