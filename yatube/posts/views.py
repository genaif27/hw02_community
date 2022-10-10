from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    latest_posts = Post.objects.order_by("-pub_date")[:12]
    context = {
        'posts': latest_posts,
    }
    return render(request, template, context)


def group_list(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
