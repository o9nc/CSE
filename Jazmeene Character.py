class Character(object):
    def __init__(self, name, health, inventory, status_effects, abilities):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.status_effects = status_effects
        self.abilities = abilities


Character("Xavier", 50, "basketball, backpack, water, gatorade, towel, shoes, extra clothes", "sleep",
          "strong, speed, high jumps")