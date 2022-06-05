"""oibp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from myadmin import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('add_cat', views.add_cat, name='add_cat'),
    path('all_cat', views.all_cat, name='all_cat'),
    path('delete_cat/<int:id>', views.delete_cat, name='delete_cat'),
    path('edit_cat/<int:id>', views.edit_cat, name='edit_cat'),
    path('update_cat/<int:id>', views.update_cat, name='update_cat'),
    path('add_sub', views.add_sub, name='add_sub'),
    path('all_sub', views.all_sub, name='all_sub'),
    path('delete_subcat/<int:id>', views.delete_subcat, name='delete_subcat'),
    path('edit_subcat/<int:id>', views.edit_subcat, name='edit_subcat'),
    path('update_subcat/<int:id>', views.update_subcat, name='update_subcat'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('orders', views.orders, name='orders'),
    path('feedback', views.feedback, name='feedback'),
    path('ideas', views.ideas, name='ideas'),
    path('innovators', views.innovators, name='innovators'),
    path('customers', views.customers, name='customers'),
    path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
