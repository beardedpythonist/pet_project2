from django.urls import path
from .views import *


urlpatterns = [path('', WomenHome.as_view(), name='home'),
               path('register.html', RegisterUSer.as_view(), name='register'),
               path('login/', login, name='login'),
               path('addpage.html', add_page, name='add_page'),
               path('contact/', contact, name='contact'),
               path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
               path('search-result.html', search, name='search'),
               path('cats/<slug:cat_slug>/', CategoryListView.as_view(), name='category'),
               ]