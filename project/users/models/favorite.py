from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from recipes.models import Recipe  # noqa

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('Пользователь'),
        related_name='favorites',
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name=_('Рецепт'),
        related_name='favorites',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата создания'),
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = _('Избранный рецепт')
        verbose_name_plural = _('Избранные рецепты')
        ordering = ('-created_at',)

        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_favorite'
            ),
        )

    def __str__(self):
        return (
            f'Пользователь: {self.user}, '
            f'добавил в избранные рецепт: {self.recipe}'
        )
