class Circle:
    _pi = 3.141  # Class private variable representing the value of pi

    def __init__(self, radius_list):
        self.radius_list = radius_list  # Initialize instance variable with the list of radii

    def _calculate_area(self, radius):
        return self._pi * (radius ** 2)  # Method to calculate the area of a circle with given radius

    def _calculate_perimeter(self, radius):
        return 2 * self._pi * radius  # Method to calculate the perimeter of a circle with given radius

    @classmethod
    def area(cls, radius_list):
        areas = []  # List to store calculated areas
        for radius in radius_list:
            area = cls._pi * (radius ** 2)  # Calculate area for each radius using class private variable
            areas.append(area)  # Append calculated area to the list
        return areas  # Return the list of calculated areas

    @classmethod
    def perimeter(cls, radius_list):
        perimeters = []  # List to store calculated perimeters
        for radius in radius_list:
            perimeter = 2 * cls._pi * radius  # Calculate perimeter for each radius using class private variable
            perimeters.append(perimeter)  # Append calculated perimeter to the list
        return perimeters  # Return the list of calculated perimeters


radius_list = [10, 501, 22, 37, 100, 999, 87, 351]  # List of radii
circle = Circle(radius_list)  # Create an instance of the Circle class with the list of radii

# Accessing methods directly
areas = Circle.area(radius_list)  # Calculate areas using class method
perimeters = Circle.perimeter(radius_list)  # Calculate perimeters using class method

for radius, area, perimeter in zip(radius_list, areas, perimeters):
    print(f"Circle with radius {radius}:")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    print()
