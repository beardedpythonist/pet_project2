from django.urls import path
from .views import *

urlpatterns = [path('', index11, name='home'),
               path('about/', about, name='about'),
               path('single-post.html', addpage, name='add_page'),
               path('contact/', contact, name='contact'),
               path('login/', login, name='login'),
               path('post/<slug:post_slug>/', show_post, name='post'),
               path('cats/<int:cat_id>/', show_category, name='category')
               ]