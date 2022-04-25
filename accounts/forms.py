from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Course, Subject, Student, Staff, SessionYearModel, CustomUser


class DateInput(forms.DateInput):
    input_type = "date"


class CustomUserCreateForm(UserCreationForm):
    # subjects = Subject.objects.all()
    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        fields = ('user_type', 'username', 'email', 'first_name', 'last_name')
    
    # subject = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )

class CustomUserChangeFrom(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class StaffCreateForm(CustomUserCreateForm):
    model = Staff
    # subject = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user_type'].initial = 2
        
        # subject = forms.ModelMultipleChoiceField(
        # queryset=Subject.objects.all(),
        # widget=forms.CheckboxSelectMultiple)
        # self.fields['subject'] = subject

        # add custom error messages
        # self.fields['subject'].error_messages.update({
        #     'required': 'Please add a name' })

class StaffUpdateForm(CustomUserChangeFrom):
    model = Staff

        
        
class SessionYearModelForm(forms.ModelForm):
    model = SessionYearModel
    session_start_year = forms.DateField(widget=DateInput)
    session_end_year = forms.DateField(widget=DateInput)


    class Meta:
        model = SessionYearModel
        fields = '__all__'
        # widgets = {
        #     'session_start_year': forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})),
        #     'session_end_year': forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        # }

class SubjectForm(forms.ModelForm):
    model = Subject

    class Meta:
        model = Subject
        fields = '__all__'
        # widgets = {
        #     'model' : forms.TextInput(),
        # }
        # labels = {
        #     'model' : 'Model'
        # }
    #     model = Subject
    #     fields = '__all__'
    
    # staff = forms.ModelChoiceField(
    #     queryset=Staff.objects.all()
    #      )
    # subject = forms.ModelChoiceField(
    #     queryset=Subject.objects.all(), 
    #     to_field_name="staff",
    #     empty_label=None )


class StudentForm(forms.ModelForm):
    model = Student

    class Meta:
        model = Student

        fields = '__all__'
        # widgets = {
        #     'first_name': forms.CharField(required=True),
        #     'last_name': forms.CharField(required=True),
        # }


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    session_year_id=SessionYearModel.objects.all()
    courses = Course.objects.all()
    course_list = []
    
    try:
        for course in courses:
            sml_course = (course.id, course.course_name)
            course_list.append(sml_course)
    except: 
        course_list = []

    session_list = []
    try:          
        sessions = SessionYearModel.objects.all()
        for ses in sessions:
            sml_session = (ses.id, str(ses.session_start_year)+" TO "+str(ses.session_end_year))
            session_list.append(sml_session)
    except:
        session_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say')
    )

    course = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class": "form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))
    # session_start=forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end=forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    date_joined = forms.DateField(label="Date Joined", widget=DateInput(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50, widget=forms.FileInput(attrs={"class": 'form-control'}), required=False)
    note = forms.CharField(label="Note", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)


class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
   
    courses = Course.objects.all()
    course_list = []
    try:
        for course in courses:
            sml_course = (course.id, course.course_name)
            course_list.append(sml_course)
    except: 
        course_list = []

    sessions = SessionYearModel.objects.all()
    session_list = []
    try:               
        for ses in sessions:
            sml_ses = (ses.id, str(ses.session_start_year)+" TO "+str(ses.session_end_year))
            session_list.append(sml_ses)
            
    except:
        session_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say')
    )
    
    course = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label="Gender", choices=gender_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))
    # session_start = forms.DateField(label="Session Start",widget=DateInput(attrs={"class": "form-control"}))
    # session_end = forms.DateField(label="Session End",widget=DateInput(attrs={"class": "form-control"}))
    date_joined = forms.DateField(label="Date Joined", widget=DateInput(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", widget=forms.FileInput(attrs={"class": "form-control"}), required=False)
    note = forms.CharField(label="Note", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

class EditResultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.staff_id = kwargs.pop("staff_id")
        super(EditResultForm, self).__init__(*args, **kwargs)
        subject_list = []
        try:
            subjects = Subject.objects.filter(staff_id=self.staff_id)
            for subject in subjects:
                subject_single = (subject.id, subject.subject_name)
                subject_list.append(subject_single)
        except:
            subject_list = []
        
        self.fields['subject_id'].choices = subject_list

    session_list = []
    try:
        sessions = SessionYearModel.objects.all()
        for session in sessions:
            session_single = (session.id, str(session.session_start_year)+" TO "+str(session.session_end_year))
            session_list.append(session_single)
    except:
        session_list = []
        
    subject_id = forms.ChoiceField(label="Subject", widget=forms.Select(attrs={"class": "form-control"}))
    session_ids = forms.ChoiceField(label="Session Year", choices=session_list,widget=forms.Select(attrs={"class": "form-control"}))
    student_ids = forms.ChoiceField(label="Student", widget=forms.Select(attrs={"class": "form-control"}))
    assignment_marks = forms.CharField(label="Assignment Marks", widget=forms.TextInput(attrs={"class": "form-control"}))
    exam_marks = forms.CharField(label="Exam Marks", widget=forms.TextInput(attrs={"class": "form-control"}))

