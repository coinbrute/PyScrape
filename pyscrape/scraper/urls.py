from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_task/', views.create_task, name='create_task'),
    path('view_task/<int:task_id>/', views.view_task, name='view_task'),
    path('pricing/', views.pricing, name='pricing'),
    path('subscribe/<int:pricing_id>/', views.subscribe, name='subscribe'),
]