from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
import os
# to stop the code and view in terminal use print(text here)pdb.set_trace()
import pdb




# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {'theArticles':articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

def other_user_profile(request):
    # return HttpResponse(author)
    person = Article.objects.get()
    return render(request, 'articles/other_user_profile.html', {'person': person})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        files = request.FILES.getlist('video')
        # print(files)
        # pdb.set_trace()
        if form.is_valid():
            for f in files:
                instance = form.save(commit=False)
                instance.author = request.user
                videoFile = request.FILES['video'].name
                extention = os.path.splitext(videoFile)[1]
                if extention == '.MOV':
                    instance.videoFile = os.path.splitext(videoFile)[0] + '.mp4'
                    instance.save()
                else:
                    instance.videoFile = videoFile
            else:
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
            return redirect('article:list')
        args = {
            'form':form
        }
        return render(request, 'articles/article_create.html', args)
    else:
        form = forms.CreateArticle()

        args = {
            'form':form
        }
        return render(request, 'articles/article_create.html', args)
