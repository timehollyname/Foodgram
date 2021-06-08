from django.db.models import Exists, OuterRef, QuerySet


class RecipeQuerySet(QuerySet):
    def get_by_tags(self, get):
        if 'tags' in get:
            return self.filter(tags__id__in=get.getlist('tags'))
        return self

    def get_var_is_favorite(self, user):
        if user.is_authenticated:
            return self.annotate(
                is_favorite=Exists(
                    user.favorites.filter(
                        recipe__id=OuterRef('id')
                    )
                )
            )
        return self
