# write a program to print table of a number accepted from the user

n = int(input("Enter a number to print table: "))
for i in range(1,11):
    print(n,"x",i,"={0}".format(n*i))