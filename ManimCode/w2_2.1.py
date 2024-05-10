from manim import *
import subprocess
from manim import Scene
import random
import numpy as np

# Define a class for the square animation
class Amoeba(Scene):
    def construct(self):
        # Initialize parameters
        num_balls = 50
        min_distance = 0.5  # Minimum distance between centers of balls
        ball_radius = 0.2   # Radius of each ball
        
        # Initialize list to store ball centers
        ball_centers = []
        
        # Generate ball centers
        for _ in range(num_balls):
            while True:
                # Randomly generate a center point
                center = self.random_center()
                
                # Check if the new center satisfies the minimum distance constraint
                if self.valid_center(center, ball_centers, min_distance):
                    ball_centers.append(center)
                    break
        
        # Create balls at the generated centers
        balls = [Circle(radius=ball_radius, color=BLUE, fill_opacity=1).move_to(center) for center in ball_centers]
        
        # Add the balls to the scene
        self.add(*balls)
        
        # Number of pulsations
        num_pulsations = 5
        
        # Pulsating animation for each ball
        for _ in range(num_pulsations):
            for ball in balls:
                self.play(
                    ball.animate.scale(1.2),
                    rate_func=there_and_back,
                    run_time=1
                )
    
    def random_center(self):
        # Randomly generate x and y coordinates within a certain range
        x = random.uniform(-5, 5)
        y = random.uniform(-3, 3)
        return np.array([x, y, 0])
    
    def valid_center(self, new_center, existing_centers, min_distance):
        # Check if the new center is far enough from all existing centers
        for center in existing_centers:
            if np.linalg.norm(new_center - center) < min_distance:
                return False
        return True

if __name__ == "__main__":
    # Render the animation
    scene = Amoeba()
    scene.render()
