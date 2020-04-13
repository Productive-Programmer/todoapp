from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addtodo/', views.addtodo),
    path('deletetodo/<int:todo_id>', views.delete),
]
