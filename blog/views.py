from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()

    context = {"posts": posts}

    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post

    # <app>/<model>_<viewtype>.html
    # blog/post_view.html
    template_name = 'blog/home.html'

    context_object_name = 'posts'

    ordering = ['-date_posted']


def about(request):
    context = {'title': 'About'}

    return render(request, 'blog/about.html', context)
