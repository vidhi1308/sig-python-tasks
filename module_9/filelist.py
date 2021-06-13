print("name - VIDHI SHARMA  roll no - 1900300100242")
l = ['A','B','C','D']
with open('sample2.txt', 'w+') as file:
    for items in l:
        file.write('%s\n' %items)
file.close()
file = open('sample2.txt','r+') 
for l in file:
    print(l)
file.close()