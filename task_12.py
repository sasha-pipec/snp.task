class JellyBean:

    def __init__(self, flavor=''):
        self.flavor = flavor

    def setFlavor(self, flavor):
        self.flavor = flavor

    def getFlavor(self):
        return self.flavor


class Dessert(JellyBean):

    def __init__(self, name='',calories=0):
        self.name = name
        self.calories = calories
        super().__init__()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCalories(self, calories):
        self.calories = calories

    def getCalories(self):
        return self.calories

    def is_healthy(self):
        if type(self.calories) == int or float:
            if self.calories < 200:
                return True
            else:
                return False
        else:
            return False

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
        else:
            return True


pt = Dessert()
pt.calories=201.2
pt.flavor="black licorice"
print(pt.is_healthy())
print(pt.flavor)
print(pt.is_delicious())