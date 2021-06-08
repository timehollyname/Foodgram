from django.conf import settings


class Purchases(object):
    __session = None
    __session_id = settings.PURCHASES_SESSION_ID
    __recipes = None

    def __init__(self, request):
        self.__session = request.session
        self.__recipes = self.__session.get(self.__session_id, [])

    @property
    def recipes(self):
        return self.__recipes

    def exists(self, pk):
        return pk in self.recipes

    def count(self):
        return len(self.recipes)

    def add(self, pk):
        if not self.exists(pk):
            self.__recipes.append(pk)
            self.__save()

    def remove(self, pk):
        if self.exists(pk):
            self.__recipes.remove(pk)
            self.__save()

    def __save(self):
        self.__session[self.__session_id] = self.__recipes
        self.__session.modified = True
