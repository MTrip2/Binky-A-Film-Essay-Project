from manim import *
import subprocess
from manim import Scene

import numpy as np

# Define a class for the square animation

class PulsatingSphere(Scene):
    def construct(self):
        # Create a sphere
        sphere = Circle(radius=1, color=BLUE)
        
        # Add the sphere to the scene
        self.add(sphere)
        
        # Number of pulsations
        num_pulsations = 5
        
        # Pulsating animation
        for _ in range(num_pulsations):
            self.play(
                sphere.animate.scale(1.5),  # Scale up
                rate_func=there_and_back,
                run_time=1
            )
            self.play(
                sphere.animate.scale(1),  # Scale down
                rate_func=there_and_back,
                run_time=1
            )

if __name__ == "__main__":
    # Render the animation
    scene = PulsatingSphere()
    scene.render()
