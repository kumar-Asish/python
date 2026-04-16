# WAP that generate a list of 20 random numbers b/w 1 and 100 . remove the first and last items for the list ,sort
# the remaining items and print the result

import random
num=[]
for i in range(20):
    num.append(random.randint(1,100))
print("Random number b/w 1 and 100 are:: ",num)
num=num[1:19]
print("After deleting first and last element:: ",num)
num.sort()
print("After sorting list :: ",num)
