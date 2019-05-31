from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import NaniEntryModel, DiscussionEntryModel, GalleryEntryModel, CommentEntryModel, LibraryEntryModel, \
    MembershipEntryModel, UpcomingEventsEntryModel
from .forms import NaniForm, DiscussionForm, CommentForm, GalleryForm, UpcomingEventForm, LibraryForm, MembershipForm


# Create your views here.


def index(request):
    return render(request, "passionApp/index.html")


# Front page where all the articles Athena and I Post that are informative regarding the whole Asian World


def addNani(request):
    form = NaniForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        NaniEntryModel.objects.create(topic=request.POST["topic"], date=request.POST["date"],
                                      image=request.POST["image"],
                                      entry=request.POST["entry"], video=request.POST["video"], URL_link=["URL_link"])
        return redirect("index")

    return render(request, "passionApp/addNani.html", context)


def viewAllNani(request):
    return HttpResponse("Everyone can view the info the admins post weather you are a member or not")


def editNani(request):
    return HttpResponse("Need to be able to edit any post made from the President and VP")


def deleteNani(request):
    return HttpResponse("Need to be able to delete any post made from President and VP")


# Discussion Post Page
# Only members and admin can make a post and you have to be logged in to add a post

def addDiscussion(request):
    form = DiscussionForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        DiscussionEntryModel.objects.create(topic=request.POST["topic"], date=request.POST["date"],
                                            image=request.POST["image"], entry=request.POST["entry"],
                                            video=request.POST["video"], URL_link=request.POST["URL_link"])
        return redirect("viewAllDiscussion")

    return render(request, "passionApp/addDiscussion.html", context)


def viewAllDiscussion(request):
    form = CommentForm(request.POST or None, request.FILES or None)
    discussionPosts = DiscussionEntryModel.objects.all()
    context = {
        "form": form,
        "allPosts": discussionPosts
    }
    if request.method == "POST":
        CommentEntryModel.objects.create(comment=request.POST["comment"])
        return redirect("viewAllDiscussion")
    return render(request, "passionApp/discussionBoard.html", context)


def editDiscussion(request):
    return HttpResponse("only if the user who created the post can edit it")


def deleteDiscussion(request):
    return HttpResponse("Only the created of discussion can delete discussion")


# ON EACH DISCUSSION POST , YOU CAN ADD A COMMENT UNDER IT FOR THAT SPECIFIC DISCUSSION


# upcoming events
# Admins Only can add upcoming Event


def addUpcomingEvent(request):
    print(request.POST)
    form = UpcomingEventForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        UpcomingEventsEntryModel.objects.create(event=request.POST["event"], Date=request.POST["Date"],
                                                location=request.POST["location"],
                                                eventFlyer=request.FILES["eventFlyer"])

        return redirect("viewAllUpcomingEvents")

    return render(request, "passionApp/addUpcomingEvent.html", context)

# "Only admins can edit post"
def editUpcomingEvent(request, entry_id):
    upcomingEvent = get_object_or_404(UpcomingEventsEntryModel, pk=entry_id)

    newUpcomingEvent= UpcomingEventForm(request.POST or None,request.FILES or None, instance=upcomingEvent)
    context = {
        "newUpcomingEvent": newUpcomingEvent
    }
    if newUpcomingEvent.is_valid():
        newUpcomingEvent.save()
        return redirect("viewAllUpcomingEvents")
    return render(request, "passionApp/editUpcomingEvent.html", context)

# only admins can delete post
def deleteUpcomingEvent(request, entry_id):
    upcomingEvent = get_object_or_404(UpcomingEventsEntryModel, pk=entry_id)
    context={
        "upcomingEvent":upcomingEvent
    }
    if request.method =="POST":
        upcomingEvent.delete()

        return redirect("viewAllUpcomingEvents")

    return render(request, "passionApp/deleteUpcomingEvent.html", context)


# Everyone can view upcoming events whether your are logged in  or not
def viewAllUpcomingEvents(request):
    upcomingEvents = UpcomingEventsEntryModel.objects.all()
    context = {
        "allEvents": upcomingEvents
    }
    return render(request, "passionApp/upcomingEvents.html", context)


# past events

def listAllPastEvents(request):
    return HttpResponse("Everyone can view passed events to see consistency the club has had since october 2018")


#  library page
# Only admin can add to the library of the current and passed books read, and maybe even "
# "future

def addBook(request):
    form = LibraryForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        LibraryEntryModel.objects.create(title=request.POST["title"], cover=request.FILES["cover"],
                                         link=request.POST["link"])
        return redirect("listBooks")
    return render(request, "passionApp/addBook.html", context)

# only admin and vp can edit book made
def editBook(request, entry_id):
    book = get_object_or_404(LibraryEntryModel, pk=entry_id)

    newBook = LibraryForm(request.POST or None, request.FILES or None, instance=book)
    context = {
        "newBook": newBook
    }
    if newBook.is_valid():
        newBook.save()
        return redirect("listBooks")


    return render(request, "passionApp/editBook.html", context)


def deleteBook(request):
    return HttpResponse("Only admin and VP can delete book made")

# "Everyone can view books in the library so they can see the genres and different themes, good "
# "for advertising
def listBooks(request):
    books = LibraryEntryModel.objects.all()
    context = {
        "allBooks": books
    }
    return render(request, "passionApp/library.html", context)


# photo gallery
# "All members can add photo"

def addPhoto(request):
    form = GalleryForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        GalleryEntryModel.objects.create(event=request.POST["event"], image=request.POST["image"],
                                         imageDetails=request.POST["imageDetails"], date=request.POST["date"])
        return redirect("listPhotos")
    return render(request, "passionApp/addPhoto.html", context)


def editPhoto(request):
    return HttpResponse("Whoever made post and ADMIN can edit photo")


def deletePhoto(request):
    return HttpResponse("Only whoever made post and ADMIN can delete photo")

# Only members and ADMIN can view photos
def listPhotos(request):
    photos = GalleryEntryModel.objects.all()
    context = {
        "allPhotots": photos
    }
    return render(request, "passionApp/gallery.html", context)


#  Member page ( not being implemented until everything else is complete )

def newMember(request):
    return HttpResponse("New member Form ")


def profile(request):
    return HttpResponse("Profile Page")


def allMembers(request):
    return HttpResponse("Be able to list all members of the club")
