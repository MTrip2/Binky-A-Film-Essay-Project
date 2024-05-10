from manim import *
import numpy as np
import random

class SpiralWithDots(Scene):
    def construct(self):
        # Define the spiral parameters
        spiral = ParametricFunction(
            lambda t: np.array([
                1.2 * t * np.cos(t),
                1.2 * t * np.sin(t),
                0
            ]),
            t_range=[0, 100*TAU],  # 10 turns
            color=BLUE
        )

        # Create the spiral drawing animation
        draw_spiral = Create(spiral, run_time=8, rate_func=linear)

        # Prepare to add dots
        dots_group = VGroup()
        num_dots = 30  # Number of dots to place

        # Randomly place dots along the spiral
        for _ in range(num_dots):
            t = random.uniform(0, 10*TAU)  # Random parameter along the spiral's length
            point_on_spiral = spiral.point_from_proportion(t / (10*TAU))
            dot = Dot(point_on_spiral, color=random.choice([RED, GREEN, YELLOW, PURPLE]), radius=0.1)
            dots_group.add(dot)

        # Animate the spiral and the dots
        self.play(draw_spiral)
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in dots_group], lag_ratio=0.1))
        self.wait(2)

if __name__ == "__main__":
    scene = SpiralWithDots()
    scene.render()
