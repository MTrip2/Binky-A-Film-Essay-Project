from manim import *
import subprocess
from manim import Scene

import numpy as np

# Define a class for the square animation
class SphereScene(ThreeDScene):
    def construct(self):
        # Create a sphere
        sphere = Sphere(radius=1, resolution=(30, 30), color=BLUE)
        
        # Add the sphere to the scene
        self.add(sphere)
        
        # Rotate the sphere
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(4)  # Adjust the duration of the rotation
        self.stop_ambient_camera_rotation()
    
if __name__ == "__main__":
    # Render the animation
    scene =SphereScene()
    scene.render()
