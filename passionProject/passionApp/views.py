from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import NaniEntryModel, DiscussionEntryModel, GalleryEntryModel, CommentEntryModel, LibraryEntryModel, \
    MembershipEntryModel, UpcomingEventsEntryModel
from .forms import NaniForm, DiscussionForm, CommentForm, GalleryForm, UpcomingEventForm, LibraryForm, MembershipForm


# Create your views here.


def index(request):
    naniPost = NaniEntryModel.objects.all()
    context = {
        "allNani": naniPost
    }
    return render(request, "passionApp/index.html", context)


# Front page where all the articles Athena and I Post that are informative regarding the whole Asian World


def addNani(request):
    form = NaniForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        NaniEntryModel.objects.create(topic=request.POST["topic"], date=request.POST["date"],
                                      image=request.FILES["image"], entry=request.POST["entry"],
                                      video=request.FILES["video"], URL_link=request.POST["URL_link"])
        return redirect("index")

    return render(request, "passionApp/addNani.html", context)


# Everyone can view the info the admins post weather you are a member or not"
# def viewAllNani(request):
#     naniPost = NaniEntryModel.objects.all()
#     context = {
#         "allNani": naniPost
#     }
#     return render(request, "passionApp/index.html", context)

# Need to be able to edit any post made from the President and VP
def editNani(request, entry_id):
    nani = get_object_or_404(NaniEntryModel, pk=entry_id)

    newNani = NaniForm(request.POST or None, request.FILES or None, instance=nani)
    context = {
        "newNani": newNani
    }
    if newNani.is_valid():
        newNani.save()
        return redirect("index")
    return render(request, "passionApp/editNani.html", context)


# Need to be able to delete any post made from President and VP
def deleteNani(request, entry_id):
    nani = get_object_or_404(NaniEntryModel, pk=entry_id)
    context = {
        "nani": nani
    }
    if request.method == "POST":
        nani.delete()
        return redirect("index")

    return render(request, "passionApp/deleteNani.html", context)


# Discussion Post Page
# Only members and admin can make a post and you have to be logged in to add a post

def addDiscussion(request):
    form = DiscussionForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if request.method == "POST":
        DiscussionEntryModel.objects.create(topic=request.POST["topic"], date=request.POST["date"],
                                            image=request.FILES["image"], entry=request.POST["entry"],
                                            video=request.POST["video"], URL_link=request.POST["URL_link"])
        return redirect("viewAllDiscussion")

    return render(request, "passionApp/addDiscussion.html", context)


def viewAllDiscussion(request):
    form = CommentForm(request.POST or None, request.FILES or None)
    forms = CommentEntryModel.objects.all()
    discussionPosts = DiscussionEntryModel.objects.all()
    context = {
        "form": form,
        "allPosts": discussionPosts,
        "forms": forms
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

    newUpcomingEvent = UpcomingEventForm(request.POST or None, request.FILES or None, instance=upcomingEvent)
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
    context = {
        "upcomingEvent": upcomingEvent
    }
    if request.method == "POST":
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


# pnly admin and VP can delete book made
def deleteBook(request, entry_id):
    book = get_object_or_404(LibraryEntryModel, pk=entry_id)
    context = {
        "book": book
    }
    if request.method == "POST":
        book.delete()
        return redirect("listBooks")
    return render(request, "passionApp/deleteBook.html", context)


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
        GalleryEntryModel.objects.create(event=request.POST["event"], image=request.FILES["image"],
                                         imageDetails=request.POST["imageDetails"], date=request.POST["date"])
        return redirect("listPhotos")
    return render(request, "passionApp/addPhoto.html", context)


# Whoever made post and ADMIN can edit photo
def editPhoto(request, entry_id):
    photo = get_object_or_404(GalleryEntryModel, pk=entry_id)
    newPhoto = GalleryForm(request.POST or None, request.FILES or None, instance=photo)
    context = {
        "newPhoto": newPhoto
    }
    if newPhoto.is_valid():
        newPhoto.save()
        return redirect("listPhotos")
    return render(request, "passionApp/editPhoto.html", context)


# Only whoever made post and ADMIN can delete photo
def deletePhoto(request, entry_id):
    photo = get_object_or_404(GalleryEntryModel, pk=entry_id)
    context = {
        "photo": photo
    }
    if request.method == "POST":
        photo.delete()
        return redirect("listPhotos")
    return render(request, "passionApp/deletePhoto.html", context)


# Only members and ADMIN can view photos
def listPhotos(request):
    photos = GalleryEntryModel.objects.all()
    context = {
        "allPhotos": photos
    }
    return render(request, "passionApp/gallery.html", context)


#  Member page ( not being implemented until everything else is complete )

def newMember(request):
    return HttpResponse("New member Form ")


def profile(request):
    return HttpResponse("Profile Page")


def allMembers(request):
    return HttpResponse("Be able to list all members of the club")
