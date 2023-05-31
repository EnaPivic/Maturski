from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from stu_app.models import CustomUser, Staffs, ClassGroup, Subjects, Students, SchoolYear, Attendance, AttendanceReport
from .forms import AddStudent, EditStudent


def admin_home(request):
   
    return render(request, "admin_t/home.html")


def add_staff(request):
    return render(request, "admin_t/add_teach.html")


def add_staff_save(request):
    if request.method != "POST":
        return redirect('add_staff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.save()
            return redirect('add_staff')
        except:
            return redirect('add_staff')



def manage_staff(request):
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    return render(request, "admin_t/manage_teach.html", context)


def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)

    context = {
        "staff": staff,
        "id": staff_id
    }
    return render(request, "admin_t/edit_teach.html", context)


def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.save()

            return redirect('/edit_staff/'+staff_id)

        except:
            return redirect('/edit_staff/'+staff_id)



def delete_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
        staff.delete()
        return redirect('manage_staff')
    except:
        return redirect('manage_staff')




def add_class_gr(request):
    return render(request, "admin_t/add_class_gr.html")


def add_classgr_save(request):
    if request.method != "POST":
        return redirect('add_class_gr')
    else:
        classgr = request.POST.get('classgr')
        try:
            class_model = ClassGroup(class_name=classgr)
            class_model.save()
            return redirect('add_class_gr')
        except:
            return redirect('add_class_gr')


def manage_classgr(request):
    classgrs = ClassGroup.objects.all()
    context = {
        "classgrs": classgrs
    }
    return render(request, 'admin_t/manage_class_group.html', context)


def edit_classgr(request, class_id):
    classgr = ClassGroup.objects.get(id=class_id)
    context = {
        "classgr": classgr,
        "id": class_id
    }
    return render(request, 'admin_t/edit_class_gr.html', context)


def edit_classgr_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        class_id = request.POST.get('class_id')
        class_name = request.POST.get('class')

        try:
            classgr = ClassGroup.objects.get(id=class_id)
            classgr.class_name = class_name
            classgr.save()

            return redirect('/edit_classgr/'+class_id)

        except:
            return redirect('/edit_classgr/'+class_id)


def delete_classgr(request, class_id):
    classgr = ClassGroup.objects.get(id=class_id)
    try:
        classgr.delete()
        return redirect('manage_classgr')
    except:
        return redirect('manage_classgr')


def manage_schyear(request):
    school_years = SchoolYear.objects.all()
    context = {
        "school_years": school_years
    }
    return render(request, "admin_t/manage_school_year.html", context)


def add_schyear(request):
    return render(request, "admin_t/add_schyear.html")


def add_schyear_save(request):
    if request.method != "POST":
        return redirect('add_class_gr')
    else:
        school_start = request.POST.get('school_start')
        schooly_end = request.POST.get('schooly_end')

        try:
            schoolyear = SchoolYear(school_start=school_start, schooly_end=schooly_end)
            schoolyear.save()
            return redirect("add_schyear")
        except:
            return redirect("add_schyear")


def edit_schyear(request, schyear_id):
    school_year = SchoolYear.objects.get(id=schyear_id)
    context = {
        "school_year": school_year
    }
    return render(request, "admin_t/edit_schyear.html", context)


def edit_schyear_save(request):
    if request.method != "POST":
        return redirect('manage_schyear')
    else:
        schyear_id = request.POST.get('schyear_id')
        school_start = request.POST.get('school_start')
        schooly_end = request.POST.get('schooly_end')

        try:
            school_year = SchoolYear.objects.get(id=schyear_id)
            school_year.school_start = school_start
            school_year.schooly_end = schooly_end
            school_year.save()

            return redirect('/edit_schyear/'+schyear_id)
        except:
            return redirect('/edit_schyear/'+schyear_id)


def delete_schyear(request, schyear_id):
    schooly = SchoolYear.objects.get(id=schyear_id)
    try:
        schooly.delete()
        return redirect('manage_schyear')
    except:
        return redirect('manage_schyear')


def add_student(request):
    form = AddStudent()
    context = {
        "form": form
    }
    return render(request, 'admin_t/add_student.html', context)



