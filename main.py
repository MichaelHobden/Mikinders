# Import necessary modules and classes
import random
from Environment import Environment
from Creature import Creature
from EnvironmentVisualization import EnvironmentVisualization
import time
# Define parameters for the environment
width = 100
height = 100
food_count = 5


# Create the environment
env = Environment(width, height, food_count)
vis = EnvironmentVisualization(1000, 1000)
creature = Creature()


def update(dt):
    env.update([creature])
    food_positions = env.get_food()
    c_x, c_y, d = creature.get_positional_data()
    creature_position = (c_x, c_y)
    vis.update_grid(creature_position, food_positions)


last_frame_time = time.time()
fps = 120

while True:
    current_time = time.time()
    dt = current_time - last_frame_time
    last_frame_time = current_time

    update(dt)
    sleep_time = 1.0 / fps - dt

    if sleep_time > 0:
        time.sleep(sleep_time)
