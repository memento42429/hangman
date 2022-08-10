import math
def myexp(lim):
    ans = 0
    for i in range(lim):
        ans += 1/math.factorial(i)
    return ans

print(myexp(1000))