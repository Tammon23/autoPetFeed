class Pet:
    def __init__(self, exercise, drink, food, name, slot_num=-1, page=1):
        self.exercise = exercise
        self.drink = drink
        self.food = food
        self.name = name
        self.slot_num = slot_num
        self.page = page

    def __str__(self):
        return f"Name: {self.name} Page: {self.page} Slot: {self.slot_num} Food: {self.food} Drink: {self.drink} Exercise: {self.exercise}"