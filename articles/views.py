from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from dashboard.models import Health
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from .import urls
import os
# to stop the code and view in terminal use print(text here)pdb.set_trace()
import pdb
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm

@login_required(login_url="/accounts/login/")
def article_list(request):
    articles = Article.objects.all().order_by('-date')
    userImage = Health.objects.all()
    args = {
        'theArticles':articles,
        'userImages':userImage,
    }
    return render(request, "articles/articleList.html", args)

@login_required(login_url="/accounts/login/")
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    #queryset to retrieve all the approved comments from the database.
    #.comments is the related_name in models.py
    # comments = article.comments.filter(approvedComment=False)
    comments = article.comments.all()
    newComment = None
    if request.method == 'POST':
        commentForm = forms.CreateComment(data=request.POST)
        if commentForm.is_valid():
            # Create Comment object but don't save to database yet
            newComment = commentForm.save(commit=False)
            newComment.author = request.user
            # Assign the current post to the comment
            newComment.post = article
            # Save the comment to the database
            newComment.save()
            return redirect('article:detail', slug=article.slug)
    else:
        commentForm = forms.CreateComment()
        args = {
            'article': article, 'comments': comments, 'newComment': newComment,
            'commentForm': commentForm,
        }
    return render(request, 'articles/articleDetail.html', args)

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

# class based view to delete article
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/deleteConfirm.html'
    success_url = reverse_lazy('article:list')

# class based view to edit article
class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/editArticle.html'
    fields = ['title','body','slug']
    success_url = reverse_lazy('article:list')
