from manim import *
import random
import string
import numpy as np

class AnimateIsometricParallelograms(Scene):
    def construct(self):
        # Define parallelograms with specific colors and sizes
        parallelograms = [
            self.create_parallelogram(4, 1, WHITE),
            self.create_parallelogram(3, 1, PURPLE),
            self.create_parallelogram(3, 1, RED),
            self.create_parallelogram(2.5, 1, BLUE),
            self.create_parallelogram(2, 1, PURPLE),
            self.create_parallelogram(1.5, 1, RED)
        ]

        # Calculate the center of each parallelogram to align them
        offsets = [par.get_center()[0] - parallelograms[0].get_center()[0] for par in parallelograms]

        # Set initial positions so centers are aligned
        current_y = 0
        for parallelogram, offset in zip(parallelograms, offsets):
            parallelogram.shift(UP * current_y - RIGHT * offset)  # Adjust position for center alignment
            current_y -= 1.2  # Adjust spacing between parallelograms

        # Animate the parallelograms appearing one by one
        for parallelogram in parallelograms:
            self.play(Create(parallelogram))
            self.wait(0.5)  # Wait half a second between each parallelogram

        self.wait(2)  # Hold the final scene for 2 seconds

    def create_parallelogram(self, width, height, color):
        # Coordinates for parallelogram with a 30-degree acute angle
        acute_angle = 30 * DEGREES
        dx = height * np.tan(acute_angle)  # Horizontal offset
        vertices = [
            [0, 0, 0],  # Bottom left
            [width, 0, 0],  # Bottom right
            [width + dx, height, 0],  # Top right
            [dx, height, 0],  # Top left
        ]
        parallelogram = Polygon(*vertices, color=color, fill_opacity=1)
        return parallelogram

if __name__ == "__main__":
    # Render the animation
    scene = AnimateIsometricParallelograms()
    scene.render()
