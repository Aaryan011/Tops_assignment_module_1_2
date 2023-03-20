# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

n1=int(input("Enter the 1st number ="))
n2=int(input("Enter the 2nd number ="))

sum=n1+n2
diff=n1-n2

if n1==n2 or sum==5 or diff==5:
    print("True")
else:
    print("False")

print(sum)
print(diff)