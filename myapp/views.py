from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html')


def page(request):
    # data = Page.objects.all()
    data = Page.objects.filter(user__email='arsalan@gmail.com')
    return render(request, 'page.html', {'data': data})


def user(request):
    # data = User.objects.all()
    # data = User.objects.filter(email='ibad@gmail.com')
    # data = User.objects.filter(mypage__category='page2')
    # data = User.objects.filter(mypost__date='2022-1-10')
    data = User.objects.filter(song__duration=5)

    return render(request, 'user.html', {'data': data})


def post(request):
    data = Post.objects.all()
    return render(request, 'post.html', {'data': data})


def song(request):
    # data = Song.objects.all()
    data = Song.objects.filter(user__username='irshad')

    return render(request, 'song.html', {'data': data})
