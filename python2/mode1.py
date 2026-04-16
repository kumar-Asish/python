from scipy import stats as st
import random
# x=[2,3,4,5,2,5,5,1]
# op=st.mode(x)
# print("Mode :: ",op)

# take input random
# v=[]
# n=int(input("Enter the no of element:: "))
# for i in range(0,n):
#     k=random.randint(1,10)
#     v.append(k)
# print(v)
# print(st.mode(v))

# take input from user
v=[]
n=int(input("Enter the no of element:: "))
for i in range(0,n):
    l=int(input())
    v.append(l)
print(v)
op=st.mode(v)
print("Mode :: ",op)