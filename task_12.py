class Dessert:

    def __init__(self, name='', calories=''):
        self.name = name
        self.calories = calories
        super().__init__()

    def is_healthy(self):
        if type(self.calories) == str:
            return False
        else:
            if self.calories < 200:
                return True
            else:
                return False

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
        else:
            return True


class JellyBean(Dessert):

    def __init__(self, flavor=''):
        self.flavor = flavor
        super().__init__()


pt = JellyBean()
pt.calories=201
pt.calories=111
pt.flavor="black licorice"
pt.flavor='a'
pt.name='test'
pt.name='test1'
print(pt.is_healthy())
print(pt.is_delicious())
print(pt.name)