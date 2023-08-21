from django.urls import path
from . import views
from .views import UserRegisterView,UserEditView,PasswordChangeView,ShowProfileView,EditProfileView,CreateProfileView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',UserRegisterView.as_view(),name="register"),
    path('edit_profile/',UserEditView.as_view(),name="edit_profile"),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name = 'registration/change_password.html')),
    path('password/',PasswordChangeView.as_view(),name='password_change'),
    path('password_success/',views.password_success,name='password_success'),
    path('profile/<int:pk>',ShowProfileView.as_view(),name = 'show_profile'),
    path('edit_profile_page/<int:pk>',EditProfileView.as_view(),name = 'edit_profile_page'),
    path('create_profile_page/',CreateProfileView.as_view(),name = 'create_profile_page'),
]