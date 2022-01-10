class Dessert:

    def __init__(self, name='', calories=0):
        self.name = name
        self.calories = calories

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCalories(self, calories):
        self.calories = calories

    def getCalories(self):
        return self.calories

    def is_healthy(self):
        if type(self.calories) == int:
            if self.calories < 200:
                return True
            else:
                return False
        else:
            return False

    def is_delicious(self):
        return True


pt = Dessert('cake', 201)
print(pt.is_healthy(), pt.is_delicious())
