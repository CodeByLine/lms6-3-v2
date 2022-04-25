# accounts/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import accounts_home_view, registration_view, HelloView, logout_view, login_view, account_view # SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", accounts_home_view, name="accounts_home"),
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('account/', account_view, name="account"),

    path('hello/', HelloView.as_view(), name="hello"),
    
    # path("signup/", SignUpView.as_view(), name="signup"),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]