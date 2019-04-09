from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


# class UserInfo(models.Model):
#     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
#     avatar = models.ImageField(blank=True, null=True)
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(blank=True, null=True)
    subscribers = models.ManyToManyField('self')


class Recipe(models.Model):
    title = models.CharField(_('Название'), max_length=100)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL,
        verbose_name= _('Автор')
    )
    level = models.PositiveSmallIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.title}'

    def get_absolute_url(self):
        return reverse('recipe', args=(self.pk, ))

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-created_at',)
        # unique_together = (
        #     ('title', 'author'),
        # )
        # index_together = (
        #     ('title', 'author'),
        # )


class Comment(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey('cooking.Recipe', on_delete=models.CASCADE)


class BaseReaction(models.Model):
    STATUSES = (
        ('like', 'Like'),
        ('dislike', 'Dislike')
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=10, choices=STATUSES)

    class Meta:
        abstract = True


class RecipeReaction(BaseReaction):
    recipe = models.ForeignKey('cooking.Recipe', on_delete=models.CASCADE)


class CommentReaction(BaseReaction):
    comment = models.ForeignKey('cooking.Comment', on_delete=models.CASCADE)


class Repost(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True, null=True)
