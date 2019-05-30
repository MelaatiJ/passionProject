from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # add member
    path('newMember/', views.newMember, name='newMember'),
    path('allMembers/', views.allMembers, name='allMembers'),
    path('profile/', views.profile, name='profile'),


    # whats new page
    path('addNani/', views.addNani, name='addNani'),
    path('viewAllNani/', views.viewAllNani, name='viewAllNani'),
    path('editNani/', views.editNani, name='editNani'),
    path('deleteNani/', views.deleteNani, name='deleteNani'),


    # Discussion page
    path('addDiscussion/', views.addDiscussion, name='addDiscussion'),
    path('viewAllDiscussion/', views.viewAllDiscussion, name='viewAllDiscussion'),
    path('editDiscussion/', views.editDiscussion, name='editDiscussion'),
    path('deleteDiscussion/', views.deleteDiscussion, name='deleteDiscussion'),


    # ON EACH DISCUSSION POST , YOU CAN ADD A COMMENT UNDER IT FOR THAT SPECIFIC DISCUSSION
    # path('addComment/', views.addComment, name='addComment'),


    # events page
    path('addUpcomingEvent/', views.addUpcomingEvent, name='addUpcomingEvent'),
    path('editUpcomingEvent/', views.editUpcomingEvent, name='editUpcomingEvent'),
    path('deleteUpcomingEvent/', views.deleteUpcomingEvent, name='deleteUpcomingEvent'),
    path('viewAllUpcomingEvents/', views.viewAllUpcomingEvents, name='viewAllUpcomingEvents'),
    path('listAllPastEvents/', views.listAllPastEvents, name='listAllPastEvents'),

    # library page
    path('addBook/', views.addBook, name='addBook'),
    path('editBook/', views.editBook, name='editBook'),
    path('deleteBook/', views.deleteBook, name='deleteBook'),
    path('listBooks/', views.listBooks, name='listBooks'),

    # Gallery Page
    path('addPhoto/', views.addPhoto, name='addPhoto'),
    path('editPhoto/', views.editPhoto, name='editPhoto'),
    path('deletePhoto/', views.deletePhoto, name='deletePhoto'),
    path('listPhotos/', views.listPhotos, name='listPhotos'),

]