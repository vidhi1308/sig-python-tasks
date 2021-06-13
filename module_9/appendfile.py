print("name - VIDHI SHARMA  roll no - 1900300100242")
file = open('sample1.txt','r+') 
file.write("This is line 1.\n") 
file.write("this is line 2.\n") 
for l in file:
    print(l)
file.close() 
file = open('sample1.txt','a') 
file.write("This is line 3.\n") 
file.close() 
file = open('sample1.txt','r') 
for line in file:
    print(line)
file.close() 


