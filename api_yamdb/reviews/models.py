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
