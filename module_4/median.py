print("name - VIDHI SHARMA  roll no - 1900300100242")
print("Enter value 1 : ")
x=int(input())
print("Enter value 2 : ")
y=int(input())
print("Enter value 3 : ")
z=int(input())
if x>y:
    if x<z:
        median=x
    else:
        if y>z:
            median=y
        else:
            median=z
elif x>z:
    if x<y:
        median=x
    else:
        if z>y:
            median=z
        else:
            median=y
else:
    median=y
print("median = ")
print(median)
