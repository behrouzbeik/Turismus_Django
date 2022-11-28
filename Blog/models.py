from django.db import models
from Account.models import CustomUser

# Create your models here.
class Frame(models.Model):
    frameName = models.CharField(max_length=20)
    numberOfPart = models.PositiveIntegerField()
    numberOfImage = models.PositiveIntegerField()
    htmlFileName = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Frame', blank=True, null=True)

    def __str__(self):
        return self.frameName


class Article(models.Model):
    STATUS_CHOISES =(
        ('pub' , 'Published'),
        ('drf', 'Draft'),
    )
    title = models.CharField(max_length=50)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey( CustomUser, on_delete=models.CASCADE )
    status = models.CharField(choices=STATUS_CHOISES,max_length=3,default='drf')
    # is_remove = models.BooleanField(default=False) # True / False

    def __str__(self):
        return self.title


class ArticlePart(models.Model):
    partTitle = models.CharField(max_length=50)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    partOrder = models.PositiveIntegerField()

    def __str__(self):
        return self.partTitle


class ArticleImg(models.Model):
    title = models.CharField(max_length=15, default="0")
    image = models.ImageField(upload_to='Frame')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    imgOrder = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class ArticleLink(models.Model):
    title = models.CharField(max_length=50, default="0")
    link = models.CharField(max_length=150)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    linkOrder = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class SpecialPosition(models.Model):
    title = models.CharField(max_length=20)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

