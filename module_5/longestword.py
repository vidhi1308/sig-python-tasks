print("name - VIDHI SHARMA  roll no - 1900300100242")
print("enter the number of elements in the list : ")
n=int(input())
l=[]
print("Enter list elements : ")
for i in range(0, n):
    s=input()
    l.append(s)
print(l)
print("Longest word in the entered list : ")
max = -1
for s in l: 
    if len(s) > max: 
        max = len(s) 
        longest =  s
print(longest)