from manim import *
import numpy as np
import random

class Spiral3DWithDots(ThreeDScene):
    def construct(self):
        # Set up axes (optional, for visual reference)
        axes = ThreeDAxes()
        self.add(axes)


        # Define the 3D spiral parameters
        spiral = ParametricFunction(
            lambda t: np.array([
                0.6 * t * np.cos(4 * t),  # x = r * cos(theta), narrower and more turns
                0.6 * t * np.sin(4 * t),  # y = r * sin(theta), narrower and more turns
                0.1 * t                  # z = slower linear increase
            ]),
            t_range=[0, 30*TAU],  # Increased range for more turns
            color=BLUE
        )

        # Create the spiral drawing animation
        draw_spiral = Create(spiral, run_time=10, rate_func=linear)

        # Prepare to add dots
        dots_group = VGroup()
        num_dots = 50  # Number of dots to place

        # Randomly place dots along the spiral
        for _ in range(num_dots):
            t = random.uniform(0, 30*TAU)  # Random parameter along the spiral's length
            proportion = t / (30*TAU)
            point_on_spiral = spiral.point_from_proportion(proportion)
            dot = Dot(point_on_spiral, color=random.choice([RED, GREEN, YELLOW, PURPLE]), radius=0.15)  # Larger dots
            dots_group.add(dot)

        # Move the camera to show the 3D effect
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
        
        # Animate the spiral and the dots
        self.play(draw_spiral)
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in dots_group], lag_ratio=0.1))
        self.wait(2)

if __name__ == "__main__":
    scene = Spiral3DWithDots()
    scene.render()
