from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import *


def register(request):
    if request.method == "POST":
        user = FormUser(request.POST, request.FILES)
        if user.is_valid():
            user_cleaned_data = user.cleaned_data
            created_user = user.save()
            CustomUser.objects.create(user=created_user, image_to=user_cleaned_data["my_images"])
            return redirect("/home/")
    else:
        user = FormUser()
    return render(request, "blog/register.html", {"form": user})


@login_required
def update_profile(request):
    if request.method == "POST":
        user = UpdateProfile(instance=request.user, data=request.POST, files=request.FILES)
        if user.is_valid():
            user_cleaned_data = user.cleaned_data
            update_user = user.save()
            get_profile = CustomUser.objects.get(user=update_user)
            get_profile.image_to = user_cleaned_data["my_images"]
            get_profile.save()
            return redirect("/home/")
    else:
        user = UpdateProfile()
    return render(request, "blog/update_profile.html", {"form": user})


@login_required
def get_profile(request):
    obj = CustomUser.objects.get(user=request.user)
    return render(request, "blog/view_profile.html", {"object": obj})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'blog/change_password.html', {'form': form})
