from django.urls import path
from .views import *

urlpatterns = [path('', WomenHome.as_view(), name='home'),
               path('about.html/', about, name='about'),
               path('single-post.html', add_page, name='add_page'),
               path('contact/', contact, name='contact'),
               path('login/', login, name='login'),
               path('post/<slug:post_slug>/', show_post, name='post'),
               path('search-result.html', search, name= 'search'),
               path('cats/<slug:cat_slug>/', Category.as_view(), name='category')
               ]