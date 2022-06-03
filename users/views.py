from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def login_users(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
         login(request, user)
         return redirect('homepage')
        
        else:
            messages.success(request,('You information is not valid'))
            return redirect('login')
         
    else:

     return render(request,'auth/login_users.html')

def logout_users(request):  
    logout(request) 
    messages.success(request,('You have been logged out successfully'))
    return redirect('homepage')

# def register(request):
#     form= UserCreationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         username=form.cleaned_data.get('username')
#         password=form.cleaned_data.get('password')
#         messages.success(request,(f'Account for {username} and {password} was successfully registered'))

#         return redirect('homepage')
#     else:
#           form= UserCreationForm()

#     return render(request,'auth/register.html',{'form': form})


