# How will you remove last object from a list?
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 

"""
The slicing technique can also remove the last element from the list. 
list[:-1] will remove the last element except for all elements

"""

list=[2,33,222,33,25]
print("orignal list",list)

list=list[:-1]

print("new list",list)