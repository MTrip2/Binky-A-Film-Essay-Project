from manim import *
import subprocess
from manim import Scene

# Define a class for the square animation
class FractalSquare(Scene):
    def construct(self):
        self.draw_fractal_square(self.camera.frame_center, 4, 4, 2)

    def draw_fractal_square(self, center, level, n, size):
        if level == 0:
            return
        else:
            square = Square(side_length=size, stroke_color=WHITE, stroke_width=1)
            square.move_to(center)

            self.add(square)

            new_size = size / 3

            self.draw_fractal_square(center + UP * new_size, level - 1, n - 1, new_size)
            self.draw_fractal_square(center + DOWN * new_size, level - 1, n - 1, new_size)
            self.draw_fractal_square(center + LEFT * new_size, level - 1, n - 1, new_size)
            self.draw_fractal_square(center + RIGHT * new_size, level - 1, n - 1, new_size)

if __name__ == "__main__":
    # Render the animation
    scene = SquareAnimation()
    scene.render()
