print("name - VIDHI SHARMA  roll no - 1900300100242")
n=0
file = open('sample1.txt','r+') 
for l in file:
    print(l)
with open('sample1.txt') as f:
    for i, l in enumerate(f):
        pass
    n=i+1
print("The number of lines in file:",n)
