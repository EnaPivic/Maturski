from django import forms 
from django.forms import Form
from stu_app.models import ClassGroup, SchoolYear


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudent(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        classes = ClassGroup.objects.all()
        class_list = []
        for classgr in classes:
            single_class = (classgr.id, classgr.class_name)
            class_list.append(single_class)
    except:
        class_list = []
    
    try:
        school_years = SchoolYear.objects.all()
        school_year_list = []
        for school_year in school_years:
            single_school_year = (school_year.id, str(school_year.school_start)+" to "+str(school_year.schooly_end))
            school_year_list.append(single_school_year)
            
    except:
        school_year_list = []
    
   
    class_id = forms.ChoiceField(label="Class", choices=class_list, widget=forms.Select(attrs={"class":"form-control"}))
    school_year_id = forms.ChoiceField(label="School Year", choices=school_year_list, widget=forms.Select(attrs={"class":"form-control"}))



class EditStudent(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        classes = ClassGroup.objects.all()
        class_list = []
        for classgr in classes:
            single_class = (classgr.id, classgr.class_name)
            class_list.append(single_class)
    except:
        class_list = []


    try:
        school_years = SchoolYear.objects.all()
        school_year_list = []
        for school_year in school_years:
            single_school_year = (school_year.id, str(school_year.school_start)+" to "+str(school_year.schooly_end))
            school_year_list.append(single_school_year)
            
    except:
        school_year_list = []

   
    
    class_id = forms.ChoiceField(label="Class", choices=class_list, widget=forms.Select(attrs={"class":"form-control"}))
    school_year_id = forms.ChoiceField(label="School Year", choices=school_year_list, widget=forms.Select(attrs={"class":"form-control"}))
  