# Generated by Django 4.0 on 2023-05-30 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu_app', '0005_rename_course_id_students_class_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminHOD',
            new_name='Admin',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'Admin'), (2, 'Staff'), (3, 'Student')], default=1, max_length=10),
        ),
    ]
