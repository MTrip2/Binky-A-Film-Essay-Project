from manim import *

class ConcentricCircles(Scene):
    def construct(self):
        # Parameters
        num_layers = 100  # Number of layers
        max_radius = 2  # Maximum radius
        min_radius = 0.1  # Minimum radius
        center = ORIGIN  # Center of the circles
        density_factor = 3  # Factor to control the density (adjust as needed)
        
        # Create concentric circles
        circles = VGroup()
        for i in range(num_layers):
            radius = self.get_radius(i, num_layers, max_radius, min_radius, density_factor)
            circle = Circle(radius=radius)
            circles.add(circle)
        
        # Arrange circles
        self.arrange_circles(circles)

        # Add to scene
        self.add(circles)

    def get_radius(self, layer, num_layers, max_radius, min_radius, density_factor):
        """
        Calculate the radius of a circle based on the layer and the cosine of the layer number.
        """
        angle = layer / num_layers * 5
        cosine_density = (np.cos(angle) + 1) / 2  # Adjust to [0, 1]
        radius_range = max_radius - min_radius
        radius = min_radius + cosine_density * radius_range * density_factor
        return radius

    def arrange_circles(self, circles):
        """
        Arrange circles in a concentric pattern.
        """
        for i, circle in enumerate(circles):
            circle.move_to(ORIGIN)

if __name__ == "__main__":
    scene = ConcentricCircles()
    scene.render()
