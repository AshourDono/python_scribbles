import math

radius = float(input("Please enter a circle radius: "))


def circle_calc(radius):
    circumference = 2*math.pi*radius
    area = math.pi*radius**2

    print(f"your circle circumference is {circumference}")
    print(f"your circle area is {area}")


circle_calc(radius)
