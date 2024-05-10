from manim import *
import random
import string
import numpy as np

class DisplayRandomText(Scene):
    def construct(self):
        text = Text("Theorizing Multiple Ecologies", font_size=48)
        self.play(Write(text))
        self.wait(2)

if __name__ == "__main__":
    # Render the animation
    scene = DisplayRandomText()
    scene.render()
