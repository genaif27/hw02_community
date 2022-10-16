from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    # start_date=datetime.date(1854.7.7)
    # end_date=datetime.date(1854.7.21)
    # keyword = "утро"
    # post= Post.objects.filter(text__contains=keyword).filter(autho=leo).filter(pub_date__range=start_date, end_date)

    post = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': post,
    }
    return render(request, 'posts/index.html', context)



def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
