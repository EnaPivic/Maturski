# Generated by Django 4.0 on 2023-05-31 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu_app', '0014_rename_course_id_students_class_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjects',
            old_name='course_id',
            new_name='class_id',
        ),
    ]
