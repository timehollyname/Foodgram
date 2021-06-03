from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('Пользователь'),
        related_name='subscriptions',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        verbose_name=_('Автор'),
        related_name='subscribers',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата создания'),
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = _('Подписка')
        verbose_name_plural = _('Подписки')
        ordering = ('-created_at',)

        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscription'
            ),
        )

    def __str__(self):
        return (
            f'Пользователь: {self.user}, '
            f'подписан на пользователя: {self.author}'
        )
