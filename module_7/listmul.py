print("name - VIDHI SHARMA  roll no - 1900300100242")
def multiply_list_elements(p):
    product=1
    for i in p:
        product=product*i
    return product

print("enter the number of elements in the list : ")
n=int(input())
l=[]
print("Enter list elements : ")
for i in range(0, n):
    s=int(input())
    l.append(s)
prod=multiply_list_elements(l)
print("Product of list elements : ", prod)