from django.shortcuts import render, redirect
from myadmin.forms import CategoryForm, SubcategoryForm
from myadmin.models import Category, Subcategory, Profile
from customer.models import Contact
from innovator.models import Idea
from django.contrib.auth.models import User
from django.contrib import auth
from customer.models import Feedback, Order
from django.contrib import messages

def dashboard(request):
	return render(request, 'myadmin/dashboard.html')

def profile(request, id):
	idea= Idea.objects.get(id=id)
	context = {'row': idea}
	return render(request, 'myadmin/profile.html', context)

#categories
def add_cat(request):
	if request.method == 'POST':
		obj = CategoryForm(request.POST)
		if obj.is_valid():
			obj.save()
			return redirect('/myadmin/all_cat')
	else:
		obj = CategoryForm()
	return render(request, 'myadmin/add_cat.html')

def all_cat(request):
	result = Category.objects.all()
	context = {'result':result}
	return render(request, 'myadmin/all_cat.html', context)

def delete_cat(request, id):
	row = Category.objects.get(id=id)
	row.delete()
	return redirect('/myadmin/all_cat')

def edit_cat(request, id):
	category = Category.objects.get(id=id)
	context = {'row':category}
	return render(request, 'myadmin/edit_cat.html', context)


def update_cat(request, id):
	category = Category.objects.get(id=id)
	
	if request.method == 'POST':
		obj = CategoryForm(request.POST, instance=category)
		if obj.is_valid():
			obj.save()
			return redirect('/myadmin/all_cat')

#subcategories
def add_sub(request):
	categories = Category.objects.all()

	if request.method == 'POST':
		obj = SubcategoryForm(request.POST)
		if obj.is_valid():
			obj.save()
			return redirect('/myadmin/all_sub')
	else:
		obj = SubcategoryForm()
	
	context = {'result': categories, 'form':obj}
	return render(request, 'myadmin/add_sub.html', context)

def all_sub(request):
	result = Subcategory.objects.all()
	context = {'result':result}
	return render(request, 'myadmin/all_sub.html', context)

def edit_subcat(request, id):
	categories = Category.objects.all()
	
	subcategory = Subcategory.objects.get(id=id)
	context = {'row':subcategory, 'result': categories}
	return render(request, 'myadmin/edit_subcat.html', context)

def update_subcat(request, id):
	subcategory = Subcategory.objects.get(id=id)
	
	if request.method == 'POST':
		obj = SubcategoryForm(request.POST, instance=subcategory)
		if obj.is_valid():
			obj.save()
			return redirect('/myadmin/all_sub')


def delete_subcat(request, id):
	row = Subcategory.objects.get(id=id)
	row.delete()
	return redirect('/myadmin/all_sub')

def orders(request):
	result = Order.objects.all()
	context = {'result':result}
	return render(request, 'myadmin/orders.html', context)

def inquiry(request):
	result = Contact.objects.all()
	context = {'result':result}
	return render(request, 'myadmin/inquiry.html', context)

def feedback(request):
	return render(request, 'myadmin/feedback.html')

def ideas(request):
	result = Idea.objects.all()
	context = {'result': result}
	return render(request, 'myadmin/idea.html', context)

def innovators(request):
	result = Profile.objects.filter(role_id=2)
	context = {'result': result}
	return render(request, 'myadmin/innovators.html', context)

def customers(request):
	result = Profile.objects.filter(role_id=1)
	context = {'result': result}
	return render(request, 'myadmin/customers.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
        	messages.error(request, 'InvalidUsername or password')
        	return redirect('/myadmin/login')
        else:
            auth.login(request, user)
            return redirect('/myadmin/dashboard')
    else:
        context = {}
        return render(request, 'myadmin/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/myadmin/login')


def feedback(request):
	result = Feedback.objects.all()
	context = {'result':result}
	return render(request, 'myadmin/feedback.html', context)