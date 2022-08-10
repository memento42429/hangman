def fermat_minor(a,p):
    return a**(p-1)%p

ans = fermat_minor(16348039,3571)
print(ans)

import math
a = 16348039
b = 3570
for i in range(100):
    i+=1
    a+=1
    ans2 = math.gcd(a,b)
    print(ans2)
