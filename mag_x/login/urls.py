from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='Login'),
    path('login/get_pas', views.generate_pas, name='get_pas')
]
