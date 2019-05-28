from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('newMember/', views.newMember, name='newMember'),

    path('allMembers/', views.allMembers, name='allMembers'),

    path('profile/', views.profile, name='profile'),

    path('addArticle/', views.addArticle, name='addArticle'),
    path('viewAllArticles/', views.viewAllArticles, name='viewArticles'),

    path('addDiscussionPost/', views.addDiscussionPost, name='addDiscussionPost'),
    path('viewAllDiscussionPost/', views.viewAllDiscussionPost, name='viewAllDiscussionPost'),



    path('addUpcomingEvent/', views.addUpcomingEvent, name='addUpcomingEvent'),
    path('viewAllUpcomingEvents/', views.viewAllUpcomingEvents, name='viewAllUpcomingEvents'),

    path('addBook', views.addBook, name='addBook'),
    path('listBooks', views.listBooks, name='listBooks'),

    path('addPhoto', views.addPhoto, name='addPhoto'),
    path('listPhotos', views.listPhotos, name='listPhotos'),









]