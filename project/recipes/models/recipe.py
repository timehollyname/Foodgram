from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .ingredient import Ingredient
from .tag import Tag

User = get_user_model()


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name=_('Автор'),
        related_name='recipes',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name=_('Наименование'),
        max_length=128
    )
    description = models.TextField(
        verbose_name=_('Текстовое описание'),
        max_length=2048
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name=_('Ингредиент(ы)'),
        through='RecipeIngredient',
        related_name='recipes'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name=_('Время приготовления в минутах'),
        validators=(MinValueValidator(1), MaxValueValidator(1440),)
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_('Тег(и)'),
        related_name='recipes'
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата создания'),
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = _('Рецепт')
        verbose_name_plural = _('Рецепты')
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'pk': self.pk}
        return reverse('recipes:recipe', kwargs=kwargs)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name=_('Рецепт'),
        related_name='recipe_ingredients',
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name=_('Ингредиент'),
        related_name='recipes_using_the_ingredient',
        on_delete=models.CASCADE
    )
    quantity = models.DecimalField(
        verbose_name=_('Количество'),
        max_digits=6,
        decimal_places=1
    )

    class Meta:
        verbose_name = _('Ингредиент рецепта')
        verbose_name_plural = _('Ингредиенты рецепта')

        constraints = (
            models.UniqueConstraint(
                fields=('recipe', 'ingredient'),
                name='unique_recipe_ingredient'
            ),
        )

    def __str__(self):
        return (
            f'Рецепт: {self.recipe}. '
            f'Ингредиент: {self.ingredient}. '
            f'Количество: {self.quantity}'
        )
