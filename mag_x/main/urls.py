from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.despre, name='Despre'),
    path('logout/', views.user_logout, name='logout'),
    path('contact/', views.contact, name='Contact'),
    path('detail', views.prod_detail, name='Detail'),
    path('rec_pref', views.record_pref, name='rec_pref'),
    path('rec_cart', views.add_to_cart, name='rec_cart'),
]
