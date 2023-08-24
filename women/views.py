from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *

def index(request):
    posts = Women.objects.all()
    
    
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    
    return render(request, 'women/addpage.html', {'form': form, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)   
    
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    
    return render(request, 'women/post.html', context=context)

def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug=cat_slug)
    
    if len(posts) == 0:
        raise Http404
    
    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_slug,
    }
    
    return render(request, 'women/index.html', context=context)