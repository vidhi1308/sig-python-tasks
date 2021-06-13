print("name - VIDHI SHARMA  roll no - 1900300100242")
file = open('sample1.txt','r') 
for lines in file:
    print(lines)
print("The first two lines of the file:")
n=2
from itertools import islice
with open('sample1.txt') as f:
    for l in islice(f,2):
        print(l) 
file.close()