print("name - VIDHI SHARMA  roll no - 1900300100242")
print("enter the number of elements in the list : ")
n=int(input())
l=[]
print("Enter list elements : ")
for i in range(0, n):
    s=input()
    l.append(s)
print(l)
print("Altered list : ")
for i in range(0,n):
    if i%2==0:
        l[i]='#'
print(l)