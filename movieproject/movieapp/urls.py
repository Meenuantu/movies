from django.contrib import admin
from django.urls import path,include
from . import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:movie_id>',views.update_movie,name='update_movie'),
    path('delete/<int:movie_id>',views.delete,name='delete')

]