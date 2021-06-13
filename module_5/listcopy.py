print("name - VIDHI SHARMA  roll no - 1900300100242")
print("enter the number of elements in the list : ")
n=int(input())
l=[]
copy=[]
print("Enter list elements : ")
for i in range(0, n):
    s=input()
    l.append(s)
print(l)
print("Copied list : ")
copy=l.copy()
print(copy)