f=open('hello.txt','r')
d=f.read()
print("Display the words in the file: ")
print(d)
c=0
for i in d:
    if(i>='A' and i<='Z' or i>='a' and i<='z'):
        c=c+1
print('Total no. of words: ',c)