from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.
class FrameAdmin(admin.ModelAdmin):
    list_display = ['frameName', 'numberOfPart', 'numberOfImage', 'htmlFileName']
    # inlines = [city,image]
    list_editable = ('numberOfPart', 'numberOfImage', 'htmlFileName')




class ArticlePartAdmin(admin.ModelAdmin):
    list_display = ['partTitle', 'partOrder']
    # inlines = [city,image]
    list_editable = ('partOrder',)


class ArticleImgAdmin(admin.ModelAdmin):
    list_display = ['title', 'article', 'image', 'imgOrder']
    # inlines = [city,image]
    list_editable = ('image', 'imgOrder',)


class ArticleLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'article', 'linkOrder']
    # inlines = [city,image]
    list_editable = ('linkOrder',)


class SpecialPositinAdmin(admin.ModelAdmin):
    list_display = ['title', 'article']
    # inlines = [city,image]
    list_editable = ('article',)


class ArticlePartInlines(admin.TabularInline):
    model = ArticlePart
    extra = 1


class ArticleLinkInlines(admin.TabularInline):
    model = ArticleLink
    extra = 1


class ArticleImgInlines(admin.TabularInline):
    model = ArticleImg
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'frame', 'create', 'update', 'author', 'status']
    inlines = [ArticlePartInlines,ArticleLinkInlines,ArticleImgInlines]
    list_editable = ('status',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'author', 'body', 'stars', 'active']
    list_editable = ('active',)



admin.site.register(Frame, FrameAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticlePart, ArticlePartAdmin)
admin.site.register(ArticleImg, ArticleImgAdmin)
admin.site.register(ArticleLink, ArticleLinkAdmin)
admin.site.register(SpecialPosition, SpecialPositinAdmin)
admin.site.register(Comment, CommentAdmin)
