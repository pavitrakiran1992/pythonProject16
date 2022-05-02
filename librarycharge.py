'''
Accept the number of days from the user and calculate the charge for library according to following:
Till five days : Rs.2/day
six to ten days : Rs.3/day
11 to 15 days : Rs.4/day
After 15 days :Rs.5/day
'''

n = int(input("Enter the number of days by the user: "))
if (n==5):
    print(" The charge of library for 5 days:Rs.{0} ". format(n*2))
elif(n>6 and n<10):
    print(" The charge for library of 6 -10 days:Rs.{0}".format(n*3))
elif(n>11 and n<15):
    print("The charge for library for 11 to 15 days: Rs.{0}".format(n*4))
else:
    print("The charge for library for after 15 days: Rs.{0}".format(n*5))