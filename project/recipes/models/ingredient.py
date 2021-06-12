from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=128,
        db_index=True,
        unique=True
    )
    dimension = models.CharField(
        verbose_name='Единица измерения',
        max_length=16
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.dimension}'
