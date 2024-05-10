from manim import *
import subprocess
from manim import Scene
import random
import numpy as np

# Define a class for the square animation
class Amoeba(Scene):
    def construct(self):
        # Initialize parameters
        num_balls = 10
        min_distance = 0.1  # Minimum distance between edges of balls
        min_radius = 1  # Minimum radius of each ball
        max_radius = 2 # Maximum radius of each ball
        
        # Initialize list to store ball centers and radii
        ball_data = []
        
        # Generate ball centers and radii
        for i in range(num_balls):
            while True:
                if i == 0:
                    # For the first ball, center can be anywhere
                    center = self.random_center()
                else:
                    # For subsequent balls, ensure continuity with the previous ball
                    prev_center, prev_radius = ball_data[-1]
                    min_center = prev_center + (prev_radius + min_radius + min_distance) * np.array([1, 0, 0])
                    max_center = prev_center + (prev_radius + max_radius + min_distance) * np.array([1, 0, 0])
                    center = self.random_center_between(min_center, max_center)
                
                # Randomly generate a radius
                radius = random.uniform(min_radius, max_radius)
                
                # Check if the new ball satisfies the minimum distance constraint
                if self.valid_ball(center, radius, ball_data, min_distance):
                    ball_data.append((center, radius))
                    break
        
        # Create balls at the generated centers with varied radii
        balls = [Circle(radius=radius, color=BLUE, fill_opacity=1).move_to(center) for center, radius in ball_data]
        
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
        y = random.uniform(-5, 5)
        return np.array([x, y, 0])
    
    def random_center_between(self, min_center, max_center):
        # Randomly generate a center point between min_center and max_center
        x = random.uniform(min_center[0], max_center[0])
        y = min_center[1]  # Keep y-coordinate same as the previous ball
        return np.array([x, y, 0])
    
    def valid_ball(self, new_center, new_radius, existing_balls, min_distance):
        # Check if the new ball's edge touches or is within the minimum distance of any existing ball's edge
        for center, radius in existing_balls:
            if np.linalg.norm(new_center - center) < radius + new_radius + min_distance:
                return False
        return True     
if __name__ == "__main__":
    # Render the animation
    scene = Amoeba()
    scene.render()
