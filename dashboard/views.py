from django.shortcuts import render, redirect
from .models import Health, General, Friend
from articles.models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def dashboard_detail(request):
    data = Health.objects.all()
    return render(request, 'dashboard/dashboard_detail.html', {'healthInfo': data})

# not going to correct user; check out profile.html and findAccountabilityPartners.html
@login_required(login_url="/accounts/login/")
def profile_detail(request, slug=None, pk=None):
    if pk:
        otherUser = User.objects.get(pk=pk)
        otherHealthInfo = Health.objects.filter(author_id=otherUser.pk)
        otherGeneralInfo = General.objects.filter(author_id=otherUser.pk)
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all

        args = {
            'otherH_list':otherHealthInfo,'otherG_list':otherGeneralInfo, 'users':users, 'friends':friends
        }
        return render(request, 'dashboard/otherUserProfile.html', args)
    else:
        users = User.objects.filter(username=request.user)
        healthInfo = Health.objects.filter(author=request.user)
        generalInfo = General.objects.filter(author=request.user)
        article = Article.objects.filter(author=request.user)

    return render(
        request, 'dashboard/profile.html',
        context={'infoH_list':healthInfo,'infoG_list':generalInfo, 'users':users, 'posts':article}
    )

@login_required(login_url="/accounts/login/")
def awards_detail(request):
    return render(request, 'dashboard/awards.html')

@login_required(login_url="/accounts/login/")
def myAccountabilityPartners_detail(request):
    healthInfoList = Health.objects.exclude(author=request.user.id)
    generalInfo = General.objects.exclude(author=request.user.id)
    users = User.objects.exclude(id=request.user.id)
    friend, created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all()

    args = {
        'healthInfo_list':healthInfoList,'infoG':generalInfo, 'users':users, 'friends':friends
    }
    return render(request, 'dashboard/myAccountabilityPartner.html', args)

@login_required(login_url="/accounts/login/")
def findAccountabilityPartners_detail(request):
    healthInfoList = Health.objects.all()
    generalInfo = General.objects.all()
    # exclude the current user
    users = User.objects.exclude(id=request.user.id)
    # auto add user with ",created" and "_or_create"
    friend, created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all()

    args = {
        'healthInfo_list':healthInfoList,'infoG':generalInfo, 'users':users, 'friends':friends
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
        form = forms.EditHealthForm(request.POST, instance=request.user)

        if form.is_valid():
            health = Health.objects.get(author=request.user)
            #getting the data from post request
            health.thumbnail=request.POST.get('thumbnail')
            health.gender=request.POST.get('gender')
            health.age=request.POST.get('age')
            health.weight=request.POST.get('weight')
            health.fit=request.POST.get('fit')
            health.goal=request.POST.get('goal')
            health.location=request.POST.get('location')
            #saving health form
            health.save()
            form.save()
            return redirect('dashboard:profilePage')

    else:
        form = forms.EditHealthForm(instance=request.user)
        args = {'form': form}
        return render(request, 'dashboard/editHealth.html', args)

@login_required(login_url="/accounts/login/")
def editGeneral_view(request):
    if request.method == 'POST':
        form = forms.EditGeneralForm(request.POST, instance=request.user)

        if form.is_valid():
            general = General.objects.get(author=request.user)
            #getting the data from post request
            general.group=request.POST.get('group')
            general.often=request.POST.get('often')
            general.ig=request.POST.get('ig')
            general.fb=request.POST.get('fb')
            general.twitter=request.POST.get('twitter')
            general.snap=request.POST.get('snap')
            general.whatsapp=request.POST.get('whatsapp')

            #saving general form
            general.save()
            form.save()
            return redirect('dashboard:profilePage')

    else:
        form = forms.EditGeneralForm(instance=request.user)
        args = {'form': form}
        return render(request, 'dashboard/editGeneral.html', args)

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)

    return redirect('dashboard:mapPage')
