def makefib(n):
    fib = []
    for i in range(0,n):
        if i == 0 or i == 1:
            fib.append(i)
        else:
            fib.append(fib[i-2]+fib[i-1])
    return fib

fib = makefib(10)
print(fib)