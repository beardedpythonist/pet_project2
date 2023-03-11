from django.contrib import admin
from .models import *


class  WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'time_create', 'photo')
    list_display_link = ('title', 'id', 'photo')
    search_fields = ('title', 'id', 'time_create')
    list_filter = ('title', )
    prepopulated_fields = {"slug": ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_link =  ('id', 'name')
    prepopulated_fields = {"slug":('name',)}


@admin.register(Comments)
class Role(admin.ModelAdmin):
    list_display = ('author', 'text')
    search_fields = ('author', 'text')


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)



