from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('attendance/<int:attendance_id>/', views.attendance_detail, name='attendance_detail'),
    path('attendance/', views.attendance_list, name='attendance_list'),  # Include the attendance_list view
    # Add other URL patterns for your app here, if needed
]
