def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
    """
    pi = 3.14159
    area = pi * radius**2
    return area

radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:", calculate_area(radius))
