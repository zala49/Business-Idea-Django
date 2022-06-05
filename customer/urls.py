from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('ideas', views.ideas, name='ideas'),
    path('idea_details/<int:id>', views.idea_details, name='idea_details'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('clear_all_cart', views.clear_all_cart, name='clear_all_cart'),
    path('order', views.order, name='order'),
    path('make_payment', views.make_payment, name='make_payment'),
    path('success', views.success, name='success'),
    path('feedback', views.feedback, name='feedback'),


]
