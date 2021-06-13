from django.conf import settings


class Purchase:
    __session = None
    __session_id = settings.PURCHASES_SESSION_ID
    __recipes = None

    def __init__(self, request):
        self.__session = request.session
        self.__recipes = self.__session.get(self.__session_id, [])

    @property
    def recipes(self):
        return self.__recipes

    def exists(self, id):
        return id in self.recipes

    def count(self):
        return len(self.recipes)

    def add(self, id):
        if not self.exists(id):
            self.__recipes.append(id)
            self.__save()

    def remove(self, id):
        if self.exists(id):
            self.__recipes.remove(id)
            self.__save()

    def __save(self):
        self.__session[self.__session_id] = self.__recipes
        self.__session.modified = True
