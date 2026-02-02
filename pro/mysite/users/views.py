from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

##########################################################
#                   FUNCTION BASED VIEWS                 #
##########################################################

## START OF REGISTER VIEW
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user        = form.save()
            username    = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {user.username}, your account has been created successfully')
            return redirect('myapp:index')
    context = {
        'form' : form
    }
    return render(request, 'users/register.html', context)
## END OF REGISTER VIEW

## START OF LOGOUT VIEW
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')
## END OF LOGOUT VIEW

## START OF PROFILE VIEW
@login_required
def profile(request):
    return render(request, 'users/profile.html')
## END OF PROFILE VIEW


