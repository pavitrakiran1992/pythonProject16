n = float(input("enter the student percentage: "))
if (n<25.0):
    print("D GRADE-FAIL")
elif (n>25 and n<45):
    print("C GRADE")
elif (n>45 and n<50):
    print("B GRADE")
elif(n<50 and n>60):
    print("B+ GRADE")
elif(n>60 and n<80):
    print("A GRADE")
else:
    print("A+ GRADE")
