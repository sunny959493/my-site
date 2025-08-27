from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('uploads', views.uploads, name='uploads'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user_upload', views.user_upload, name='user_upload'),
    path('fav', views.fav, name='fav'),
    path('add_fav/<int:post_id>/', views.add_fav, name='add_fav')
]