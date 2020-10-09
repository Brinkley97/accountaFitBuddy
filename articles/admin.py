from django.contrib import admin
from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    #display the properties mentioned in the tuple in the comments list for each comment.
    list_display = ('post', 'comment', 'date', 'approvedComment')
    #method will filter the comments based on the creation date and their active status
    list_filter = ('approvedComment', 'date')
    #will simply search the database for the parameters provided in the tuple.
    search_fields = ('post', 'comment')
    #method will help approve many comment objects at once,
    actions = ['approve_comments']

    #method is a simple function that takes a queryset and updates the active boolean field to True. 
    def approve_comments(self, request, queryset):
        queryset.update(approvedComment=True)
