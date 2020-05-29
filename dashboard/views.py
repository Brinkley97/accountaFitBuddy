from django.shortcuts import render, redirect
from .models import Health, General, Friend
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from django.contrib.auth.models import User



# Create your views here.
def dashboard_detail(request):
    data = Health.objects.all()
    return render(request, 'dashboard/dashboard_detail.html', {'healthInfo': data})

# not going to correct user; check out profile.html and findAccountabilityPartners.html
@login_required(login_url="/accounts/login/")
def profile_detail(request, pk=None):
    if pk:
        otherUser = User.objects.get(pk=pk)
        otherHealthInfo = Health.objects.filter(author_id=otherUser.pk)
        otherGeneralInfo = General.objects.filter(author_id=otherUser.pk)
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {
            'otherH':otherHealthInfo,'otherG':otherGeneralInfo, 'users':users, 'friends':friends
        }

        return render(request, 'dashboard/otherUserProfile.html', args)
    else:
        users = User.objects.filter(username=request.user)
        healthInfo = Health.objects.filter(author=request.user)
        generalInfo = General.objects.filter(author=request.user)
    return render(request, 'dashboard/profile.html', context={'infoH':healthInfo,'infoG':generalInfo, 'users':users})


@login_required(login_url="/accounts/login/")
def awards_detail(request):
    return render(request, 'dashboard/awards.html')

@login_required(login_url="/accounts/login/")
def myAccountabilityPartners_detail(request):
    healthInfo = Health.objects.all()
    generalInfo = General.objects.exclude(author=request.user.id)
    users = User.objects.exclude(id=request.user.id)
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()

    args = {
        'infoH':healthInfo,'infoG':generalInfo, 'users':users, 'friends':friends
    }
    return render(request, 'dashboard/myAccountabilityPartner.html', args)

@login_required(login_url="/accounts/login/")
def findAccountabilityPartners_detail(request):
    healthInfo = Health.objects.all()
    generalInfo = General.objects.all()
    # exclude the current user
    users = User.objects.exclude(id=request.user.id)
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()

    args = {
        'infoH':healthInfo,'infoG':generalInfo, 'users':users, 'friends':friends
    }

    return render(request, 'dashboard/findingAccountabilityPartner.html', args)


@login_required(login_url="/accounts/login/")
def health_view(request):
    # form = Health.objects.all()
    if request.method == 'POST':
        form = forms.InsertHealth(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("dashboard:general")
    else:
        form = forms.InsertHealth()
        # {'healthInfo': form} relates to "{{healthInfo.as_p}}" in healthForm.html
    return render(request, 'dashboard/healthForm.html', {'healthInfo': form})

@login_required(login_url="/accounts/login/")
def general_view(request):
    if request.method == 'POST':
        form = forms.InsertGeneral(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("dashboard:profilePage")
    else:
        form = forms.InsertGeneral()
        # {'generalInfo': form} relates to "{{generalInfo.as_p}}" in generalForm.html
    return render(request, 'dashboard/generalForm.html', {'generalInfo': form})

@login_required(login_url="/accounts/login/")
def editHealth_view(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('dashboard:profilePage')

    else:
        form = forms.EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'dashboard/edit_health.html', args)

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)

    return redirect('dashboard:mapPage')
