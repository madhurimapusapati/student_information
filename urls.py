from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.student_add, name='student_add'),
    path('edit/<int:id>/', views.student_edit, name='student_edit'),  # <-- Make sure this exists
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
]
