from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path("",views.home,name='home'),
    path("logout/",views.logout_user,name='logout'),
    path("signup/",views.signup_user,name='signup'),
    path("list_songs/<album_name>",views.list_songs,name='list_songs'),
    path("play_songs/<title>",views.play_songs,name='play_songs'),
    path("search/",views.search,name='search'),
]