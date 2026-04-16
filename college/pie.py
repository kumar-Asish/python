import matplotlib.pyplot as plt

# Get user input for data points
x = list(map(int, input("Enter numeric labels separated by spaces: ").split()))
y = list(map(int, input("Enter values separated by spaces: ").split()))


labels = [str(label) for label in x]


plt.pie(y, labels=labels)

plt.title('Pie Chart Example')

plt.show()
