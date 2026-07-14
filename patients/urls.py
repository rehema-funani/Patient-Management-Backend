from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_patient),
    path("view", views.list_patients),
    path("show/<int:pk>", views.get_patient),
    path("update/<int:pk>", views.update_patient),
    path("delete/<int:pk>", views.delete_patient),
]