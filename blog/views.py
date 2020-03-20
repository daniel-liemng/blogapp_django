from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': "Blog Post 1",
        'content': 'First Post Content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': "Blog Post 2",
        'content': 'Second Post Content',
        'date_posted': 'August 30, 2019'
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, 'blog/home.html', context)


def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)
