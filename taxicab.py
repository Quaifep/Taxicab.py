# Author: Paul Quaife
# Date: 2/4/2021
# Description: Sets coordinate and keeps track of movement for Taxicab.

class Taxicab:
    """
    Creates the class, Taxicab.
    """
    def __init__(self, x, y):
        """Sets definitions and odometer value."""
        self.x_coordinate = x
        self.y_coordinate = y
        self.odometer = 0

    def get_x_coord(self):
        """Sets Left and Right of initial Coordinate"""
        return self.x_coordinate

    def get_y_coord(self):
        """Sets up Up and Down of initial Coordinates."""
        return self.y_coordinate

    def get_odometer(self):
        """Adds changes to odometer reading"""
        return self.odometer

    def move_x(self, distance):
        self.x_coordinate += distance
        self.odometer += abs(distance)

    def move_y(self, distance):
        self.y_coordinate += distance
        self.odometer += abs(distance)
