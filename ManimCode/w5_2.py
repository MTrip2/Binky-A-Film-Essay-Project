from manim import *
import numpy as np
import random

class MultiColoredSpiral(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        num_spirals = 5  # Total number of spirals
        t_max = 6 * TAU  # Maximum t value for spirals
        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]  # Colors for the spirals

        spirals = VGroup()
        dots_group = VGroup()

        for i in range(num_spirals):
            spiral = ParametricFunction(
                lambda t, li=i: np.array([
                    0.6 * (t + li) * np.cos(t + 0.5 * li),  # x coordinate
                    0.6 * (t + li) * np.sin(t + 0.5 * li),  # y coordinate
                    0.1 * (t + li)                           # z coordinate (for 3D effect)
                ]),
                t_range=[0, t_max],
                color=colors[i % len(colors)]
            )
            spirals.add(spiral)

            # Adding dots
            num_dots = 10  # Adjust the number of dots per spiral
            for _ in range(num_dots):
                t = random.uniform(0, t_max)
                dot_point = spiral.point_from_proportion(t / t_max)
                dot = Dot(dot_point, color=BLACK, radius=0.1)
                dots_group.add(dot)

        # Animation
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(LaggedStart(*[Create(spiral) for spiral in spirals], lag_ratio=0.2, run_time=4))
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in dots_group], lag_ratio=0.1))
        self.wait(2)

if __name__ == "__main__":
    scene = MultiColoredSpiral()
    scene.render()


