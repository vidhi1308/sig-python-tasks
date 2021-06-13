print("name - VIDHI SHARMA  roll no - 1900300100242")
print("enter side 1 of triangle")
x=input()
print("enter side 2 of triangle")
y=input()
print("enter side 3 of triangle")
z=input()
if x==y and y==z and z==x:
    print("equilateral triangle")
elif x==y or y==z or x==z:
    print("isosceles triangle")
else:
    print("scalene triangle")
