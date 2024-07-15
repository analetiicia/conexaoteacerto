from django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name ='login'),
    path('home/', views.home, name ='home'),
    path('logout', views.logout_view, name ='logout'),
]