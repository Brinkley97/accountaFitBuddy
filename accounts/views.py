from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import MyRegistrationForm
from django.contrib.auth import login, logout



# Creation your views here.
def signup_view(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:health')
    else:
        form = MyRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('article:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('article:list')


def editProfile_view(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('dashboard:profilePage')

    else:
        form = MyRegistrationForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)
