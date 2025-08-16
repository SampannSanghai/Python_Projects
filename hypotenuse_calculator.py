import math

base = float(input("Enter Base Length in cm : "))
perpendicular = float(input("Enter Perpendicular Length in cm : "))

print(" ")

hypotenuse = math.sqrt(math.pow(base,2) + math.pow(perpendicular,2))

print("Length of Hypotenuse for the triangle is ",hypotenuse," cm")