n = int(input("ENTER NO OF ROWS:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-i,end='')
    print()