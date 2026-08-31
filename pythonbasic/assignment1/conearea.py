import math

def area_of_cone(radius, slant_height):
    return math.pi * radius * (radius + slant_height)

# Example usage:
r = 5  # radius
l = 7  # slant height
area = area_of_cone(r, l)
print(f"Total Surface Area of cone: {area:.2f}")
