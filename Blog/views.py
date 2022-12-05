import datetime
from django.shortcuts import render,redirect
from Home.models import *
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def bloglist(request):
    class counter():
        tour = Tour.objects.all().count()
        airplane = Transport.objects.filter(beginning__type='Pl').count()
        train = Transport.objects.filter(beginning__type='Tr').count()
        bus = Transport.objects.filter(beginning__type='BU').count()
        cruise = Transport.objects.filter(beginning__type='Cr').count()
        residence = Residence.objects.all().count()

    class MyArticle:
        def __init__(self, selectarticle):
            self.id = selectarticle.id
            self.img = ArticleImg.objects.get(article_id=selectarticle.id, imgOrder=1)
            self.part = ArticlePart.objects.get(article_id=selectarticle.id, partOrder=1)
            self.title = selectarticle.title
            self.create = selectarticle.create
            self.month = (datetime.datetime.strptime(str(self.create.month), "%m")).strftime("%b")
            self.update = selectarticle.update
            self.author = selectarticle.author
            self.status = selectarticle.status
    allArticles = Article.objects.all()
    articles = []
    
    for a in allArticles:
        if a.status == 'pub':
            articles.append(MyArticle(a))

    paginator = Paginator(articles,6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context = {
        'articles':page_obj,
        'page_num':page_num,
        'counter':counter,
        # 'articles':articles
    }
    return (render(request,'Blog/bloglist.html',context))


def blogdetail(request, articleid):

    class counter():
        tour = Tour.objects.all().count()
        airplane = Transport.objects.filter(beginning__type='Pl').count()
        train = Transport.objects.filter(beginning__type='Tr').count()
        bus = Transport.objects.filter(beginning__type='BU').count()
        cruise = Transport.objects.filter(beginning__type='Cr').count()
        residence = Residence.objects.all().count()

    class MyArticle:
        def __init__(self, selectarticle):
            self.id = selectarticle.id
            self.parts = ArticlePart.objects.filter(article_id=selectarticle.id).order_by('partOrder')
            # print('selectarticle.id', self.parts[0].partTitle)
            self.images = ArticleImg.objects.filter(article_id=selectarticle.id).order_by('imgOrder')
            self.links = ArticleLink.objects.filter(article_id=selectarticle.id).order_by('linkOrder')
            self.title = selectarticle.title
            self.frame = selectarticle.frame.htmlFileName
            # print('page', self.frame.htmlFileName)
            self.create = selectarticle.create
            self.month = (datetime.datetime.strptime(str(self.create.month), "%m")).strftime("%b")
            self.update = selectarticle.update
            self.author = selectarticle.author
            self.status = selectarticle.status
    # selectedArticle = SpecialPosition.objects.get(title='Homepage')
    myarticle = MyArticle(Article.objects.get(id=articleid))
    comments = Comment.objects.filter(article_id=articleid, active=True)
    context = {
        'counter':counter,
        'myarticle' : myarticle,
        'comments':comments,
    }
    return (render(request,'Blog/blogdetail.html',context))


def comment_create(request, articleid):
    url = request.META.get('HTTP_REFERER')
    comment = Comment(article=Article.objects.get(id=articleid), author=CustomUser.objects.get(id=request.user.id), body=request.POST['message'], stars=request.POST['rate'], active=False)
    comment.save()
    return redirect(url)