class Dessert:

    def __init__(self, name='', calories=''):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        if (type(self.calories) == int or type(self.calories) == float) and self.calories < 200:
            return True
        return False

    def is_delicious(self):
        return True


pt = Dessert()
pt.calories = 200
print(pt.is_healthy())