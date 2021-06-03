from recipes.models import Tag  # type: ignore
from rest_framework.serializers import ModelSerializer


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
