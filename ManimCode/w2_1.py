from manim import *
import subprocess
from manim import Scene

import numpy as np

# Define a class for the square animation
class SnowflakeFractal(Scene):
    def construct(self):
        # Initial triangle vertices
        triangle_vertices = [
            np.array([0, 0, 0]),
            np.array([2, 0, 0]),
            np.array([1, np.sqrt(3), 0])
        ]
        
        # Draw the initial triangle
        triangle = Polygon(*triangle_vertices, color=WHITE, fill_opacity=0)
        self.add(triangle)
        
        # Recursively generate snowflake fractal
        self.generate_snowflake(triangle_vertices, depth=10)
    
    def generate_snowflake(self, vertices, depth):
        if depth == 0:
            return
        else:
            # Divide each line segment into three equal parts
            new_vertices = [
                vertices[0],
                self.divide_segment(vertices[0], vertices[1]),
                self.divide_segment(vertices[1], vertices[2]),
                vertices[2]
            ]
            
            # Draw the new segments
            for i in range(len(new_vertices) - 1):
                line = Line(new_vertices[i], new_vertices[i + 1], color=WHITE)
                self.add(line)
            
            # Recursively generate the snowflake fractal
            for i in range(len(new_vertices) - 1):
                mid_point = self.divide_segment(new_vertices[i], new_vertices[i + 1])
                next_vertices = [new_vertices[i], mid_point, new_vertices[i + 1]]
                self.generate_snowflake(next_vertices, depth - 1)
    
    def divide_segment(self, point1, point2):
        return (point1 + point2) / 2
    
if __name__ == "__main__":
    # Render the animation
    scene = SnowflakeFractal()
    scene.render()
