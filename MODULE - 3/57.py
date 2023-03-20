"""
58) Write a Python program to read a random line from a file. 
"""

import random

f = open("D:\SMART DUSTBIN.txt",'r')

lines = f.read().splitlines() 

print(lines)
print(lines[0])

print(random.choice(lines))