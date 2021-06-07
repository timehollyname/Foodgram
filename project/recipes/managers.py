from django.db.models import Manager

from .querysets import RecipeQuerySet


class RecipeManager(Manager):
    def get_queryset(self):
        return RecipeQuerySet(self.model, using=self._db)

    def get_by_tags(self, tags):
        return self.get_queryset().get_by_tags(tags)

    def get_var_is_favorite(self, user):
        return self.get_queryset().get_var_is_favorite(user)
