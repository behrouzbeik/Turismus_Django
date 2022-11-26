from django.db import models
from Account import CustomUser

# Create your models here.
class Frame(models.Model):
    numberOfPart = models.PositiveIntegerField()
    numberOfImage = models.PositiveIntegerField()
    htmlFileName = models.CharField(max_length=20)


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


class ArticleImg(models.Model):
    image = models.ImageField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    imgOrder = models.PositiveIntegerField()



