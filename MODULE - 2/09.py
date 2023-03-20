# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

x=int(input("Enter the 1st number :-"))
y=int(input("Enter the 2st number :-"))
z=int(input("Enter the 3st number :-"))

sum=x+y+z

if x==y or y==z or z==x:
    sum=0
   
else:
     x+y+z
    
print(sum)