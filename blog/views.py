from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# How we want to handle server routes
posts =[
    {
        'author': 'Aarya',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                   'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris '
                   'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate '
                   'velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non '
                   'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted': '4 January, 2024'
    },
    {
        'author': 'User12',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                   'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris '
                   'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate '
                   'velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non '
                   'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted': '2 January, 2024',

    },
    {
        'author': 'Jamwal',
        'title': 'Blog post 3',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                   'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris '
                   'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate '
                   'velit esse cillum dolore eu fugiat nulla paginator. Excepteur sint occaecat cupidatat non '
                   'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted': '1 January, 2024',

    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

