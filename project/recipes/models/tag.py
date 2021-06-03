from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
    name = models.CharField(
        verbose_name=_('Наименование'),
        max_length=64,
        unique=True
    )
    color = ColorField(
        verbose_name=_('Цвет текста'),
        format='hexa'
    )
    background = ColorField(
        verbose_name=_('Цвет фона'),
        format='hexa'
    )

    class Meta:
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')

    def __str__(self):
        return self.name
