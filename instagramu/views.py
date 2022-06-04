from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
# Create your views here.
# def homepage(request):
#     return render(request, 'insta/homepage.html')

def homepage(request):
    Images = Image.get_images()
    comments = Comment.get_comment()
    profile = Profile.get_profile()

    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('homepage')

    else:
        form = CommentForm()

    return render(request,"insta/homepage.html",{"Images":Images, "comments":comments,"form": form,"profile":profile})

def user_profile(request,profile_id):
    profile = Profile.objects.get(pk = profile_id)
    Images = Image.objects.filter(profile_id=profile).all()

    return render(request,"profile/profile.html",{"profile":profile,"Images":Images})

def like(request,operation,pk):
    image = get_object_or_404(Image,pk=pk)
    if operation == 'like':
        image.likes += 1
        image.save()
    elif operation =='unlike':
        image.likes -= 1
        image.save()
    return redirect('homepage')


def add_user_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = NewProfileForm()
    return render(request, 'profile/new_user_profile.html', {"form": form})


def search_results(request):
    current_user = request.user
    profile = Profile.get_profile()
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_name = Profile.find_profile(search_term)
        message = search_term

        return render(request,'insta/search.html',{"message":message,"profiles":profile,"user":current_user,"username":searched_name})
    else:
        message = "You haven't searched for any username"
        return render(request,'insta/search.html',{"message":message})

def user_comments(request,pk):
    image = get_object_or_404(Image, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.poster = current_user
            comment.save()
            return redirect('homepage')
    else:
        form = CommentForm()
        return render(request,'insta/comment.html',{"user":current_user,"comment_form":form})


def follow(request,operation,id):
    current_user=User.objects.get(id=id)
    if operation=='follow':
        Follow.follow(request.user,current_user)
        return redirect('homepage')
    elif operation=='unfollow':
        Follow.unfollow(request.user,current_user)
        return redirect('homepage')
    
def upload_image(request):
    current_user = request.user
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.posted_by = current_user
                    upload.profile = profile
                    upload.save()
                    return redirect('homepage')
            else:
                form = UploadForm()
            return render(request,'insta/upload.html',{"user":current_user,"form":form})


def login_user(request):  
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
            else:
               
                return HttpResponseRedirect(reverse("login"))

        else:
            messages.success(request,('Invalid Information,Try Again!!'))
            return HttpResponseRedirect(reverse("login")) 
    else:
        return render(request, "registration/login.html",)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register_user(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = Profile()
            user_profile.user = user
            user_profile.save()
            registered = True

            return HttpResponseRedirect(reverse("login"))

        else:
            pass

    else:
        user_form = UserForm()
        
    return render(request, "registration/register.html", context={"user_form":user_form,"registered":registered})
