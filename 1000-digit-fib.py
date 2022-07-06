def fib(a):
    if a==1 or a==0:
        return 1
    else:
        return fib(a-1)+fib(a-2)
def digits(a):
    i=0
    while fib(i) < 10 ** a:
       i=i+1
    print(fib(i))
    return i+1
print(digits(3))