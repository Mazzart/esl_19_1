from django.urls import path

from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('files/', views.files_list, name='files_list'),
    path('files/<int:pk>/', views.delete_file, name='delete_file'),
    path('files/<int:pk>/time', views.file_life_time, name='file_life_time'),
    path('files/<int:pk>/error', views.file_not_exist, name='file_not_exist'),
]
