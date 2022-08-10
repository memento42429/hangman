def detectfibn(n):
    fibn = (((1+5**(1/2))/2)**n - ((1-5**(1/2))/2)**n)/5**(1/2)
    return fibn

fib = []
for i in range(100):
    fib.append(int(detectfibn(i)))

print(fib)    