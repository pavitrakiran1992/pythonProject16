#find  factorial of a number

n = int(input("Enter a number to find factorial : "))
if n>0:
    for i in range(1,n):
         n = n*i
    print( "factorial:",n)