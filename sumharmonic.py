def sumharmonic(m):
    sum =0
    for i in range(1,1+m):
        sum += 1/i
    return sum

print(sumharmonic(100))

"""
def sumharmonic(m):
    sum = 0
    for i in range(1,m+1):
        sum += 1/i
        return sum

ans = sumharmonic(100)
print(ans)
"""