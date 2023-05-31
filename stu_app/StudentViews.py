from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime 

from stu_app.models import CustomUser, Staffs, Subjects, Students, Attendance, AttendanceReport, StudentGrade


def student_home(request):
    return render(request, "student/home.html")


def student_view_attendance(request):
    student = Students.objects.get(admin=request.user.id) # Getting Logged in Student Data
    classgroup = student.class_id # Getting Course of LoggedIn Student
    subjects = Subjects.objects.filter(class_id=classgroup) # Getting the Subjects of Course 
    context = {
        "subjects": subjects
    }
    return render(request, "student/view_attendance.html", context)


def student_view_attendance_post(request):
    if request.method != "POST":
        return redirect('student_view_attendance')
    else:
        # Getting all the Input Data
        subject_id = request.POST.get('subject')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Parsing the date data into Python object
        start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

        # Getting all the Subject Data based on Selected Subject
        subject_obj = Subjects.objects.get(id=subject_id)
        # Getting Logged In User Data
        user_obj = CustomUser.objects.get(id=request.user.id)
        # Getting Student Data Based on Logged in Data
        stud_obj = Students.objects.get(admin=user_obj)

        # Now Accessing Attendance Data based on the Range of Date Selected and Subject Selected
        attendance = Attendance.objects.filter(attendance_date__range=(start_date_parse, end_date_parse), subject_id=subject_obj)
        # Getting Attendance Report based on the attendance details obtained above
        attendance_reports = AttendanceReport.objects.filter(attendance_id__in=attendance, student_id=stud_obj)

        context = {
            "subject_obj": subject_obj,
            "attendance_reports": attendance_reports
        }

        return render(request, 'student/view_attendance.html', context)
       



def student_view_grade(request):
    student = Students.objects.get(admin=request.user.id)
    student_grade = StudentGrade.objects.filter(student_id=student.id)
    context = {
        "student_grade": student_grade,
    }
    return render(request, "student/view_grade.html", context)






