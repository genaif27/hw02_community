from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
    
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    # template = 'posts/index.html'
    # title = 'Это главная страница проекта Yatube'
    # context = {
    #     'title':title
    # } 
    # return render(request, template, context) 
    
    # posts = Post.objects.order_by('-pub_date')[:10]
    # # В словаре context отправляем информацию в шаблон
    # context = {
    #     'posts': posts,
    # }
    # return HttpResponse (
    #     'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
    #     'если у тебя нет правильных <s>вопросов</s> запросов.'
    # )

def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list', context)
    # return HttpResponse ('втоорая страница')
