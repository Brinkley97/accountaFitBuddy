from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
import os
# to stop the code and view in terminal use print(text here)pdb.set_trace()
import pdb
from django.utils.datastructures import MultiValueDictKeyError

def article_list(request):
    articles = Article.objects.all().order_by('-date')
    args = {
        'theArticles':articles
    }
    return render(request, "articles/articleList.html", args)

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/articleDetail.html', {'article': article})

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
                try:
                    imageFile = request.FILES['image'].name
                    imageExtention = os.path.splitext(imageFile)[1]
                    if imageExtention == '.jpeg':
                        instance.videoFile = os.path.splitext(imageFile)[0] + '.jpg'
                        instance.save()
                except MultiValueDictKeyError:
                    image = False

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
        return render(request, 'articles/articleCreate.html', args)
    else:
        form = forms.CreateArticle()

        args = {
            'form':form
        }
        return render(request, 'articles/articleCreate.html', args)
