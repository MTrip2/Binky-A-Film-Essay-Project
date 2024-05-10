from manim import *
import random
import string
import numpy as np

class CircleText(Scene):
    def construct(self):
        text = Text("Theorizing Multiple Ecologies", font_size=48)
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text))
        
if __name__ == "__main__":
    # Render the animation
    scene = CircleText()
    scene.render()
