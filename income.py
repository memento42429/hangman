income = [402116, 402932, 383960, 389848, 380863, 383851, 380966, 381929, 381193, 376576, 382434, 400964, 416980, 431992]
incr = [0]*(len(income)-1)
n = len(incr)
for i in range(n):
    a = len(income)-(i+1)
    b = len(income)-(i+2)
    incr[i] = round((income[a]/income[b]*100),1)
print(incr)