from re import template
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    contex = {
        'title': title,
    }
    return render(request, template, contex)
    
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
    # return HttpResponse ('втоорая страница')
