from django.urls import path
from .views import *


urlpatterns = [path('', WomenHome.as_view(), name='home'),
               path('register.html', RegisterUSer.as_view(), name='register'),
               path('login/', login, name='login'),
               path('single-post.html', AddPage.as_view(), name='add_page'),
               path('contact/', contact, name='contact'),
               path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
               path('search-result.html', search, name='search'),
               path('cats/<slug:cat_slug>/', Category.as_view(), name='category'),
               ]