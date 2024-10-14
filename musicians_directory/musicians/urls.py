from django.urls import path 
from . import views

urlpatterns = [
    
    path('musician/',views. musician_list, name='musician_list'),
    path('musician/create/', views.musician_create, name='musician_create'),
    path('musician/edit/<int:musician_id>/',views.musician_edit, name='musician_edit'),
    path('musician/delete/<int:musician_id>/', views.musician_delete, name='musician_delete'),
    path('album/create/', views.album_create, name='album_create'),
    path('album/edit/<int:album_id>/', views.album_edit, name='album_edit'),
    path('album/delete/<int:album_id>/', views.album_delete, name='album_delete'),

]


