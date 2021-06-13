print("name - VIDHI SHARMA  roll no - 1900300100242")
print("Enter a number : ")
num=int(input())
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=int(num/10)
print("sum of digits of entered number : ")
print(sum)