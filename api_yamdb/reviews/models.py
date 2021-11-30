from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.SlugField(
        'Имя пользователя', max_length=150, blank=False, unique=True)
    email = models.EmailField('Эл. почта', blank=False)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    # role = models.TextField()

    def __str__(self):
        return self.username


class Category(models.Model):  # id, name, slug
    name = models.CharField('Название категории', max_length=200)
    slug = models.SlugField('Идентификатор категории', unique=True)

    def __str__(self):
        return self.name[:15]


class Genre(models.Model):  # id, name, slug
    name = models.CharField('Название жанра', max_length=200)
    slug = models.SlugField('Идентификатор жанра', unique=True)

    def __str__(self):
        return self.name[:15]


class Title(models.Model):  # id,name,year,category
    name = models.TextField('Название')
    year = models.CharField('Год произведения', max_length=4)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,

    )

    def __str__(self):
        return self.name[:15]
