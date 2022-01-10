class Dessert:

    def __init__(self, name='', calories=0):
        self._name = name
        self._calories = calories

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
        return True


pt = Dessert('cake', 201)
print(pt.is_healthy(), pt.is_delicious())
