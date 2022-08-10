def average(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    return sum/len(x)

data = [67, 85, 78, 72]
ans = 0
for i in data:
    ans += i
ans = ans/len(data)
print(ans)
print(average(data))