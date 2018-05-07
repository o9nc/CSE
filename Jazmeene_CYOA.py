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
    def __init__(self, use, name, amount, material):
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
    def __init__(self, name, color, brand, use):
        super(Clothing, self).__init__(name, color)
        self.name = name
        self.color = color
        self.brand = brand
        self.use = use


class Outfit(Clothing):
    def __init__(self, name, color, brand, use):
        super(Outfit, self).__init__(name, color, brand, None)
        self.name = name
        self.color = color
        self.brand = brand
        self.use = use

    def wear(self):
        print("you put on %s " % self.name)


class Shirt(Outfit):
    def __init__(self):
        super(Shirt, self).__init__("Shirt", "red", "nike", "change shirts")

    def shirt_use(self):
        print("you %s when you're done playing basketball" % self.use)


class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.name = name

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
SCE = Room("Sport complex entrance", "This is a building with two doors. On the west side of the building there is an "
                                     "entrance door. On the south side there is an exit.", None, None, "FIELD ONE", None
           , None, None)


current_node = SCE
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)