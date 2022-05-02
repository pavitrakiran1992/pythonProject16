def hello_decorator(func):
    def inner1():
        print("hello, this is before execution")
        func()
        print("This is after function execution")
    return inner1
def fun_to_used():
    print("the decorator function")
fun_to_used = hello_decorator(fun_to_used)
fun_to_used()