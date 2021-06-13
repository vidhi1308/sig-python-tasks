print("name - VIDHI SHARMA  roll no - 1900300100242")
dic={}
sum=0
print("Enter the number of elements in the dictionary : ")
n=int(input())
print("Enter dictionary elements : ")
for i in range(1,n+1):
    dic[i]=int(input())
print(dic)
print("Sum of all data elements : ")
for i in range(1,n+1):
    sum=sum+dic[i]
print(sum)
