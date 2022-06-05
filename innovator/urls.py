from django.contrib import admin
from django.urls import path, include
from innovator import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_idea', views.add_idea, name='add_idea'),
    path('all_idea', views.all_idea, name='all_idea'),
    path('delete_idea/<int:id>', views.delete_idea, name='delete_idea'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('orders', views.orders, name='orders'),
    path('feedback', views.feedback, name='feedback'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('upload_profile_pic', views.upload_profile_pic, name='upload_profile_pic'),
    
]
