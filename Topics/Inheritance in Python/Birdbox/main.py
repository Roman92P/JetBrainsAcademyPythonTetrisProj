# create your classes here
class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    pass


class Pigeon(Bird):
    pass


class Sparrow(Bird):
    pass


sparrow = Sparrow('ASASD')
