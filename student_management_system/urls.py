"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from student_management_system import settings
from accounts import views, HodViews, StaffViews, StudentViews
from accounts.EditResultViewClass import EditResultViewClass
from django.urls import reverse

app_name = 'accounts'
urlpatterns = [
    path('demo/', views.showDemoPage, name='demo'),
    path('accounts/account/', views.account, name='account'),
    path('accounts/accounts_home/', views.account, name='accounts_home'),
    path('signup_admin/', views.signup_admin, name='signup_admin'),
    path('signup_staff/', views.signup_staff, name='signup_staff'),
    path('signup_student/', views.signup_student, name='signup_student'),
    path('do_signup_admin/', views.do_signup_admin, name='do_signup_admin'),
    path('do_signup_staff/', views.do_signup_staff, name='do_signup_staff'),
    path('do_signup_student/', views.do_signup_student, name='do_signup_student'),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', views.showLoginPage, name='show_login'),
    path('get_user_details', views.GetUserDetails, name='get_user_details'),
    path('logout_user', views.logout_user, name="logout"),
    path('doLogin', views.doLogin, name="dologin"),
    
    # path('admin_home',HodViews.AdminHomeView.as_view(), name="admin_home"),
    path('admin_home',HodViews.admin_home, name="admin_home"),
    path('add_staff', HodViews.add_staff, name="add_staff"),
    path('add_staff_save', HodViews.add_staff_save, name="add_staff_save"),
    path('add_student', HodViews.add_student, name="add_student"),
    path('add_student_save', HodViews.add_student_save, name="add_student_save"),
    # path('add_subject', HodViews.add_subject, name='add_subject'),
    # path('add_subject_save', HodViews.add_subject_save, name='add_subject_save'),
    path('edit_staff/<str:staff_id>', HodViews.edit_staff, name='edit_staff'),
    path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    path('edit_student/<str:student_id>', HodViews.edit_student, name='edit_student'),
    path('edit_student_save/', HodViews.edit_student_save, name="edit_student_save"),
    # path('edit_subject/<str:subject_id>', HodViews.edit_subject, name='edit_subject'),
    # path('edit_subject_save', HodViews.edit_subject_save,name="edit_subject_save"),
    path('check_email_exist', HodViews.check_email_exist,name="check_email_exist"),
    path('check_username_exist', HodViews.check_username_exist,name="check_username_exist"),
    path('student_feedback_message', HodViews.student_feedback_message, name="student_feedback_message"),
    path('staff_feedback_message', HodViews.staff_feedback_message, name="staff_feedback_message"),
    path('student_feedback_message_replied', HodViews.student_feedback_message_replied, name="student_feedback_message_replied"),
    path('staff_feedback_message_replied', HodViews.staff_feedback_message_replied, name="staff_feedback_message_replied"),

    path('student_leave_view', HodViews.student_leave_view, name="student_leave_view"),
    path('staff_leave_view', HodViews.staff_leave_view, name="staff_leave_view"),
    path('student_leave_approved/<str:leave_id>', HodViews.student_leave_approved, name="student_leave_approved"),
    path('student_leave_denied/<str:leave_id>', HodViews.student_leave_denied, name="student_leave_denied"),
    path('staff_leave_approved/<str:leave_id>', HodViews.staff_leave_approved, name="staff_leave_approved"),
    path('staff_leave_denied/<str:leave_id>', HodViews.staff_leave_denied, name="staff_leave_denied"),
    path('admin_view_attendance', HodViews.admin_view_attendance, name="admin_view_attendance"),
    path('admin_get_attendance_dates', HodViews.admin_get_attendance_dates, name="admin_get_attendance_dates"),
    path('admin_get_attendance_student', HodViews.admin_get_attendance_student, name="admin_get_attendance_student"),
    path('admin_profile', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_save', HodViews.admin_profile_save, name="admin_profile_save"),

#class-based list view
    path('courses', HodViews.CourseListView.as_view(), name="course_list"),
    path('sessions', HodViews.SessionYearModelListView.as_view(), name="session_list"),
    path('students', HodViews.StudentListView.as_view(), name="student_list"),
    path('staff', HodViews.StaffListView.as_view(), name="staff_list"),
    path('subjects', HodViews.SubjectListView.as_view(), name="subject_list"),


#class-based create view
    path('course/add/', HodViews.CourseCreateView.as_view(), name="course_add"),
    path('session/add/', HodViews.SessionYearModelCreateView.as_view(), name="session_add"),
    path('staff/add/', HodViews.StaffCreateView.as_view(), name="staff_add"),
    path('student/add/', HodViews.StudentCreateView.as_view(), name="student_add"),
    path('subject/add/', HodViews.SubjectCreateView.as_view(), name="subject_add"),

#class-based detail view
    path('course/<int:pk>/', HodViews.CourseDetailView.as_view(), name="course_detail"),
    path('session/<int:pk>/', HodViews.SessionYearModelDetailView.as_view(), name="session_detail"),
    path('staff/<int:pk>/', HodViews.StaffDetailView.as_view(), name="staff_detail"),
    path('student/<int:pk>/', HodViews.StudentDetailView.as_view(), name="student_detail"),
    path('subject/<int:pk>/', HodViews.SubjectDetailView.as_view(), name="subject_detail"),

#class-based update view
    path('course/<int:pk>/update', HodViews.CourseUpdateView.as_view(), name="course_update"),
    path('session/<int:pk>/update', HodViews.SessionYearModelUpdateView.as_view(), name="session_update"),
    path('staff/<int:pk>/update', HodViews.StaffUpdateView.as_view(), name="staff_update"),
    path('student/<int:pk>/update', HodViews.StudentUpdateView.as_view(), name="student_update"),
    path('subject/<int:pk>/update', HodViews.SubjectUpdateView.as_view(), name="subject_update"),

#class-based delete view
    path('courses/<int:pk>/delete', HodViews.CourseDeleteView.as_view(), name="course_delete"),
    path('session/<int:pk>/delete', HodViews.SessionYearModelDeleteView.as_view(), name="session_delete"),
    path('staff/<int:pk>/delete', HodViews.StaffDeleteView.as_view(), name="staff_delete"),
    path('student/<int:pk>/delete', HodViews.StudentDeleteView.as_view(), name="student_delete"),
    path('subject/<int:pk>/delete', HodViews.SubjectDeleteView.as_view(), name="subject_delete"),


    # staff URL paths
    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('staff_take_attendance', StaffViews.staff_take_attendance, name="staff_take_attendance"),
    path('staff_update_attendance', StaffViews.staff_update_attendance, name="staff_update_attendance"),
    path('get_attendance_dates', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    path('get_students', StaffViews.get_students, name="get_students"),
    path('get_attendance_student', StaffViews.get_attendance_student, name="get_attendance_student"),
    path('save_attendance_data', StaffViews.save_attendance_data, name="save_attendance_data"),
    path('save_updateattendance_data', StaffViews.save_updateattendance_data, name="save_updateattendance_data"),
    path('staff_apply_leave', StaffViews.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save', StaffViews.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback', StaffViews.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save', StaffViews.staff_feedback_save, name="staff_feedback_save"),
    path('staff_profile', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_save', StaffViews.staff_profile_save, name="staff_profile_save"),
    path('staff_add_result', StaffViews.staff_add_result, name="staff_add_result"),
    path('save_student_result', StaffViews.save_student_result, name="save_student_result"),
    path('edit_student_result', EditResultViewClass.as_view(), name="edit_student_result"),
    path('fetch_result_student',StaffViews.fetch_result_student, name="fetch_result_student"),
    # student URL paths
    path('student_home', StudentViews.student_home, name="student_home"),
    path('student_view_attendance', StudentViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),

    path('student_apply_leave', StudentViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile', StudentViews.student_profile, name="student_profile"),
    path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),
    path('student_view_result', StudentViews.student_view_result, name="student_view_result"),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


# """student_management_system URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # django_project/urls.py
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.urls import include, path
# from django.views.generic.base import TemplateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", TemplateView.as_view(template_name="home.html"), name="home"),

#     path('slm_home/', include('slm_app.urls')),

#     path("accounts/", include("accounts.urls")),
#     path("accounts/", include("django.contrib.auth.urls")),

#      path("catalog/", include("course_catalog.urls")),


#     # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
#     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
#         name='password_change_done'),

#     # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
#     #     name='password_change'),

#     path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
#      name='password_reset_done'),

#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
#      name='password_reset_complete'),
# ]
