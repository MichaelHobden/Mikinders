import tkinter as tk
import random


class EnvironmentVisualization:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.draw_grid()

    def draw_grid(self):
        for i in range(self.width):
            self.canvas.create_line(
                i * 10, 0, i * 10, self.height, fill="gray")
        for j in range(self.height):
            self.canvas.create_line(0, j * 10, self.width, j * 10, fill="gray")

    def update_grid(self, creature_position, food_positions):
        self.canvas.delete("all")

        self.draw_grid()

        self.draw_creature(creature_position)

        for food_pos in food_positions:
            self.draw_food(food_pos)

        self.root.update()

    def draw_creature(self, position):
        x, y = position
        self.canvas.create_rectangle(
            x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill="blue")

    def draw_food(self, position):
        x, y = position
        self.canvas.create_rectangle(
            x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill="green")

    def run(self):
        self.root.mainloop()
