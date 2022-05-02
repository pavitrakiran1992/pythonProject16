'''
Acompany decided to give bonus for employee according to following criteria
time period of service :bonus
more than 10 years :10%
>=6 and <=10 -8%
less than 6 years -5%
ask user for their salary and years of service and print the net bonus amount

'''
m = int(input(" enter your salary: "))
n = int(input("enter the years of experience: "))
if (n > 10):
    m = m*(10/100)
    print(m,"-your net bonus salary- 10 %  added as bonus to your salary")
elif (n>=6 and  n<=10):
    m = m*(8/100)
    print(m,"- your net bonus salary - 8% added as bonus to your salary")
elif(n<6):
    m = m*(5/100)
    print(m,"- your net bonus salary - 5% added as bonus to your salary")
else:
    print("no bonus will be provided due to less experience")


