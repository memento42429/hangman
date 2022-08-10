import math
def nsphere_volume(n):
    ans = (math.pi**(n/2)/math.gamma(n/2+1))
    return ans

print(nsphere_volume(2))
