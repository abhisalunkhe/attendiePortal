from django.shortcuts import render, get_object_or_404
from .models import Student, Attendance

def home(request):
    return render(request, 'home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    attendance_records = Attendance.objects.filter(student=student)
    return render(request, 'student_detail.html', {'student': student, 'attendance_records': attendance_records})

def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendance_records': attendance_records})

def attendance_detail(request, attendance_id):
    attendance_record = get_object_or_404(Attendance, pk=attendance_id)
    return render(request, 'attendance_detail.html', {'attendance_record': attendance_record})
