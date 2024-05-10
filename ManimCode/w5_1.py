from manim import *
import random

class OrbitDiagram(Scene):
    def construct(self):
        # Define the number of orbits and their properties
        num_orbits = 3
        colors = [BLUE, PURPLE, TEAL]  # Colors for each orbit
        dot_colors = [GREEN, PURPLE, GREEN]  # Colors for the dots on each orbit
        orbits = []
        dots_group = VGroup()

        # Create the orbits and the dots
        for i in range(num_orbits):
            # Create an ellipse for the orbit
            orbit = Ellipse(width=4 + i, height=2 + 0.5 * i, color=colors[i]).shift(UP * 0.5 * i)
            orbits.append(orbit)
            self.add(orbit)

            # Add dots to each orbit
            num_dots = 6
            for j in range(num_dots):
                angle = TAU / num_dots * j
                dot = Dot(color=dot_colors[i]).move_to(orbit.point_at_angle(angle))
                dots_group.add(dot)

        # Add all dots at once to the scene for better performance
        self.add(dots_group)

        # Animate all elements coming into view
        self.play(LaggedStart(*[Create(orbit) for orbit in orbits], lag_ratio=0.5))
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in dots_group], lag_ratio=0.1))
        self.wait(2)

if __name__ == "__main__":
    scene = OrbitDiagram()
    scene.render()
