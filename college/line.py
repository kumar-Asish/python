import matplotlib.pyplot as plt

x=list(map(int,input("Enter the value of time:: ").split()))
y=list(map(int,input("Enter the value of distance:: ").split()))


print(x)
print(y)


plt.xlabel('Time')
plt.ylabel('Distance')


plt.plot(x,y)
plt.show()