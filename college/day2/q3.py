import csv
import pandas as pd
f=pd.read_csv('prac.csv')
print(f)
new = [["Anubhav",6,95]]
f=open("prac.csv","a")
w=csv.writer(f)
w.writerows(new)

# import csv
# import pandas as pd
# f = pd.read_csv('prac.csv')
# print(f)
# new = [["Hrishi", 60, 91]]
# with open("prac.csv", "a", newline='') as file:
#     w = csv.writer(file)
#     w.writerows(new)
