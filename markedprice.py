'''
accept the marked price from the user and calculate the net amount as (marked price-discount)
to pay according to following criteria
marked price        discount
>10000              20%
>7000 and <=10000   15%
<=7000              10%
'''
x = float(input("Enter the mark price : "))
if x>10000 :
    print("net amount of 20 % discount: {0}" .format((x*20)/100))
elif (x>7000 and x<=10000):
    print(" net amount of 15% discount: {0}" .format((x*15)/100))
else:
    print("net amount of 10% discount:{0}".format((x*10)/100))
