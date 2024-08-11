class Bird():
    def __init__(self, feathers, beak_shape, can_fly=True):
        self.feathers = feathers
        self.beak_shape = beak_shape
        self.can_fly = can_fly

Chicken = Bird("brown", "small", False);
print("{} {} {}".format(Chicken.feathers , Chicken.beak_shape, Chicken.can_fly))

