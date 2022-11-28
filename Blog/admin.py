from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.
class FrameAdmin(admin.ModelAdmin):
    list_display = ['frameName', 'numberOfPart', 'numberOfImage', 'htmlFileName']
    # inlines = [city,image]
    list_editable = ('numberOfPart', 'numberOfImage', 'htmlFileName')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'frame', 'create', 'update', 'author', 'status']
    # inlines = [city,image]
    list_editable = ('status',)


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


admin.site.register(Frame, FrameAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticlePart, ArticlePartAdmin)
admin.site.register(ArticleImg, ArticleImgAdmin)
admin.site.register(ArticleLink, ArticleLinkAdmin)
admin.site.register(SpecialPosition, SpecialPositinAdmin)
