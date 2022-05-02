def add(a,b):
    sum = a+b
    print(sum)
add(10,20)

def sub_decor(fun):
    def sub(a,b):
        print(a-b)
    return sub
@sub_decor
def add(x,y):
    print(x+y)
add(5,6)

