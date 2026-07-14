from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_visit),
    path("view", views.list_visits),
    path("show/<int:pk>", views.get_visit),
    path("update/<int:pk>", views.update_visit),
    path("delete/<int:pk>", views.delete_visit),
    
]