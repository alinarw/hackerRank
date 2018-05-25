# https://www.hackerrank.com/challenges/battery/problem

import matplotlib.pyplot as plt

timeCharged = []
timeUsed = []

with open('battery.txt', 'r') as f:
    for line in f:
        char, wat = line.rstrip('\n').split(',')
        char, wat = [float(char), float(wat)]
        timeCharged.append(char)
        timeUsed.append(wat)
plt.scatter(timeCharged, timeUsed)
plt.xlabel("Charging time")
plt.ylabel("Watching time")
plt.show()

a = float(input())
if a >= 4.00:
    b = 8.00
else:
    b = 2 * a
print(b)