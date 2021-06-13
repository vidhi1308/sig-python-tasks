print("name - VIDHI SHARMA  roll no - 1900300100242")
print("Enter the size of list : ")
n=int(input())
l=[]
print("Enter list elements : ")
for i in range(0, n):
    s=input()
    l.append(s)
print(l)
if len(l)==0:
    print("List is empty")
else:
    print("List is not empty")
