from django.urls import path
from . import views
urlpatterns = [
    path('', views.especialistas, name ='especialistas'),
    path('createespecialista/', views.createespecialista, name ='createespecialista'),
    path('updateespecialista/<int:id_especialista>', views.updateespecialista, name="updateespecialista"),
    path('deleteespecialista/<int:id_especialista>', views.deleteespecialista, name="deleteespecialista"),
    path('delete/confirm/<int:id_especialista>', views.confirmDelete, name="confirmdelete")
    #path('read/<int:id_profissional>', views.readprofissional, name="readprofissional"),
    #path('update/<int:id_profissional>', views.updateprofissional, name="updateprofissional"),
    #path('delete/<int:id_profissional>', views.deleteprofissional, name="deleteprofissional"),
    #path('delete/confirm/<int:id_profissional>', views.confirmDelete, name="ConfirmDelete")
]
