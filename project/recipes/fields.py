from django.forms import MultipleChoiceField


class ListWithoutValidationField(MultipleChoiceField):
    def valid_value(self, *args, **kwargs):
        return True
