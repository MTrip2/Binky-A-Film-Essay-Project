from manim import *
import random
import string
import numpy as np

class AnimateRectangles(Scene):
    def construct(self):
        # Define the rectangles with specific colors and sizes
        rectangles = [
            Rectangle(width=4, height=1, color=WHITE, fill_opacity=0.2),
            Rectangle(width=3, height=1, color=PURPLE, fill_opacity=0.2),
            Rectangle(width=2.5, height=1, color=BLUE, fill_opacity=0.2),
            Rectangle(width=2, height=1, color=PURPLE, fill_opacity=0.2),
            Rectangle(width=1.5, height=1, color=RED, fill_opacity=0.2)
        ]

        # Set initial positions
        current_y = 3
        for rectangle in rectangles:
            rectangle.shift(UP*current_y)
            current_y -= 1.5  # Adjust spacing between rectangles

        # Animate the rectangles appearing one by one
        for rectangle in rectangles:
            self.play(Create(rectangle))
            self.wait(0.5)  # Wait half a second between each rectangle

        self.wait(2)  # Hold the final scene for 2 seconds

if __name__ == "__main__":
    # Render the animation
    scene = AnimateRectangles()
    scene.render()
