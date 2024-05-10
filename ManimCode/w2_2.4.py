from manim import *
import subprocess
from manim import Scene
import random
import numpy as np

class MovingWave(Scene):
    def construct(self):
        # Draw the axis
        self.draw_axis()
        # Draw the sine waves
        self.draw_sine_waves()

    def draw_axis(self):
        # Create x and y axes
        x_axis = Line(np.array([-4,0,0]), np.array([4,0,0]))
        y_axis = Line(np.array([-4,2,0]), np.array([-4,-2,0]))

        # Add axes to the scene
        self.add(x_axis, y_axis)
        # Define minimum and maximum values for x-axis
        self.x_min = -4
        self.x_max = 4

    def draw_sine_waves(self):
        # Create a ValueTracker to animate the waves
        vt = ValueTracker(0)
        # Number of sine waves to draw
        num_waves = 5
        # Create a VGroup to hold all the sine waves
        sine_waves = VGroup()

        # Iterate over the number of waves
        for i in range(num_waves):
            # Get a sine wave and add it to the VGroup
            sine_wave = self.get_sine_wave(i, num_waves)
            sine_waves.add(sine_wave)

        # Define an updater function to animate the waves
        def update_waves(waves):
            for i, wave in enumerate(waves):
                wave.become(self.get_sine_wave(i, num_waves, dx=vt.get_value()))

        # Add the updater to the VGroup
        sine_waves.add_updater(update_waves)

        # Add the VGroup to the scene
        self.add(sine_waves)
        # Wait for 2 seconds before proceeding
        self.wait(2)

        # Move all sine waves 2PI in 4 seconds
        moving_time = 4
        moving_length = 2 * PI
        # Animate the ValueTracker to move the waves
        self.play(vt.animate.set_value(moving_length), run_time=moving_time, rate_func=linear)
        # Wait for the animation to finish
        self.wait()

    def get_sine_wave(self, wave_num, total_waves, dx=0):
        # Calculate parameters for the sine wave
        frequency = (wave_num + 1) * 2  # Adjust frequency based on wave number
        amplitude = 0.5  # Adjust amplitude as desired
        phase_shift = wave_num * PI / 2  # Adjust phase shift based on wave number

        # Define the range of x values for the wave
        x_range = (self.x_min, self.x_max)

        # Create the sine wave
        return FunctionGraph(
            lambda x: amplitude * np.sin((frequency * (x - self.x_min) + phase_shift + dx)),
            x_range=x_range,
            color=YELLOW
        )
    

if __name__ == "__main__":
    # Render the animation
    scene = MovingWave()
    scene.render()
