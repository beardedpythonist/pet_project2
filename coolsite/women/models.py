from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Women(models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique= True, db_index= True, verbose_name= "URL")
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, )

    class Meta:
        verbose_name_plural = 'Известные женщины'
        ordering = ('cat', 'title')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})



class Comments(models.Model):
    article = models.ForeignKey(Women, on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True,
                                related_name='comments_articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)

