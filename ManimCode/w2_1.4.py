from manim import *
import subprocess
from manim import Scene

import numpy as np

import random

# Define a class for the square animation

class PulsatingSpheres(Scene):
    def construct(self):
        # Number of spheres
        num_spheres = 50
        
        # Create spheres with different colors and initial positions
        spheres = [
            Circle(radius=0.5, color=self.random_color()).move_to(self.random_position())
            for _ in range(num_spheres)
        ]
        
        # Add the spheres to the scene
        self.add(*spheres)
        
        # Number of pulsations
        num_pulsations = 5
        
        # Pulsating animation with movement
        for _ in range(num_pulsations):
            for sphere in spheres:
                self.play(
                    sphere.animate.scale(1.5).shift(self.random_direction()),  # Scale up and move
                    rate_func=there_and_back,
                    run_time=1
                )
            self.wait(0.1)  # Wait for a short duration between pulsations

    def random_color(self):
        return random.choice([BLUE, RED, GREEN, YELLOW, ORANGE, PURPLE, PINK])  # Add more colors as needed
    
    def random_position(self):
        x = random.uniform(-5, 5)
        y = random.uniform(-3, 3)
        return np.array([x, y, 0])
    
    def random_direction(self):
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)
        return np.array([dx, dy, 0])


if __name__ == "__main__":
    # Render the animation
    scene = PulsatingSpheres()
    scene.render()
