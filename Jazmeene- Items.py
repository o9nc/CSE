class Item(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Tool(Item):
    def __init__(self, name, amount, material, use):
        super(Tool, self).__init__(name, amount)
        self.material = material
        self.use = use


class Towel (Tool):
    def __init__(self, use, name, amount, material,):
        super(Towel, self).__init__(name, amount, material, use)
        self.use = use
        self.name = name
        self.amount = amount
        self.material = material

    def towel_use(self):
        print("you use this towel to %s up sweat" % self.use)


Test1 = Towel("dry", Towel, 1, "cloth")
Test1.towel_use()


class Basketball (Towel):
    def __init__(self):
        super(Basketball, self).__init__("play", "basketball", 1, "leather")

    def basketball_use(self):
        print("you use this basketball to %s" % self.use)


Test2 = Basketball()
Test2.basketball_use()


class Ball_Hog_Gloves (Towel):
    def __init__(self):
       super(Ball_Hog_Gloves, self).__init__("handling", "ball hog gloves", 2, None)

    def ball_hog_gloves_use(self):
        print("you use the ball hog gloves for %s" % self.use)


Test3 = Ball_Hog_Gloves()
Test3.ball_hog_gloves_use()


class Clothing(Item):
    def __init__(self, name, color, brand):
        super(Clothing, self).__init__(name, color)
        self.name = name
        self.color = color
        self.brand = brand


class Outfit(Clothing):
    def __init__(self, name, color, brand):
        super(Outfit, self).__init__(name, color, brand)
        self.name = name
        self.color = color
        self.brand = brand

    def wear(self):
        print("you put on %s " % self.name)


class Shirt(Outfit):
    def __init__(self):
        super(Shirt, self).__init__("Shirt", "red", "nike")

    def Outfit_use(self):
        print("you %s the outfit when done playing basketball" %self.use)

