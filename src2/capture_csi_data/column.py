import pandas as pd
import numpy as np
import csv

f1 = open("no-people.csv", 'r')
f2 = open("people.csv", 'r')
f3 = open("n.csv", 'w', newline='')
f4 = open("p.csv", 'w', newline='')

list1 = []
list2 = []
list3 = []

lines1 = f1.readlines()
lines2 = f2.readlines()

for line in lines1:
    a = line.split(',')
    x1 = a[25]
    list1.append(x1)
    f3.writelines(x1 + "\n")

for line in lines2:
    a = line.split(',')
    x2 = a[25]
    list2.append(x2)
f4.writelines(x2 + "\n")

for a, b in zip(list1, list2):
    x = {}
    x['沒人'] = a
    x['有人'] = b
    list3.append(x)

with open('compare1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    #writer.writerow(['沒人', '有人'])
    list3 = [list1, list2]
    # l = list(map(list, zip(*list3)))
    #writer.writerows(l)
    writer.writerows(list3)

print("寫入完成!")
