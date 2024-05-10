from manim import *
import subprocess
from manim import Scene
import random
import numpy as np

# Define a class for the square animation
class Amoeba(Scene):
    def construct(self):
        # Initialize parameters
        num_circles = 20
        min_distance = 0.0  # Minimum distance between circumferences of circles
        min_radius = 0.2   # Minimum radius of each circle
        max_radius = 0.5   # Maximum radius of each circle
        
        # Initialize list to store circle centers and radii
        circle_data = []
        
        # Generate circle centers and radii
        for _ in range(num_circles):
            while True:
                # Randomly generate a center point
                center = self.random_center()
                
                # Randomly generate a radius
                radius = random.uniform(min_radius, max_radius)
                
                # Check if the new circle satisfies the minimum distance constraint
                if self.valid_circle(center, radius, circle_data, min_distance):
                    circle_data.append((center, radius))
                    break
        
        # Create circles at the generated centers with varied radii
        circles = [Circle(radius=radius, color=BLUE, fill_opacity=1).move_to(center) for center, radius in circle_data]
        
        # Add the circles to the scene
        self.add(*circles)
        
        # Number of pulsations
        num_pulsations = 5
        
        # Pulsating animation for each circle
        for _ in range(num_pulsations):
            for circle in circles:
                self.play(
                    circle.animate.scale(1.2),
                    rate_func=there_and_back,
                    run_time=1
                )
    
    def random_center(self):
        # Randomly generate x and y coordinates within a certain range
        x = random.uniform(-5, 5)
        y = random.uniform(-3, 3)
        return np.array([x, y, 0])
    
    def valid_circle(self, new_center, new_radius, existing_circles, min_distance):
        # Check if the new circle's circumference touches any existing circle's circumference
        for center, radius in existing_circles:
            if np.linalg.norm(new_center - center) < radius + new_radius + min_distance:
                return False
        return True
    
if __name__ == "__main__":
    # Render the animation
    scene = Amoeba()
    scene.render()
