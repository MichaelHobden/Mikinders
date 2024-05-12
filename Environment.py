import random
from Creature import Creature  # Assuming Creature class is defined in "Creature.py"


class Environment:
    def __init__(self, width=100, height=100, food=5):
        self.width = width
        self.height = height
        self.food = []
        for i in range(food):
            self.add_food()

    def add_food(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.food:
                break
        self.food.append((x, y))

    def remove_food(self, position):
        if position in self.food:
            self.food.remove(position)

    def update(self, creatures):
        for creature in creatures:
            pos_x, pos_y, direction = creature.get_positional_data()
            creature_position = (pos_x, pos_y)
            if creature_position in self.food:
                self.food.remove(creature_position)
                self.add_food()
            visual_data = self.get_visual_data(creature_position, direction)
            reaction = creature.get_action(visual_data)

            # Move forward
            print(reaction)
            if reaction == 1:
                new_pos_y, new_pos_x = None, None
                if direction == 0:  # Up
                    new_pos_y = pos_y + 1
                elif direction == 1:  # Right
                    new_pos_x = pos_x + 1
                elif direction == 2:  # Down
                    new_pos_y = pos_y - 1
                elif direction == 3:  # Left
                    new_pos_x = pos_x - 1

                # Check if the new position is within bounds
                if 0 <= new_pos_x < self.width and 0 <= new_pos_y < self.height:
                    creature.set_position(new_pos_x, new_pos_y)

            # Turn right
            if reaction == 0:
                creature.set_direction((direction + 1) % 4)

            # Turn left
            if reaction == 2:
                creature.set_direction((direction - 1) % 4)

            # Train the creature after updating its position
            creature.train()

        # Spawn new food item if needed
        if random.random() < 1:
            self.add_food()

    def get_visual_data(self, creature_position, direction):
        visual_range = 3
        visual_data = []
        x, y = creature_position

        visual_data.append(direction)
        visual_data.append(x)
        visual_data.append(y)

        if direction == 0:  # Up
            for i in range(1, visual_range + 1):
                if y - i >= 0:
                    pos = (x, y - i)
                    visual_data.append(1 if pos in self.food else 0)
                else:
                    break
        elif direction == 1:  # Right
            for i in range(1, visual_range + 1):
                if x + i < self.width:
                    pos = (x + i, y)
                    visual_data.append(1 if pos in self.food else 0)
                else:
                    break
        elif direction == 2:  # Down
            for i in range(1, visual_range + 1):
                if y + i < self.height:
                    pos = (x, y + i)
                    visual_data.append(1 if pos in self.food else 0)
                else:
                    break
        elif direction == 3:  # Left
            for i in range(1, visual_range + 1):
                if x - i >= 0:
                    pos = (x - i, y)
                    visual_data.append(1 if pos in self.food else 0)
                else:
                    break
        return visual_data

    def get_food(self):
        return self.food
