from django.contrib import admin
from .models import User, Category, Genre, Title, Review


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'role')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category')
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'score', 'pub_date', 'text',)
    list_filter = ('id',)
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
