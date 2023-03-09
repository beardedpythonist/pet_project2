from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import *
from .forms import *
from .models import *


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_act'] = Women.objects.filter(cat__pk=1).order_by("-id")[0:5]
        context['last_sport'] = Women.objects.filter(cat__pk=2).order_by("-id")[0:5]
        context['last_sing'] = Women.objects.filter(cat__pk=3).order_by("-id")[0:5]
        context['last_mode'] = Women.objects.filter(cat__pk=3).order_by("-id")[0:5]
        context['last_all'] = Women.objects.filter().order_by("-id")[0:5]
        context['cats'] = Category.objects.all()
        return context


class CategoryListView(DataMixin, ListView):
    template_name = 'women/category.html'
    context_object_name = 'posts'


    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/single.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     return Women.objects.filter(slug__slug=self.kwargs['post_slug'])
    #

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True




def contact(request):
    return render(request, 'women/contact.html')


def search(request):
    return render(request, 'women/search-result.html')


class RegisterUSer(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def login(request):
    return render(request, 'register.html')


#


# def show_category(request, cat_id):
#     post = Women.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#     if len(post) == 0:
#         raise Http404()
#
#     context = {'post': post,
#                'menu': menu,
#                'cats': cats,
#                'title5': 'отображение по рубрикам',
#                'cat_selected': cat_id}
#
#     return render(request, 'women/category.html', context=context)
# def create(request):
#     error = ''
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Error'
#     form = TaskForm()
#
#     context ={'form': form, 'error': error}
#     return render(request, 'main/create.html', context)

def add_page(request):
    global  context1
    post = Women.objects.all()
    if request.method == "POST":
        form = AddPostForm(request.POST)


        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, "Ошибка")
    else:
        form = AddPostForm()
        context1 = {'form': form, 'post': post}
    return render(request, 'women/addpage.html', context1)

# def show_post(request, post_slug):
#         post = get_object_or_404(Women, slug=post_slug)
#         cats = Category.objects.all()
#         context = {'post': post,
#                    'menu': menu,
#                    'cats': cats,
#                    'title5': post.title,
#                    'cat_selected': post.cat_id}
#         return render(request, 'women/single-post.html', context)
#

# def index11(request):
#     post = Women.objects.all()
#     cats = Category.objects.all()
#     context = {'post': post,
#                'menu': menu,
#                'cats': cats,
#                'title5': 'Главная страница))))))',
#                'cat_selected': 0,}
#
#     return render(request, 'women/index.html', context=context)
