# Generated by Django 4.0 on 2023-05-30 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu_app', '0004_rename_courses_classgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='course_id',
            new_name='class_id',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='course_id',
            new_name='class_id',
        ),
    ]