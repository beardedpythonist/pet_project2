from django.urls import path
from .views import *


urlpatterns = [path('', WomenHome.as_view(), name='home'),
               path('index.html', WomenHome.as_view(), name='home'),
               path('register.html', RegisterView.as_view(), name='register'),
               path('login/', login, name='login'),
               path('addpage.html', add_page, name='add_page'),
               path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
               path('search-result.html', search, name='search'),
               path('cats/<slug:cat_slug>/', CategoryListView.as_view(), name='category'),
               ]