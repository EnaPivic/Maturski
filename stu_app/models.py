from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class SchoolYear(models.Model):
    id = models.AutoField(primary_key=True)
    school_start = models.DateField()
    schooly_end = models.DateField()
    objects = models.Manager()



# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)



class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
   
    objects = models.Manager()


class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)

    objects = models.Manager()



class ClassGroup(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=255)
   
    objects = models.Manager()



class Subjects(models.Model):
    id =models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    class_id = models.ForeignKey(ClassGroup, on_delete=models.CASCADE, default=1) #need to give defauult classgrid
    staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
 
    objects = models.Manager()



class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
 
    class_id = models.ForeignKey(ClassGroup, on_delete=models.DO_NOTHING, default=1)
    school_year_id = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
   
    objects = models.Manager()


class Attendance(models.Model):
    # Subject Attendance
    id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    school_year_id = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
   
    objects = models.Manager()


class AttendanceReport(models.Model):
    # Individual Student Attendance
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    objects = models.Manager()


class StudentGrade(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    subject_exam_points = models.FloatField(default=0)
   
    objects = models.Manager()


#Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance, class_id=ClassGroup.objects.get(id=1), school_year_id=SchoolYear.objects.get(id=1))
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.students.save()
    


