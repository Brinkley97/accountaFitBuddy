from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms


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
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            # instance.published_date = timezone.now()
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
