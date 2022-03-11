from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm, EditUserProfileForm
from .models import Profile

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)

    return render(request, 'users/profile.html', {'user': user, 'profile': profile})

@login_required
def edit_profile(request):
    form = EditUserProfileForm()

    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            username = form.cleaned_data['username']
            pic = form.cleaned_data['pic']

            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.bio = bio
            if pic:
                profile.pic = pic
            profile.save()
            return redirect('profile',username=user.username)

    return render(request, 'users/edit_profile.html', {'form': form})