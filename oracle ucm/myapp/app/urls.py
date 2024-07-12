from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('process_list/', views.process_list, name='process_list'),
]
