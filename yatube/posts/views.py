# posts/views.py
from django.shortcuts import get_object_or_404, render
# Импортируем модель, чтобы обратиться к ней
from .models import Group, Post

def index(request):
    title = 'Это главная страница проекта Yatube'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request,slug):
    group = get_object_or_404(Group, slug=slug)
    title = "Здесь будет информация о группах проекта Yatube"
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)

# Create your views here.
