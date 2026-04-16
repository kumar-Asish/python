import numpy as np
import random
# x=[5,6,7,8,9]
# op=np.mean(x)
# print(op)

# random input
# x=[]
# num=int(input("Enter the number of element:: "))
# for i in range(0,num):
#     op=random.randint(1,100)
#     x.append(op)
# print(x)
# k=np.mean(x)
# print(k)

# user input 
v=[]
num=int(input("Enter the number of element:: "))
for i in range(0,num):
    a=int(input())
    v.append(a)
print(v)
op=np.mean(v)
print(op)