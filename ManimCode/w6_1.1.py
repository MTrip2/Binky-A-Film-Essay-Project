from manim import *

class PreFuzzCloud(Scene):
    def construct(self):
        # Create amoebic boundary
        boundary = ParametricFunction(
            lambda t: np.array([np.sin(t) + 0.2 * np.sin(5 * t), np.cos(t) + 0.2 * np.cos(5 * t), 0]),
            t_range=[0, TAU],
            color=WHITE
        ).scale(3)

        # Add random strands
        strands = VGroup()
        for _ in range(100):  # Adjust number of strands
            # Generate random points for start_anchor, start_handle, end_handle, end_anchor
            start_anchor = self.random_point()
            start_handle = self.random_point()
            end_handle = self.random_point()
            end_anchor = self.random_point()

            # Create CubicBezier object
            strand = CubicBezier(start_anchor, start_handle, end_handle, end_anchor, color=WHITE)
            strands.add(strand)

            # Animate perturbations
            self.play(
                strand.animate.apply_function(lambda p: p + np.random.uniform(-0.2, 0.2, 3)),
                rate_func=linear,
                run_time=3
            )

        # Add nodes or dots
        dots = VGroup()
        for strand in strands:
            dot_positions = np.linspace(0, 1, num=5)  # Adjust number and placement of dots
            for pos in dot_positions:
                dot = Dot(point=strand.point_from_proportion(pos), color=BLACK)
                dots.add(dot)

        # Combine all elements
        self.add(boundary, dots)

    def random_point(self):
        # Random point generation within an assumed range
        x = np.random.uniform(-3, 3)
        y = np.random.uniform(-3, 3)
        return np.array([x, y, 0])

if __name__ == "__main__":
    scene = PreFuzzCloud()
    scene.render()
