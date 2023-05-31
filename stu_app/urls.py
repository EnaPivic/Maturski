
from django.urls import path, include
from . import views
from .import AdminViews, StaffViews, StudentViews


urlpatterns = [
    path('', views.loginPage, name="login"),
    path('Login/', views.Login, name="Login"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', AdminViews.admin_home, name="admin_home"),
    path('add_staff/', AdminViews.add_staff, name="add_staff"),
    path('add_staff_save/', AdminViews.add_staff_save, name="add_staff_save"),
    path('manage_staff/', AdminViews.manage_staff, name="manage_staff"),
    path('edit_staff/<staff_id>/', AdminViews.edit_staff, name="edit_staff"),
    path('edit_staff_save/', AdminViews.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', AdminViews.delete_staff, name="delete_staff"),
    path('add_class_gr/', AdminViews.add_class_gr, name="add_class_gr"),
    path('add_classgr_save/', AdminViews.add_classgr_save, name="add_classgr_save"),
    path('manage_classgr/', AdminViews.manage_classgr, name="manage_classgr"),
    path('edit_classgr/<class_id>/', AdminViews.edit_classgr, name="edit_classgr"),
    path('edit_classgr_save/', AdminViews.edit_classgr_save, name="edit_classgr_save"),
    path('delete_classgr/<class_id>/', AdminViews.delete_classgr, name="delete_classgr"),
    path('add_student/', AdminViews.add_student, name="add_student"),
    path('add_student_save/', AdminViews.add_student_save, name="add_student_save"),
    path('edit_student/<student_id>', AdminViews.edit_student, name="edit_student"),
    path('edit_student_save/', AdminViews.edit_student_save, name="edit_student_save"),
    path('manage_student/', AdminViews.manage_student, name="manage_student"),
    path('delete_student/<student_id>/', AdminViews.delete_student, name="delete_student"),
    path('add_subject/', AdminViews.add_subject, name="add_subject"),
    path('add_subject_save/', AdminViews.add_subject_save, name="add_subject_save"),
    path('manage_subject/', AdminViews.manage_subject, name="manage_subject"),
    path('edit_subject/<subject_id>/', AdminViews.edit_subject, name="edit_subject"),
    path('edit_subject_save/', AdminViews.edit_subject_save, name="edit_subject_save"),
    path('delete_subject/<subject_id>/', AdminViews.delete_subject, name="delete_subject"),
    path('check_email_exist/', AdminViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', AdminViews.check_username_exist, name="check_username_exist"),
    path('manage_schyear/', AdminViews.manage_schyear, name="manage_schyear"),
    path('add_schyear/', AdminViews.add_schyear, name="add_schyear"),
    path('add_schyear_save/', AdminViews.add_schyear_save, name="add_schyear_save"),
    path('edit_schyear/<schyear_id>', AdminViews.edit_schyear, name="edit_schyear"),
    path('edit_schyear_save/', AdminViews.edit_schyear_save, name="edit_schyear_save"),
    path('delete_schyear/<schyear_id>/', AdminViews.delete_schyear, name="delete_schyear"),

    path('staff_home/', StaffViews.staff_home, name="staff_home"),
    path('staff_take_attendance/', StaffViews.staff_take_attendance, name="staff_take_attendance"),
    path('get_students/', StaffViews.get_students, name="get_students"),
    path('save_attendance_data/', StaffViews.save_attendance_data, name="save_attendance_data"),
    path('staff_edit_attendance/', StaffViews.staff_edit_attendance, name="staff_edit_attendance"),
    path('get_attendance_dates/', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student/', StaffViews.get_attendance_student, name="get_attendance_student"),
    path('edit_attendance_data/', StaffViews.edit_attendance_data, name="edit_attendance_data"),
    path('staff_add_grade/', StaffViews.staff_add_grade, name="staff_add_grade"),
    path('staff_add_grade_save/', StaffViews.staff_add_grade_save, name="staff_add_grade_save"),

    path('student_home/', StudentViews.student_home, name="student_home"),
    path('student_view_attendance/', StudentViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_view_grade/', StudentViews.student_view_grade, name="student_view_grade"),
]