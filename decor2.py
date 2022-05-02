def sum(fun):
    def avg(a,b,c):
        sum= a+b+c
        avg= sum/3
    print(avg)
@sum
def add(x,y,z):
    print(sum)
add(10,20,30)