from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from ..managers import RecipeManager
from .ingredient import Ingredient
from .tag import Tag

User = get_user_model()


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='recipes',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Наименование',
        max_length=128
    )
    description = models.TextField(
        verbose_name='Текстовое описание',
        max_length=2048
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиент(ы)',
        through='RecipeIngredient',
        related_name='recipes'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        validators=(MinValueValidator(1), MaxValueValidator(1440),)
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег(и)',
        related_name='recipes'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='recipes/'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        db_index=True
    )

    objects = RecipeManager()

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {'pk': self.pk}
        return reverse('recipes:recipe', kwargs=kwargs)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        related_name='recipe_ingredients',
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='Ингредиент',
        related_name='recipes_using_the_ingredient',
        on_delete=models.CASCADE
    )
    quantity = models.DecimalField(
        verbose_name='Количество',
        max_digits=6,
        decimal_places=1
    )

    class Meta:
        verbose_name = 'Ингредиент рецепта'
        verbose_name_plural = 'Ингредиенты рецепта'

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
