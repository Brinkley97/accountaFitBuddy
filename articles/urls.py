from . import views
from django.conf.urls import url
from .views import ArticleCreateView, ArticleDeleteView, ArticleEditView

app_name= 'article'

urlpatterns = [
    url(r'^$', views.articleList, name="list"),
    url(r'^mental/$', views.mentalArticlesList, name="mental"),
    url(r'^food-nutrition/$', views.foodArticlesList, name="food"),
    url(r'^sleep/$', views.sleepArticlesList, name="sleep"),
    url(r'^exercise/$', views.exerciseArticlesList, name="exercise"),
    url(r'^(?P<slug>[\w-]+)/like/$', views.likeArticle, name="like"),
    # url(r'^create/$', views.article_create, name="create"),
    url(r'^create/$', ArticleCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', ArticleEditView.as_view(), name="edit"),
    url(r'^(?P<slug>[\w-]+)/delete/$', ArticleDeleteView.as_view(), name="delete"),
]
