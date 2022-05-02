# write a program to display product of the digits  of a number accepted from the user
# Python3 program to compute
# product of digits in the number.

# Function to get product of digits
n = input ("enter a number to find sum and product : ")

s = 0
m = 1

for i in n:
    if i.isdigit ():
        s=s+ int (i)
        m=m* int (i)

print ("Sum:", s)
print ("Product:", m)
