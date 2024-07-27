from django.urls import path
from . import views
app_name = 'loloutplays'
urlpatterns = [
    #loloutplays_story views
    path('', views.loloutplay_home, name='loloutplay_home'),
    path('add', views.add_story, name='add-story'),
    path('edit/<int:story_id>/', views.edit_story, name='edit-story'),
    path('delete/<int:story_id>/', views.delete_story, name='delete-story'),
    path('list', views.loloutplay_story_list, name='loloutplays_story_list'),
    path('list/<int:story_id>', views.loloutplay_story_detail, name='story-detail'),
    path('add_comment/<int:story_id>/', views.add_comment, name='add-comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit-comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete-comment'),
]