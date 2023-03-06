
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import *
from .forms import *
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'добавить статью', 'url_name': 'add_page'},
        {'title': 'обратная связь', 'url_name': 'contact'},
        {'title': 'войти', 'url_name': 'login'}]


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class Category(DataMixin, ListView):
    model = Category
    template_name = 'women/category.html'
    context_object_name = 'cats'

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound(' <h1> страница не найдена  </h1>')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def login(request):
#     return render(request, 'women/register.html')

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


# def add_page(request):
#     if request.method == "POST":
#         form =AddPostForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             try:
#                 Women.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, "Ошибка")
#         # else:
#         #     # form =AddPostForm()
#
#     form = AddPostForm()
#     return render(request, 'women/addpage.html', {'menu': menu, 'form': form, 'title': 'добавить статью'})


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


