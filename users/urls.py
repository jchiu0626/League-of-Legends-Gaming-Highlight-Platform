from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    # user views
    path('register', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('edit_profile/<str:username>', views.edit_profile, name='edit-profile'),
    path('edit_role/<str:username>', views.edit_role, name='edit-role'),
]
