import statistics as st
import random 
# v=[5,6,7,8,9]
# op=st.variance(v)
# print(op)

# Take input randomly

# v=[]
# n=int(input("Enter the no of element:: "))
# for i in range (0,n):
#     k=random.randint(1,100)
#     v.append(k)
# print(v)
# op=st.variance(v)
# print("Variance:: ",op)


# Take input from user

v=[]
n=int(input("Enter the no of element:: "))
for i in range (0,n):
    k=int(input())
    v.append(k)
print(v)
op=st.variance(v)
print("Variance:: ",op)
