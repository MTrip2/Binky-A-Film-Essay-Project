from manim import *
import random

class ColoredComplexGraph(Scene):
    def construct(self):
        # Define the graph layout
        vertices = {}
        for i in range(30):
            vertices[i] = np.array([random.uniform(-5, 5), random.uniform(-3, 3), 0])

        edge_list = [(random.randint(0, 29), random.randint(0, 29)) for _ in range(50)]  # Random connections
        colors_hex = [
                "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
                "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#aec7e8", "#ffbb78",
                "#98df8a", "#ff9896", "#c5b0d5", "#c49c94", "#f7b6d2", "#c7c7c7",
                "#dbdb8d", "#9edae5", "#ad494a", "#8c6d31", "#843c39", "#fd8d3c",
                "#e7969c", "#7b4173", "#a55194", "#ce6dbd", "#de9ed6", "#6b6ecf"
            ]
        edge_config = {
            edge: {"stroke_color": color, "stroke_width": 2} 
            for edge, color in zip(edge_list, colors_hex)
        }

        # Create the graph
        graph = Graph(vertices.keys(), edge_list, layout=vertices, labels=False, edge_config=edge_config)

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
    scene = ColoredComplexGraph()
    scene.render()
