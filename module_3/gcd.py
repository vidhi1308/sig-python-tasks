print("name - VIDHI SHARMA  roll no - 1900300100242")
print("enter first no")
x = int(input())
print("enter second no")
y = int(input())
if x>y:
        small=y
else:
        small=x
for i in range(1,small+1):
        if((x%i==0)and(y%i==0)):
                gcd=i
print("gcd = ", gcd)
