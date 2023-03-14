from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [path('', WomenHome.as_view(), name='home'),
               path('index/', WomenHome.as_view(), name='home'),
               path('register/', RegisterView.as_view(), name='register'),
               path('login/', SignInView.as_view(), name='login'),
               path('logout/', LogoutView.as_view(), name='logout'),
               path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
               path('cats/<slug:cat_slug>/', CategoryListView.as_view(), name='category'),
                path('about/', about, name='about'),
               path('search/', Search.as_view(), name='search')
               ]