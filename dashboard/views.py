from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Health, General, Friend
from articles.models import Article
from django.contrib.auth.models import User
from .import forms
from django.contrib.auth.forms import UserChangeForm
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# not going to correct user; check out profile.html and findAccountabilityPartners.html
@login_required(login_url="/accounts/login/")
def profile_detail(request, pk=None):
    if pk:
        otherUser = User.objects.get(pk=pk)
        otherHealthInfo = Health.objects.filter(author_id=otherUser.pk)
        otherGeneralInfo = General.objects.filter(author_id=otherUser.pk)
        article = Article.objects.filter(author=otherUser.pk)
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {
            'healths':otherHealthInfo, 'generals':otherGeneralInfo,
            'posts':article, 'users':users, 'friends':friends
        }
        return render(request, 'dashboard/otherUserProfile.html', args)
    else:
        users = User.objects.filter(username=request.user)
        healthInfo = Health.objects.filter(author=request.user)
        generalInfo = General.objects.filter(author=request.user)
        article = Article.objects.filter(author=request.user)

        args = {
            'healths':healthInfo,'generals':generalInfo, 'users':users, 'posts':article
        }
        return render(request, 'dashboard/profile.html', args)

@login_required(login_url="/accounts/login/")
def awards_detail(request):
    return render(request, 'dashboard/awards.html')

@login_required(login_url="/accounts/login/")
def myAccountabilityPartners_detail(request):
    healthInfo = Health.objects.exclude(author=request.user.id)
    generalInfo = General.objects.exclude(author=request.user.id)
    users = User.objects.exclude(id=request.user.id)
    friend, created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all().order_by('first_name')

    args = {
        'healths':healthInfo,'generals':generalInfo, 'users':users, 'friends':friends
    }
    return render(request, 'dashboard/myAccountabilityPartner.html', args)

@login_required(login_url="/accounts/login/")
def findAccountabilityPartners_detail(request):
    healthInfo = Health.objects.all()
    generalInfo = General.objects.all()
    # exclude the current user
    users = User.objects.exclude(id=request.user.id)
    # auto add user with ",created" and "_or_create"
    friend, created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all()

    args = {
        'healths':healthInfo, 'generals':generalInfo, 'users':users, 'friends':friends
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
        # {'generalInfo': form } relates to "{{ generalInfo.as_p }}" in generalForm.html
        args = {'generalInfo': form}
    return render(request, 'dashboard/generalForm.html', args)

@login_required(login_url="/accounts/login/")
def editHealth_view(request):
    if request.method == 'POST':
        form = forms.EditHealthForm(request.POST, instance=request.user)

        if form.is_valid():
            health = Health.objects.get(author=request.user)
            #getting the data from post request
            health.gender=request.POST.get('gender')
            health.gender=request.POST.get('mental')
            health.gender=request.POST.get('food')
            health.gender=request.POST.get('sleep')
            health.gender=request.POST.get('exercise')
            health.age=request.POST.get('age')

            #saving health form
            health.save()
            form.save()
            return redirect('dashboard:profilePage')

    else:
        form = forms.EditHealthForm(instance=request.user)
        args = {'form':form}
        return render(request, 'dashboard/editHealth.html', args)

@login_required(login_url="/accounts/login/")
def editGeneral_view(request):
    if request.method == 'POST':
        form = forms.EditGeneralForm(request.POST, instance=request.user)

        if form.is_valid():
            general = General.objects.get(author=request.user)
            #getting the data from post request
            general.thumbnail=request.POST.get('thumbnail')
            general.location=request.POST.get('location')
            general.bio=request.POST.get('bio')
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
        args = {'form':form}
        return render(request, 'dashboard/editGeneral.html', args)

@login_required(login_url="/accounts/login/")
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)

    return redirect('dashboard:mapPage')
