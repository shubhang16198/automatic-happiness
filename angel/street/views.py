from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Profile
from django.http import HttpResponse

@login_required
def home(request):
    return render(request, 'profile.html', {'user':request.user})

def video(request):
    return render(request, 'video.html')

def start(request):
    return render(request,'index.html')

def performances(request):
    users = User.objects.all()
    return render(request , 'live.html', {'user1':users[0],'user2':users[1]})

def stream(request):
    return render(request,'stream.html')

    
def stream2(request):
    return render(request,'stream2.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST , request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.pic = form.cleaned_data.get('pic')
            user.mobile = form.cleaned_data.get('mobile')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'index.html', {'form': form})
