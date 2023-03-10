from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import *
from .forms import *
from .models import *

menu = [{'title': 'На главную страницу', 'url_name': 'home'},
        {'title': ' О сайте', 'url_name': 'about'},
        {'title':'Добавить новый блог', 'url_name':'add_page'},
        {'title':'Авторизация', 'url_name':'login'},
        {'title': 'Регистрация', 'url_name': 'register'},
    ]


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
        context['menu'] = menu
        context['all'] = Women.objects.all()

        return context


class CategoryListView(DataMixin, ListView):
    model = Women
    template_name = 'women/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self):
        context = super(CategoryListView, self).get_context_data()
        context['menu'] = menu
        context['cats'] = Category.objects.all()
        return context


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/single.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cats'] = Category.objects.all()
        return context


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


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('home')

def login(request):
    return render(request, 'register.html')



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

def about(request):
    context = {'menu': menu}
    return render(request, 'women/about.html', context)

