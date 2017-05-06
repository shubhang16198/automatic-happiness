# from django.shortcuts import render

# # Create your views here.
from .forms import SignUpForm
# def signup(request):
# 	if request.method == "POST":
# 		form  = SignUpForm(request.POST , request.FILES)
# 		if form.is_valid():
# 			user = form.save()
# 			user.refresh_from_db()
# 			user.profile.art = form.cleaned_data['art']
# 			user.profile.mobile_no = form.cleaned_data['mobile_no']
# 			user.save()
# 			raw_password = form.cleaned_data.get('password1')
# 			user = authenticate(username=user.username, password=raw_password)
# 			login(request, user)
# 			return HttpResponse("success")
# 	else:
# 		form = SignUpForm()
# 	return render(request, 'street/signup.html', {'form': form})
# 	
# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect

# from .forms import SignUpForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return HttpResponse("success")
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})