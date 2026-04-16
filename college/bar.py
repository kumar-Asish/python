import matplotlib.pyplot as plt

x=list(map(int,input("Enter the value of time:: ").split()))
y=list(map(int,input("Enter the value of distance:: ").split()))


print(x)
print(y)

plt.xlabel('Time')
plt.ylabel('Distance')

plt.bar(x,y,color='r',label='user Data')
plt.show()