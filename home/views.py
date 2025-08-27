from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import post, user_uploads, favourites
from django.contrib.auth.models import User, auth
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    content={}
    if request.method=='POST':
        content['name']=request.POST.get('name')
        content['email']=request.POST.get('email')
        content['message']=request.POST.get('message')
        content['submitted']=True
    return render(request, 'contact.html', content)

def uploads(request):
    posts=post.objects.all()
    user_upload=user_uploads.objects.all()
    return render(request, 'upload.html', {'posts': posts, 'user_uploads':user_upload})

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'user already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                #messages.success(request, 'user created successfully')
                return redirect('login')
        else:
            messages.info(request, 'password mismatch')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def user_upload(request):
    if request.method=='POST':
        place=request.POST['place']
        image=request.FILES['image']
        description=request.POST['description']

        user_uploads.objects.create(place=place, description=description, image=image)
        return redirect('uploads')

    else:
        return render(request, 'user_upload.html')

def add_fav(request, post_id):
    if request.method=='POST':
        post = get_object_or_404(user_uploads, id=post_id)
        favourites.objects.get_or_create(user=request.user, post=post)
    return redirect('fav')

def fav(request):
    posts = favourites.objects.filter(user=request.user)
    return render(request, 'favourites.html', {'posts': posts})