from django.urls import path
from .views import *




urlpatterns = [path('', WomenHome.as_view(), name='home'),
               path('index/', WomenHome.as_view(), name='home'),
               path('register/', RegisterView.as_view(), name='signup'),
               path('login/', login, name='login'),
               path('addpage/', AddPage.as_view(), name='add_page'),
               path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
               path('search-result/', search, name='search'),
               path('cats/<slug:cat_slug>/', CategoryListView.as_view(), name='category'),
                path('about/', about, name='about') ,
               ]