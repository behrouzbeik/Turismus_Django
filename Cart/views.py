from django.shortcuts import render,redirect
from Home.models import *
# Create your views here.

class MyTraveler:
    def __init__(self, selectarticle):
        self.tour  =  models.ForeignKey ( Tour,on_delete=models.CASCADE,blank=True,null=True )
        self.transport  =  models.ForeignKey ( Transport,on_delete=models.CASCADE,blank=True,null=True )
        self.room  =  models.ForeignKey ( Room,on_delete=models.CASCADE,blank=True,null=True )
        self.adult = models.PositiveIntegerField(  )
        self.child = models.PositiveIntegerField(blank=True,null=True)
        self.baby = models.PositiveIntegerField(blank=True,null=True)
        self.user  =  models.ForeignKey ( CustomUser,on_delete=models.CASCADE )
        self.traveler = 1


class MyCart:
    def __init__(self, selectObject, objectType, userid):
        if objectType == "tour" :
            self.tour=Tour.objects.get(Tour_id=selectObject.id)
            self.transport={}
            self.room={}
        elif objectType=="transport":
            self.tour={}
            self.transport=Transport.objects.get(Transport_id=selectObject.id)
            self.room={}
        elif objectType=="room":
            self.tour={}
            self.transport={}
            self.room=Room.objects.get(Room_id=selectObject.id)
        if objectType=="transport":
            self.transport=Transport.objects.get(Transport_id=selectObject.id)
        self.adult=0 
        self.child=0
        self.baby =0
        self.user =CustomUser.objects.get(CustomUser_id=userid)
        self.traveler={}

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

def tourbooking(request,tourid):
    tour = Tour.objects.get(id=tourid)

    context = {'tour':tour}
    return (render(request,'Cart/tourBooking.html', context))