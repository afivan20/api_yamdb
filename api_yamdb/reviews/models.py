from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.SlugField(
        'Имя пользователя',
        max_length=150,
        blank=False,
        unique=True
    )
    email = models.EmailField('Эл. почта', blank=False, unique=True)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    USER_ROLES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]
    role = models.CharField(
        max_length=150,
        blank=False,
        choices=USER_ROLES,
        default='user',
    )
    confirmation_code = models.CharField(
        max_length=200,
    )

    @property
    def is_admin(self):
        if self.role == 'admin' or self.is_superuser:
            return True

    @property
    def is_moderator(self):
        if self.role == 'moderator' or self.is_superuser:
            return True

    def __str__(self):
        return self.username

    class Meta:
        ordering = (
            'username',
        )


class Category(models.Model):
    name = models.CharField('Название категории', max_length=200)
    slug = models.SlugField('Идентификатор категории', unique=True)

    def __str__(self):
        return self.name[:15]


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=200)
    slug = models.SlugField('Идентификатор жанра', unique=True)

    def __str__(self):
        return self.name[:15]


class Title(models.Model):
    name = models.CharField('Название', max_length=200)
    year = models.IntegerField('Год произведения')
    description = models.TextField('Описание', blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles'
    )
    genre = models.ManyToManyField(Genre, through='GenreTitle')

    def __str__(self):
        return self.name[:15]


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title.name} {self.genre.name}'


class Review(models.Model):
    SCORES = (
        (1, 1), (2, 2), (3, 3), (4, 4),
        (5, 5), (6, 6), (7, 7), (8, 8),
        (9, 9), (10, 10))
    text = models.TextField('Описание', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField('Оценка', choices=SCORES)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    title = models.ForeignKey(
        Title, related_name='reviews', on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField('Описание', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    review = models.ForeignKey(
        Review, related_name='comments', on_delete=models.CASCADE)
