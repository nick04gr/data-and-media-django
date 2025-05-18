# account/views.py
from django.shortcuts import render,  redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return HttpResponseRedirect(reverse_lazy('blog:post_list'))  
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')  

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:profile')
    else:
        form = UserProfileForm(instance=request.user.profile, user=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})

