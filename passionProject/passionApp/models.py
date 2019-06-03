from django.db import models
# from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

# 2
class NaniEntryModel(models.Model):
    topic = models.CharField(max_length=200, default="", blank=False)
    date = models.DateTimeField(default=datetime.now)
    image = models.FileField(upload_to='images', blank=True)
    entry = models.TextField(max_length=5000, default="", blank=True)
    video = models.FileField(upload_to='videos', null=True, verbose_name="", blank=True)
    URL_link = models.CharField(max_length=200, default="", blank=True)


# 3
class DiscussionEntryModel(models.Model):
    topic = models.CharField(max_length=200, default="", blank=False)
    date = models.DateTimeField(default=datetime.now)
    image = models.FileField(upload_to='images', blank=True)
    entry = models.TextField(max_length=5000, default="", blank=False)
    video = models.FileField(upload_to='videos', blank=True, verbose_name="")
    URL_link = models.URLField()


# comment form
class CommentEntryModel(models.Model):
    comment = models.CharField(max_length=200, blank=False)
    # discussion = models.ForeignKey(DiscussionEntryModel, on_delete=models.CASCADE, null=True, blank=True)


# 4. Gallery Form


class GalleryEntryModel(models.Model):
    event = models.CharField(max_length=200, blank=True, default="")
    image = models.FileField(upload_to='images', blank=False)
    imageDetails = models.TextField(max_length=400, blank=True)
    date = models.DateField(blank=True)


# 5.Upcoming Events

class UpcomingEventsEntryModel(models.Model):
    event= models.CharField(max_length=200, blank=False)
    Date = models.DateField()
    location = models.CharField(max_length=200, blank=False)
    eventFlyer = models.FileField(upload_to='flyers', blank=False,)


# 6. Library
class LibraryEntryModel(models.Model):
    title = models.CharField(max_length=200, blank=False, default="")
    cover = models.FileField(upload_to='books')
    link = models.URLField()


#7 Membership form that is not going to be implemented until everything else is complete

class MembershipEntryModel(models.Model):
    name=models.CharField(max_length=200, default="", blank=False)
    email=models.EmailField(max_length=200, blank=False)
    profilePic = models.FileField(upload_to='profilePics', blank=True)
    moto = models.CharField(max_length=300, blank=True)
    password = models.CharField(max_length=20, blank=False)




