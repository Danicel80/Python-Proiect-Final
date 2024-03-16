from django.urls import path
from . import views
from main.views import add_to_cart


urlpatterns = [
    path('adm/', views.my_admin, name='adm'),
    path('adm/rec_cart_adm', add_to_cart, name='rec_cart_adm'),
    path('adm/del_pref', views.del_pref, name='del_pref'),
    path('adm/del_cart', views.del_cart, name='del_cart'),
]
