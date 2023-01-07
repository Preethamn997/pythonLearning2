import math
print("You need to enter Three Values nameley")
a = int(input("enter first vakue :"))
b = int(input("enter second value :"))
c = int(input("enter third value :"))
root1 = (-b+math.sqrt((b**2)-4*a*c))/(2*a)
root2 = (-b-math.sqrt((b**2)-4*a*c))/(2*a)
print(root1)
print(root2)