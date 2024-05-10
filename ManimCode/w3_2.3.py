from manim import *
import random
import string
import numpy as np

class AnimateRectanglesWithArrows(Scene):
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

        # Adding arrows between the rectangles
        arrows = []
        for i in range(len(rectangles) - 3):
            arrow = Arrow(start=rectangles[i].get_bottom(), end=rectangles[i + 1].get_top(), buff=0.1, max_stroke_width_to_length_ratio=10)
            arrows.append(arrow)

        # Animate the arrows appearing
        for arrow in arrows:
            self.play(Create(arrow))
            self.wait(0.5)  # Wait half a second between each arrow

        for arrow in arrows:
            self.play(arrow.animate.shift(RIGHT * 0.5))
            self.wait(0.5)  # Wait half a second between each movement

        u_arrows = []
        for i in range(-(len(rectangles) - 1),0):
            u_arrow = Arrow(start=rectangles[-i].get_top(), end=rectangles[-(i + 1)].get_bottom(), buff=0.1, max_stroke_width_to_length_ratio=10)
            u_arrows.append(u_arrow)

        for u_arrow in u_arrows:
            self.play(Create(u_arrow))
            self.wait(0.5) 

        for u_arrow in u_arrows:
            self.play(u_arrow.animate.shift(LEFT * 0.5))
            self.wait(0.5)  # Wait half a second between each movement


        self.wait(2)  # Hold the final scene for 2 seconds

if __name__ == "__main__":
    # Render the animation
    scene = AnimateRectanglesWithArrows()
    scene.render()

if __name__ == "__main__":
    # Render the animation
    scene = AnimateRectanglesWithArrows()
    scene.render()
