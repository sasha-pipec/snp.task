class JellyBean:

    def __init__(self, flavor):
        self._flavor = flavor

    def setFlavor(self, flavor):
        self._flavor = flavor

    def getFlavor(self):
        return self._flavor


class Dessert(JellyBean):

    def __init__(self, name,calories):
        self._name = name
        self._calories = calories
        super().__init__()

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setCalories(self, calories):
        self._calories = calories

    def getCalories(self):
        return self._calories

    def is_healthy(self):
        if type(self._calories) == int:
            if self._calories < 200:
                return True
            else:
                return False
        else:
            return False

    def is_delicious(self):
        if self.getFlavor() == "black licorice":
            return False
        else:
            return True


pt = Dessert('cake', 199)
print(pt.is_delicious())
pt.setFlavor('black licorice')
print(pt.is_delicious(), pt.is_healthy())
