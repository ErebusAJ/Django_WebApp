from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# How we want to handle server routes
posts =[
    {
        'author': 'Aarya',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '4 January, 2024'
    },
    {
        'author': 'User12',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '2 January, 2024'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

