import math

print("Pitagoras")

b = float(input("Write the value of b: "))
c = float(input("Write a value of c: "))

hip = a = (b**2 + c**2)
hip = math.sqrt(a)

print("{:.2}".format(hip))