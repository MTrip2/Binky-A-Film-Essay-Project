from manim import *
import subprocess
from manim import Scene

import numpy as np

# Define a class for the square animation

class PulsatingSpheres(Scene):
    def construct(self):
        # Create two spheres
        sphere1 = Circle(radius=1, color=BLUE)
        sphere2 = Circle(radius=1, color=RED)
        
        # Initial positions of spheres
        sphere1.move_to(LEFT * 2)
        sphere2.move_to(RIGHT * 2)
        
        # Add the spheres to the scene
        self.add(sphere1, sphere2)
        
        # Number of pulsations
        num_pulsations = 5
        
        # Pulsating animation with movement
        for _ in range(num_pulsations):
            self.play(
                sphere1.animate.scale(1.5).shift(LEFT * 2),  # Scale up and move left
                sphere2.animate.scale(1.5).shift(RIGHT * 2), # Scale up and move right
                rate_func=there_and_back,
                run_time=1
            )
            self.play(
                sphere1.animate.scale(1).shift(RIGHT * 2),   # Scale down and move right
                sphere2.animate.scale(1).shift(LEFT * 2),    # Scale down and move left
                rate_func=there_and_back,
                run_time=1
            )
            
if __name__ == "__main__":
    # Render the animation
    scene = PulsatingSphere()
    scene.render()
