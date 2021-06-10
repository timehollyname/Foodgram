from django.db.models import Exists, OuterRef, QuerySet


class RecipeQuerySet(QuerySet):
    def get_by_tags(self, get):
        tags = get.getlist('tags')
        return self.filter(tags__id__in=tags) if tags else self

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

    def get_var_is_subscribed(self, user):
        if user.is_authenticated:
            return self.annotate(
                is_subscribed=Exists(
                    user.subscriptions.filter(
                        author__id=OuterRef('author__id')
                    )
                )
            )
        return self
