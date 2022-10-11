from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):

    post = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': post,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
