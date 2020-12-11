from django.conf.urls import url
from . import views
from .views import ArticleDeleteView, ArticleEditView

app_name= 'article'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', ArticleEditView.as_view(), name="edit"),
    url(r'^(?P<slug>[\w-]+)/delete/$', ArticleDeleteView.as_view(), name="delete"),
]
