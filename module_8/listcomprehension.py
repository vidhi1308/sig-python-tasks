print("name - VIDHI SHARMA  roll no - 1900300100242")
print("enter the number of elements in the list : ")
n=int(input())
l=[]
sum=0
print("Enter list elements : ")
for i in range(0, n):
    s=int(input())
    l.append(s)
for i in l:
    sum +=i
print("sum of all elements :", sum)

