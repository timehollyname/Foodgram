from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name=_('Наименование'),
        max_length=128,
        db_index=True,
        unique=True
    )
    dimension = models.CharField(
        verbose_name=_('Единица измерения'),
        max_length=16
    )

    class Meta:
        verbose_name = _('Ингредиент')
        verbose_name_plural = _('Ингредиенты')

    def __str__(self):
        return f'{self.name}, {self.dimension}'
