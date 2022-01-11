class Dessert:

    def __init__(self, name='', calories=''):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        if type(self.calories) == str:
            return False
        else:
            if self.calories < 200:
                return True
            else:
                return False

    def is_delicious(self):
        return True


pt = Dessert()
pt.calories = 200
print(pt.is_healthy())