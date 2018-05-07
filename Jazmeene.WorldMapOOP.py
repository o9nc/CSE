class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down, ):
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
                                     "entrance door. On the south side there is an exit.", None, None, "FIELDONE", None
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