from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import NaniEntryModel, DiscussionEntryModel, GalleryEntryModel, CommentEntryModel, LibraryEntryModel, \
    MembershipEntryModel
from .forms import NaniForm, DiscussionForm, CommentForm, GalleryForm, UpcomingEventForm, LibraryForm, MembershipForm


# Create your views here.


def index(request):
    return HttpResponse("Testing server")


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

def addDiscussion(request):
    form = DiscussionForm(request.POST or None, request.FILES or None)

    return HttpResponse("Only members and admin can make a post and you have to be logged in to add a post")


def viewAllDiscussion(request):
    return HttpResponse("Only Members loggeed in can view discussion board")


def editDiscussion(request):
    return HttpResponse("only if the user who created the post can edit it")


def deleteDiscussion(request):
    return HttpResponse("Only the created of discussion can delete discussion")


# ON EACH DISCUSSION POST , YOU CAN ADD A COMMENT UNDER IT FOR THAT SPECIFIC DISCUSSION

def addComment(request):
    return HttpResponse("Members are able to add a single comment on the discussion post.")


# upcoming events


def addUpcomingEvent(request):
    return HttpResponse("Admins Only can add upcoming Event")


def editUpcomingEvent(request):
    return HttpResponse("Only admins can edit post")


def deleteUpcomingEvent(request):
    return HttpResponse("only admins can delete post")


def viewAllUpcomingEvents(request):
    return HttpResponse("Everyone can view upcoming events whether your are logged in  or not")


# past events

def listAllPastEvents(request):
    return HttpResponse("Everyone can view passed events to see consistency the club has had since october 2018")


# library page

def addBook(request):
    return HttpResponse("Only admin can add to the library of the current and passed books read, and maybe even "
                        "future")


def editBook(request):
    return HttpResponse("only admin and vp can edit book made ")


def deleteBook(request):
    return HttpResponse("Only admin and VP can delete book made")


def listBooks(request):
    return HttpResponse("Everyone can view books in the library so they can see the genres and different themes, good "
                        "for advertising")


# photo gallery

def addPhoto(request):
    return HttpResponse("All members can add photo")


def editPhoto(request):
    return HttpResponse("Whoever made post and ADMIN can edit photo")


def deletePhoto(request):
    return HttpResponse("Only whoever made post and ADMIN can delete photo")


def listPhotos(request):
    return HttpResponse("Only members and ADMIN can view photos")


#  Member page ( not being implemented until everything else is complete )

def newMember(request):
    return HttpResponse("New member Form ")


def profile(request):
    return HttpResponse("Profile Page")


def allMembers(request):
    return HttpResponse("Be able to list all members of the club")
