import numpy as np
import random
# v=[5,6,7,7,8,8,9,6,8,5]
# op=np.median(v)
# print(op)

# take input random 
# v=[]
# n=int(input("Enter the no of element :: "))
# for i in range (0,n):
#     k=random.randint(1,100)
#     v.append(k)
# print(v)
# op=np.median(v)
# print(op)


# take input from user
v=[]
n=int(input("Enter the no of element :: "))
for i in range (0,n):
    k=int(input())
    v.append(k)
print(v)
op=np.median(v)
print(op)

