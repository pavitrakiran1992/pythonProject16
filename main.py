x = int(input("Total no of working days: "))
y = int(input("total number of days for absent"))
per = (y/x)*100
if(per<75):
    print("student will not be allowed to sit in examination")
else:
    print("student will be allowed for examination")
