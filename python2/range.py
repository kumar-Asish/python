import numpy as np
import random
# v=[5,6,7,7,8,8,9]
# Minimum=np.min(v)
# Maximum=np.max(v)
# print("Minimum:: ",Minimum)
# print("Maximum:: ",Maximum)
# Range=Maximum-Minimum
# print("Range:: ",Range)

# Take input randomly

# v=[]
# n=int(input("Enter the no of element:: "))
# for i in range (0,n):
#     k=random.randint(1,100)
#     v.append(k)
# print(v)
# Min=np.min(v)
# Max=np.max(v)
# Range = Max-Min
# print("Minimum:: ",Min)
# print("Maximum:: ",Max)
# print("Range:: ",Range)

# Take input from user

v=[]
n=int(input("Enter the no of element:: "))
for i in range (0,n):
    k=int(input())
    v.append(k)
print(v)
Min=np.min(v)
Max=np.max(v)
Range = Max-Min
print("Minimum:: ",Min)
print("Maximum:: ",Max)
print("Range:: ",Range)
