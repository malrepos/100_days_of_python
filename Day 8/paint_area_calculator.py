import math


def paint_area(height, width, coverage):
    print(f"You need {math.ceil((height*width) / coverage)} cans of paint.")


wall_height = int(input("How high is the wall:"))
wall_width = int(input("How wide is the wall:"))
coverage = int(input("What is the coverage per can:"))

paint_area(wall_height, wall_width, coverage)
