from django.shortcuts import render, redirect, get_object_or_404
from myadmin.models import Category, Subcategory
from django.core import serializers
from django.http import HttpResponse
from customer.models import Contact, Order
from customer.forms import ContactForm, FeedbackForm
from django.contrib.auth.models import User
from myadmin.models import Profile
from django.contrib import messages
from django.contrib import auth
from innovator.models import Idea
import razorpay
from django.views.decorators.csrf import csrf_exempt

def home(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {'categories': categories, 'subcategories': subcategories}
    return render(request, 'customer/index.html', context)


def about(request):
    context = {}
    return render(request, 'customer/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        else:
            pass
    else:
        form = ContactForm()
        print(form)
    context = {'form': form}
    return render(request, 'customer/contact.html', context)

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        role = int(request.POST['role'])

        if password == cpassword:
            user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password)
            
            try:
                user.save()
                profile = Profile.objects.create(role_id=role, user=user)
                profile.save()
                messages.success(request, 'You have Successfully Registered')    
            except:
                 messages.error(request, 'Error Occured in Registration')

        else:
            messages.error(request, 'password & Confirm password not matched')

        context = {}
        return render(request, 'customer/signup.html', context)
    else:
        context = {}
        return render(request, 'customer/signup.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Username or password')
            return redirect(login)
        else:
            auth.login(request, user)
            role_id = user.innovatorprofile.role_id
            if role_id == 1:
                return redirect('/')
            else:
                return redirect('/innovator/dashboard')
    else:
        context = {}
        return render(request, 'customer/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/customer/login')


def search(request):
    if request.method == 'POST':
        cat_id = request.POST['cat_id']
        subcategories = Subcategory.objects.filter(category_id=cat_id)
        subcategories_serialized = serializers.serialize('json', subcategories)
        # return JsonResponse(subcategories_serialized, safe=False)
        return HttpResponse(subcategories_serialized, content_type='application/json')
    else:
        return HttpResponse('Product Creation failed')


def ideas(request):
    if request.method == 'POST':
        cat = Category.objects.get(id=int(request.POST['category']))
        sub = Subcategory.objects.get(id=int(request.POST['subcategory']))
        idea = Idea.objects.filter(category=cat, subcategory=sub)
        categories = Category.objects.all()

        context= {'idea': idea,'categories': categories}
        return render(request, 'customer/ideas.html', context)
    else:
        idea = Idea.objects.all().order_by('-id')[:3]
        categories =  Category.objects.all()
        context = {'idea':idea, 'categories':categories}
        return render(request, 'customer/ideas.html', context)

def idea_details(request, id):
    idea = Idea.objects.get(id=id)
    context= {'idea': idea}
    return render(request, 'customer/ideas-details.html', context)

def add_to_cart(request, id):
    user = request.user
    idea = Idea.objects.get(id=id)
    request.session['idea_id'] = idea.id
    request.session['title'] = idea.title
    request.session['duration'] = idea.setup_duration
    request.session['price'] = idea.setup_price
    return redirect('/customer/shopping_cart')

def shopping_cart(request):
    if request.session.has_key('idea_id'):
        idea_detail = {'idea_id':request.session['idea_id'], 'title': request.session['title'],'duration':request.session['duration'],'price':request.session['price']}
        context= {'idea_detail':idea_detail}
        return render(request, 'customer/shopping-cart.html', context)
    else:
        context = {}
        return render(request, 'customer/shopping-cart.html', context)

def clear_all_cart(request):
    del request.session['idea_id']
    del request.session['title']
    del request.session['duration']
    del request.session['price']
    return redirect('/customer/ideas')

def order(request):
    idea_id = request.session['idea_id']
    idea = Idea.objects.get(id=idea_id)
    user = request.user
    order = Order();
    order.title = request.session['title']
    order.duration = request.session['duration']
    order.price = request.session['price']
    order.idea = idea
    order.user = user
    order.innovator_id = idea.user_id
    order.save()
    # del request.session['idea_id']
    # del request.session['title']
    # del request.session['duration']
    # del request.session['price']
    # return redirect('/customer/ideas')
    return redirect('/customer/make_payment')

def myorders(request):
    user = request.user
    order = Order.objects.filter(user=user)
    context= {'order': order}


def make_payment(request):
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    amount = request.session['price']

    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        'amount': amount,
        'currency': 'INR',
        "receipt":"OIBP",
        "notes":{
            'name' : 'AK',
            'payment_for':'OIBP Test'
        }
    }
    id = request.user.id
    result = User.objects.get(pk=id)
    payment = client.order.create(data=data)
    context = {'payment' : payment,'result':result}
    return render(request, 'customer/process_payment.html',context)

@csrf_exempt
def success(request):
    return render(request, "customer/payment_done.html")


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user =request.user
            try:
                feedback.save()
                messages.success(request, 'Feedback Submitted Successfully..')
                return redirect('feedback')
            except:
                messages.error(request, 'Error Occured in Feedback')
                return redirect('feedback')
        else:
            context = {'form': form}
            return render(request, 'customer/feedback.html', context)
    else:
        form = FeedbackForm()
    context = {'form': form}
    return render(request, 'customer/feedback.html', context)