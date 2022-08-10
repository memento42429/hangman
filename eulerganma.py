import math
import sumharmonic
def eulerg(limit):
    """
    sum = 0
    for i in range (1,limit):
        sum += 1/i
    """
    lim = math.log(limit)
    euler = sumharmonic.sumharmonic(limit) - lim
    return euler

print(eulerg(10000))
