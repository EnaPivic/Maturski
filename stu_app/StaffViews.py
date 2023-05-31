from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


from stu_app.models import CustomUser, Staffs, ClassGroup, Subjects, Students, SchoolYear, Attendance, AttendanceReport, StudentGrade


def staff_home(request):
   
    return render(request, "teaching_staff/home.html")



def staff_take_attendance(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    school_years = SchoolYear.objects.all()
    context = {
        "subjects": subjects,
        "school_years": school_years
    }
    return render(request, "teaching_staff/take_attendance.html", context)


@csrf_exempt
def get_students(request):
    # Getting Values from Ajax POST 'Fetch Student'
    subject_id = request.POST.get("subject")
    school_year = request.POST.get("school_year")

    # Getting all data from subject model based on subject_id
    subject_model = Subjects.objects.get(id=subject_id)

    schyear_model = SchoolYear.objects.get(id=school_year)

    students = Students.objects.filter(class_id=subject_model.class_id, school_year_id=schyear_model)

    # Only Passing Student Id and Student Name Only
    list_data = []

    for student in students:
        data_small={"id":student.admin.id, "name":student.admin.first_name+" "+student.admin.last_name}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)




@csrf_exempt
def save_attendance_data(request):
    # Get Values from Staf Take Attendance form via AJAX (JavaScript)
    # Use getlist to access HTML Array/List Input Data
    student_ids = request.POST.get("student_ids")
    subject_id = request.POST.get("subject_id")
    attendance_date = request.POST.get("attendance_date")
    school_year_id = request.POST.get("school_year_id")

    subject_model = Subjects.objects.get(id=subject_id)
    school_year_model = SchoolYear.objects.get(id=school_year_id)

    json_student = json.loads(student_ids)
    # print(dict_student[0]['id'])

    # print(student_ids)
    try:
        # First Attendance Data is Saved on Attendance Model
        attendance = Attendance(subject_id=subject_model, attendance_date=attendance_date, school_year_id=school_year_model)
        attendance.save()

        for stud in json_student:
            # Attendance of Individual Student saved on AttendanceReport Model
            student = Students.objects.get(admin=stud['id'])
            attendance_report = AttendanceReport(student_id=student, attendance_id=attendance, status=stud['status'])
            attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")




def staff_edit_attendance(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    school_years = SchoolYear.objects.all()
    context = {
        "subjects": subjects,
        "school_years": school_years
    }
    return render(request, "teaching_staff/edit_attendance.html", context)

@csrf_exempt
def get_attendance_dates(request):
    

    # Getting Values from Ajax POST 'Fetch Student'
    subject_id = request.POST.get("subject")
    school_year = request.POST.get("school_year_id")

    # Getting all data from subject model based on subject_id
    subject_model = Subjects.objects.get(id=subject_id)

    schyear_model = SchoolYear.objects.get(id=school_year)

    attendance = Attendance.objects.filter(subject_id=subject_model, school_year_id=schyear_model)

    # Only Passing Student Id and Student Name Only
    list_data = []

    for attendance_single in attendance:
        data_small={"id":attendance_single.id, "attendance_date":str(attendance_single.attendance_date), "school_year_id":attendance_single.school_year_id.id}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def get_attendance_student(request):
    # Getting Values from Ajax POST 'Fetch Student'
    attendance_date = request.POST.get('attendance_date')
    attendance = Attendance.objects.get(id=attendance_date)

    attendance_data = AttendanceReport.objects.filter(attendance_id=attendance)
    # Only Passing Student Id and Student Name Only
    list_data = []

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id, "name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name, "status":student.status}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def edit_attendance_data(request):
    student_ids = request.POST.get("student_ids")

    attendance_date = request.POST.get("attendance_date")
    attendance = Attendance.objects.get(id=attendance_date)

    json_student = json.loads(student_ids)

    try:
        
        for stud in json_student:
            # Attendance of Individual Student saved on AttendanceReport Model
            student = Students.objects.get(admin=stud['id'])

            attendance_report = AttendanceReport.objects.get(student_id=student, attendance_id=attendance)
            attendance_report.status=stud['status']

            attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")



def staff_add_grade(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    school_years = SchoolYear.objects.all()
    context = {
        "subjects": subjects,
        "school_years": school_years,
    }
    return render(request, "teaching_staff/add_grade.html", context)


def staff_add_grade_save(request):
    if request.method != "POST":
        return redirect('staff_add_grade')
    else:
        student_admin_id = request.POST.get('student_list')
        exam_points = request.POST.get('exam_points')
        subject_id = request.POST.get('subject')

        student_obj = Students.objects.get(admin=student_admin_id)
        subject_obj = Subjects.objects.get(id=subject_id)

        try:
            # Check if Students Result Already Exists or not
            check_exist = StudentGrade.objects.filter(subject_id=subject_obj, student_id=student_obj).exists()
            if check_exist:
                result = StudentGrade.objects.get(subject_id=subject_obj, student_id=student_obj)
                result.subject_exam_points = exam_points
                result.save()
                return redirect('staff_add_grade')
            else:
                result = StudentGrade(student_id=student_obj, subject_id=subject_obj, subject_exam_points=exam_points)
                result.save()
                return redirect('staff_add_grade')
        except:
            return redirect('staff_add_grade')
