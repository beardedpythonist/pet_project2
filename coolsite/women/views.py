from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddPostForm
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'добавить статью', 'url_name': 'add_page'},
        {'title': 'обратная связь', 'url_name': 'contact'},
        {'title': 'войти', 'url_name': 'login'}]

def index11(request):
    post = Women.objects.all()
    cats = Category.objects.all()
    context = {'post': post,
               'menu': menu,
               'cats': cats,
               'title5': 'Главная страница))))))',
               'cat_selected':0}
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu})


def addpage(request):
    form = AddPostForm()
    return render(request, 'women/single-post.html', {'menu': menu, 'form': form, 'title': 'добавить статью'})

def contact(request):
    return render(request, 'women/contact.html')

def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_id):
    post = Women.objects.filter(cat=cat_id)
    cats = Category.objects.all()
    if len(post) == 0:
        raise Http404()

    context = {'post': post,
               'menu': menu,
               'cats': cats,
               'title5': 'отображение по рубрикам',
               'cat_selected': cat_id}
    return render(request, 'women/index.html', context=context)




def show_post(request, post_slug):
        post = get_object_or_404(Women, slug=post_slug)
        cats = Category.objects.all()
        context = {'post': post,
                   'menu': menu,
                   'cats': cats,
                   'title5': post.title,
                   'cat_selected': post.cat_id}
        return render(request, 'women/post.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(' <h1> страница не найдена  </h1>')