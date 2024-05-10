from manim import *
import random
import string
import numpy as np

class CircleText(Scene):
    def construct(self):
        text = Text("Hello, Manim!", font_size=48)
        self.play(Write(text))
        self.wait(1)
        self.play(text.animate.shift(2*UP).rotate(PI/2, about_point=ORIGIN), run_time=2)
        self.play(text.animate.shift(2*RIGHT).rotate(PI/2, about_point=ORIGIN), run_time=2)
        self.play(text.animate.shift(2*DOWN).rotate(PI/2, about_point=ORIGIN), run_time=2)
        self.play(text.animate.shift(2*LEFT).rotate(PI/2, about_point=ORIGIN), run_time=2)
        self.wait(1)

if __name__ == "__main__":
    # Render the animation
    scene = CircleText()
    scene.render()
