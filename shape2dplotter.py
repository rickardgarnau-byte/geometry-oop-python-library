"""
Shape2DPlotter module - A class to plot 2D shapes using Matplotlib.

This module uses the matplotlib.patches library to create and add
geometric shapes (Circle, Rectangle) to a pyplot axes.

Sources:
- Official Matplotlib Patches API documentation:
  https://matplotlib.org/stable/api/patches_api.html
- The structure for the 'add_shape' method (using isinstance)
  was suggested by an LLM.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from shape import Shape
from rectangle import Rectangle
from circle import Circle


class Shape2DPlotter:
    """
    A class to plot 2D shapes that inherit from Shape.
    """

    def __init__(self, title: str = "My 2D Shapes"):
        """Initialize a Shape2DPlotter with an empty matplotlib canvas."""
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.ax.set_aspect("equal")
        self.ax.grid(True)
        self.ax.set_title(title)
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")

    def add_shape(self, shape_obj: Shape) -> None:
        """Adds a 2D shape (Circle or Rectangle) to the plot."""
        if isinstance(shape_obj, Circle):
            patch = patches.Circle(
                (shape_obj.x, shape_obj.y),
                shape_obj.radius,
                facecolor="blue",
                alpha=0.6,
            )
        elif isinstance(shape_obj, Rectangle):
            patch = patches.Rectangle(
                (shape_obj.x, shape_obj.y),
                shape_obj.width,
                shape_obj.height,
                facecolor="red",
                alpha=0.6,
            )
        else:
            print(f"Warning: Cannot draw unknown shape type {type(shape_obj)}")
            return

        self.ax.add_patch(patch)


    def show_plot(self) -> None:
        """Displays the plot with all added shapes."""
        self.ax.relim()
        self.ax.autoscale_view()
        plt.show()


if __name__ == "__main__":
    print("Creating plotter and shapes...")

    plotter = Shape2DPlotter(title="Test Plot of My Shapes")
    c1 = Circle(x=5, y=5, radius=4)
    r1 = Rectangle(x=0, y=0, width=3, height=6)
    c2 = Circle(x=-3, y=-2, radius=1.5)
    r2 = Rectangle(x=-8, y=2, width=2, height=2)

    for shape in [c1, r1, c2, r2]:
        plotter.add_shape(shape)

    print("Showing plot...")
    plotter.show_plot()
