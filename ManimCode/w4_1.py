from manim import *
import random

class ColoredGraph(Scene):
    def construct(self):
        # Define the graph layout
        vertices = {
            0: LEFT * 2 + DOWN,
            1: LEFT * 2 + UP,
            2: RIGHT * 2 + UP,
            3: RIGHT * 2 + DOWN,
        }
        edge_list = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)]
        edge_config = {
            (0, 1): {"stroke_color": RED, "stroke_width": 4},
            (1, 2): {"stroke_color": GREEN, "stroke_width": 4},
            (2, 3): {"stroke_color": BLUE, "stroke_width": 4},
            (3, 0): {"stroke_color": PURPLE, "stroke_width": 4},
            (0, 2): {"stroke_color": TEAL, "stroke_width": 4},
            (1, 3): {"stroke_color": ORANGE, "stroke_width": 4},
        }

        # Create the graph
        graph = Graph(vertices.keys(), edge_list, layout=vertices, labels=True, edge_config=edge_config)

        # Add the graph to the scene
        self.add(graph)

        # Animate the opacity of the edges
        animations = []
        for edge in edge_list:
            animations.append(self.pulsate_edge(graph.edges[edge]))

        self.play(AnimationGroup(*animations, lag_ratio=0.5))
        self.wait(2)

    def pulsate_edge(self, edge):
        # Create a pulsating effect by animating the opacity
        return AnimationGroup(
            edge.animate.set_opacity(1),
            edge.animate.set_opacity(0.2),
            rate_func=there_and_back,  # Makes the opacity animate back and forth
            run_time=2,  # Duration of the pulsating effect
            lag_ratio=random.uniform(0, 1)  # Random stagger to desynchronize the pulsating effect
        )

if __name__ == "__main__":
    scene = ColoredGraph()
    scene.render()
