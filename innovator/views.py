from django.shortcuts import render, redirect, get_object_or_404
from myadmin.models import Category, Subcategory, State, City
from innovator.forms import IdeaForm, PhotoUploadForm
from innovator.models import Idea
from django.contrib.auth.models import User
from myadmin.models import Profile
from django.contrib import messages
import json
from django.http import JsonResponse
from customer.models import Feedback, Order

def dashboard(request):
    user = User.objects.get(pk=request.user.id)
    context = {'row':user}
    return render(request, 'innovator/dashboard.html', context)

def editprofile(request):
    profile = Profile.objects.get(user=request.user)
    user = User.objects.get(id=request.user.id)
    states = State.objects.all()
    cities = City.objects.all()

    
    if request.method == 'POST':
        user.first_name = request.POST['fname']
        user.last_name  = request.POST['lname']
        user.email  = request.POST['email']
        try:
            user.save()
            profile.contact = request.POST['contact']
            profile.experience = request.POST['experience']
            profile.about = request.POST['about']
            profile.address = request.POST['address']
            profile.designation = request.POST['designation']
            profile.state_id = int(request.POST['state'])
            profile.city_id = int(request.POST['city'])
            profile.save()
            messages.success(request, 'You have Successfully Updated Profile') 
        except:
            messages.error(request, 'Failed to Update Profile') 
    
    context = {'p':profile, 'u':user, 'row':user, 'cities':cities, 'states':states}
    return render(request, 'innovator/profile.html', context)

def add_idea(request):
    if request.method == 'POST':
        obj = IdeaForm(request.POST, request.FILES)
        if obj.is_valid():
            newobj = obj.save(commit=False)
            newobj.user = request.user
            newobj.save()
    else:
        obj = IdeaForm()

    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {'categories': categories, 'subcategories': subcategories, 'form': obj}
    return render(request, 'innovator/add_idea.html', context)


def all_idea(request):
    user = request.user
    result = Idea.objects.filter(user_id=user.id)
    context = {'result':result}
    return render(request, 'innovator/all_idea.html',context)

def delete_idea(request, id):
    row = Idea.objects.get(id=id)
    row.delete()
    return redirect('/innovator/all_idea')


def orders(request):
    user = request.user
    result = Order.objects.filter(innovator_id=user.id)
    context = {'result':result}
    return render(request, 'innovator/orders.html', context)


def inquiry(request):
    return render(request, 'innovator/inquiry.html')


def feedback(request):
    return render(request, 'innovator/feedback.html')


def upload_profile_pic(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        form = PhotoUploadForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            profile.save()
            filename = request.FILES['profile_photo'].name
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully','image':filename})
        else:
            return JsonResponse({'error': True, 'errors': form.errors})
        
    else:
        form = PhotoUploadForm()
    
    context = {'form': form}
    return render(request, 'innovator/profile.html', context)
