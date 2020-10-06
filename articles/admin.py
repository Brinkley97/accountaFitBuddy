from django.contrib import admin
from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment', 'date', 'approvedComment')
    list_filter = ('approvedComment', 'date')
    search_fields = ('post', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approvedComment=True)