def add_student_save(request):
    if request.method != "POST":
        return redirect('add_student')
    else:
        form = AddStudent(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            school_year_id = form.cleaned_data['school_year_id']
            class_id = form.cleaned_data['class_id']

            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)

                classgr_obj = ClassGroup.objects.get(id=class_id)
                user.students.class_id = classgr_obj

                school_year_obj = SchoolYear.objects.get(id=school_year_id)
                user.students.school_year_id = school_year_obj

                user.save()
                return redirect('add_student')
            except:
                return redirect('add_student')
        else:
            return redirect('add_student')


def manage_student(request):
    students = Students.objects.all()
    context = {
        "students": students
    }
    return render(request, 'admin_t/manage_students.html', context)


def edit_student(request, student_id):
    # Adding Student ID into Session Variable
    request.session['student_id'] = student_id

    student = Students.objects.get(admin=student_id)
    form = EditStudent()
    # Filling the form with Data from Database
    form.fields['email'].initial = student.admin.email
    form.fields['username'].initial = student.admin.username
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['class_id'].initial = student.class_id.id
    form.fields['school_year_id'].initial = student.school_year_id.id

    context = {
        "id": student_id,
        "username": student.admin.username,
        "form": form
    }
    return render(request, "admin_t/edit_student.html", context)


def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        student_id = request.session.get('student_id')
        if student_id == None:
            return redirect('/manage_student')

        form = EditStudent(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            class_id = form.cleaned_data['class_id']
            school_year_id = form.cleaned_data['school_year_id']

            try:
                # First Update into Custom User Model
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.username = username
                user.save()

                # Then Update Students Table
                student_model = Students.objects.get(admin=student_id)

                classgr = ClassGroup.objects.get(id=class_id)
                student_model.class_id = classgr

                school_year_obj = SchoolYear.objects.get(id=school_year_id)
                student_model.school_year_id = school_year_obj

           
                student_model.save()
                # Delete student_id SESSION after the data is updated
                del request.session['student_id']

                return redirect('/edit_student/'+student_id)
            except:
                return redirect('/edit_student/'+student_id)
        else:
            return redirect('/edit_student/'+student_id)


def delete_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    try:
        student.delete()
        return redirect('manage_student')
    except:
        return redirect('manage_student')


def add_subject(request):
    classgrs = ClassGroup.objects.all()
    staffs = CustomUser.objects.filter(user_type='2')
    context = {
        "classgrs": classgrs,
        "staffs": staffs
    }
    return render(request, 'admin_t/add_subject.html', context)



def add_subject_save(request):
    if request.method != "POST":
        return redirect('add_subject')
    else:
        subject_name = request.POST.get('subject')

        class_id = request.POST.get('classgr')
        classgr = ClassGroup.objects.get(id=class_id)
        
        staff_id = request.POST.get('staff')
        staff = CustomUser.objects.get(id=staff_id)

        try:
            subject = Subjects(subject_name=subject_name, class_id=classgr, staff_id=staff)
            subject.save()
            return redirect('add_subject')
        except:
            return redirect('add_subject')


def manage_subject(request):
    subjects = Subjects.objects.all()
    context = {
        "subjects": subjects
    }
    return render(request, 'admin_t/manage_subject.html', context)


def edit_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    classgrs = ClassGroup.objects.all()
    staffs = CustomUser.objects.filter(user_type='2')
    context = {
        "subject": subject,
        "classgrs": classgrs,
        "staffs": staffs,
        "id": subject_id
    }
    return render(request, 'admin_t/edit_subject.html', context)


def edit_subject_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method.")
    else:
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject')
        class_id = request.POST.get('classgr')
        staff_id = request.POST.get('staff')

        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name

            classgr = ClassGroup.objects.get(id=class_id)
            subject.class_id = classgr

            staff = CustomUser.objects.get(id=staff_id)
            subject.staff_id = staff
            
            subject.save()

            # return redirect('/edit_subject/'+subject_id)
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))

        except:
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))
            # return redirect('/edit_subject/'+subject_id)



def delete_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    try:
        subject.delete()
        return redirect('manage_subject')
    except:
        return redirect('manage_subject')


@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)





