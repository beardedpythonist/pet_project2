from django.shortcuts import *
from django.urls import reverse_lazy
from django.views.generic import *
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import *
from django.contrib.auth.models import User
from django.contrib.auth.views import *

from .utils import *
from .forms import *
from .models import *

menu = [
    {'title': 'Выйти', 'url_name': 'logout'},
    {'title': 'На главную страницу', 'url_name': 'home'},
    {'title': 'О создателе сайта', 'url_name': 'about'},
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Регистрация', 'url_name': 'register'},
]


class WomenHome(DataMixin, ListView):
    paginate_by = 4
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
    paginate_by = 4
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


class ShowPost(DataMixin, FormMixin, DetailView):
    model = Women
    template_name = 'women/single.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'post_slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cats'] = Category.objects.all()
        return context


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'women/login.html'


def add_page(request):
    pass


def about(request):
    context = {'menu': menu}
    return render(request, 'women/about.html', context)


# класс сеарч не раотает!!!
class Search(ListView):
    paginate_by = 4
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Women.objects.filter(content__iregex=self.request.GET.get('q'))
