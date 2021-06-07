from django.db.models import Exists, OuterRef, QuerySet


class RecipeQuerySet(QuerySet):
    def get_by_tags(self, tags):
        return self.filter(tags__id__in=tags)

    def get_var_is_favorite(self, user):
        return self.annotate(
            is_favorite=Exists(
                user.favorites.filter(
                    recipe__id=OuterRef('id')
                )
            )
        )
