from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from dashboard.models import Health, General
from django.contrib.auth.models import User
from .models import Article, Comment
# from .forms import CreateArticle, CreateComment
from .import forms
from .import urls
import pdb # to stop the code and view in terminal use print(text here)pdb.set_trace()
import os

@login_required(login_url="/accounts/login/")
def articleList(request):
    article = Article.objects.all().order_by('-date')
    generalInfo = General.objects.all()
    otherUser = User.objects.exclude(id=request.user.id)
    user = User.objects.filter(username=request.user)
    args = {
        'theArticles':article,
        'userImages':generalInfo, 'otherUsers':otherUser,
        'users':user,
    }
    return render(request, "articles/articleList.html", args)

@login_required(login_url="/accounts/login/")
def likeArticle(request, slug):
    #filling out a form and submitting it
    #when submit, grab request.POST.get the postId from articleList like button name
    #look up the postId in the Article table
    article = get_object_or_404(Article, id=request.POST.get('postId'))
    liked = False
    #see if current user likes the post
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        #save the like to the table as that specific user
        article.likes.add(request.user)
        liked = True
    #return redirect to same page without noticing they have done anything
    #return the reverse of article list and the exact id with str(slug)
    return HttpResponseRedirect(reverse_lazy('article:detail', args=[str(slug)]))

@login_required(login_url="/accounts/login/")
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    #totalLikes() coming from function in models
    likesTotal = article.totalLikes()
    liked = False
    #if requested user likes article
    if article.likes.filter(id=request.user.id).exists():
        liked = True
    #queryset to retrieve all the approved comments from the database.
    #.comments is the related_name in models.py
    # comments = article.comments.filter(approvedComment=False)
    comments = article.comments.all().order_by('-date')
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
            'totalLikes':likesTotal, 'article':article, 'like':liked,
            'comments':comments,'newComment':newComment,
            'commentForm':commentForm,
        }
    return render(request, 'articles/articleDetail.html', args)

#class based view to create article
class ArticleCreateView(LoginRequiredMixin, CreateView):
    form_class = forms.CreateArticle
    template_name = 'articles/articleCreate.html'
    success_url = reverse_lazy('article:list')

    #check to see if form is valid
    def form_valid(self, form):
        #get whatever the object (this case the author) is in form
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)

#class based view to edit article
class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/editArticle.html'
    fields = ['topic','title','body','slug']
    success_url = reverse_lazy('article:list')

# class based view to delete article
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/deleteConfirm.html'
    success_url = reverse_lazy('dashboard:profilePage')

@login_required(login_url="/accounts/login/")
def mentalArticlesList(request):
    article = Article.objects.filter(topic=['Mental']).order_by('-date')
    generalInfo = General.objects.all()
    args = {
        'articles':article, 'userImages':generalInfo
    }
    return render(request, "articles/mentalArticleList.html", args)

@login_required(login_url="/accounts/login/")
def foodArticlesList(request):
    article = Article.objects.filter(topic=['Food']).order_by('-date')
    generalInfo = General.objects.all()
    args = {
        'articles':article, 'userImages':generalInfo
    }
    return render(request, "articles/foodArticleList.html", args)

@login_required(login_url="/accounts/login/")
def sleepArticlesList(request):
    article = Article.objects.filter(topic=['Sleep']).order_by('-date')
    generalInfo = General.objects.all()
    args = {
        'articles':article, 'userImages':generalInfo
    }
    return render(request, "articles/sleepArticlesList.html", args)

@login_required(login_url="/accounts/login/")
def exerciseArticlesList(request):
    article = Article.objects.filter(topic=['Exercise']).order_by('-date')
    generalInfo = General.objects.all()
    args = {
        'articles':article, 'userImages':generalInfo
    }
    return render(request, "articles/exerciseArticlesList.html", args)
