from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_vital),
    path("view", views.list_vitals),
    path("show/<int:pk>", views.get_vital),
    path("update/<int:pk>", views.update_vital),
    path("delete/<int:pk>", views.delete_vital),
]