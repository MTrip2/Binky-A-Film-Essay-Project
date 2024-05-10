from manim import *
import subprocess
from manim import Scene

# Define a class for the square animation
class SquareAnimation(Scene):
    def construct(self):
        # Create a square object
        square = Square()

        # Play the animation to create the square
        self.play(Create(square))

        # Wait for 2 seconds
        self.wait(2)

if __name__ == "__main__":
    # Render the animation
    scene = SquareAnimation()
    scene.render()
