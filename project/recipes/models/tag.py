from colorfield.fields import ColorField
from django.db import models


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=64,
        unique=True
    )
    color = ColorField(
        verbose_name='Цвет текста',
        format='hexa'
    )
    background = ColorField(
        verbose_name='Цвет фона',
        format='hexa'
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
