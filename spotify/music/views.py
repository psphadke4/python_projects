from django.shortcuts import render,redirect
from django.contrib.auth import  login,logout,authenticate
from django.contrib import messages
from .models import Songs
from .forms import create_user

def home(request):
    playlist=Songs.objects.all()
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged In")
            return redirect('home')
        else:
            messages.warning(request, "Please login to Hear Songs")
            return redirect('home')
    else:
        return render(request, template_name='music/home.html',context={'playlist':playlist})

def logout_user(request):
    logout(request)
    messages.success(request, "You are logged Out")
    return redirect('home')


def signup_user(request):
    if request.method == "POST":
        form = create_user(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'{user} is Registered Successfull')
            return redirect('home')
    else:
        form = create_user
        return render(request, template_name='music/signup.html', context={'form': form})
    return render(request, template_name='music/home.html', context={'form': form})

def list_songs(request,album_name):
    playlist_album = Songs.objects.filter(album_name=album_name)
    return render(request, template_name='music/Songs_list.html', context={'playlist_album': playlist_album})

def play_songs(request,title):
    if user.is_authenticated:
        playlist_title = Songs.objects.filter(title=title).get()
        return render(request, template_name='music/Songs_list.html', context={'playlist_title': playlist_title})
    else:
        messages.warning(request,f"Please login before playing songs")
        redirect('home')


def search(request):
    if request.method == "POST":
        searched=request.POST["search_query"]
        if searched != "":
            posts=Songs.objects.filter(title__icontains=searched)
            if posts.count() == 0 :
                messages.warning(request, f"No such songs in List , Please search for relevant songs")
                return  render(request,template_name='music/Songs_list.html',context={'searched':searched,'posts':posts})
            else:
                return  render(request,template_name='music/Songs_list.html',context={'searched':searched,'posts':posts})
        else:
            messages.warning(request,f"Please Search for Song")
            return redirect('home')

    else:
        return redirect('home')