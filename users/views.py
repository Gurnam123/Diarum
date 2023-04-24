"""User creation, input validation"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import forms


def register(request):
    """User validation at registeraion form"""
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # cleaned data is a dictionary
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, you're account is created, please login.")
            return redirect('user-login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    """return profile page"""
    return render(request, 'users/profile.html')
