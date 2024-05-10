from manim import *
import subprocess
from manim import Scene

import numpy as np

# Define a class for the square animation
class AmoebaScene(Scene):
    def construct(self):
        # Create the main body of the amoeba
        amoeba_body = Circle(radius=2, color=YELLOW, fill_opacity=0.8)
        
        # Create pseudopodia (tentacles)
        pseudopodia = [
            self.create_pseudopodium(start_point=amoeba_body.get_center(), angle=i*TAU/6)
            for i in range(6)
        ]
        
        # Add the main body and pseudopodia to the scene
        self.add(amoeba_body, *pseudopodia)
        
        # Number of pulsations
        num_pulsations = 5
        
        # Pulsating animation for each pseudopodium
        for _ in range(num_pulsations):
            for pseudopodium in pseudopodia:
                self.play(
                    pseudopodium.animate.scale(1.2),
                    rate_func=there_and_back,
                    run_time=1
                )
    
    def create_pseudopodium(self, start_point, angle):
        # Define the length of pseudopodium
        pseudopodium_length = 2
        
        # Calculate end point of pseudopodium
        end_point = start_point + pseudopodium_length * np.array([np.cos(angle), np.sin(angle), 0])
        
        # Create and return the pseudopodium (line)
        return Line(start_point, end_point, color=BLUE, stroke_width=5)
    

if __name__ == "__main__":
    # Render the animation
    scene = AmoebaScene()
    scene.render()
