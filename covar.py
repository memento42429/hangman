def covar(x,y):
    sumx = 0
    sumy = 0
    sumxy = 0
    for i in x:
        sumx += i
    for i in y:
        sumy += i
    for i in range(len(x)):
        a = x[i] - sumx/len(x)
        b = y[i] - sumy/len(y)
        sumxy += a*b
    return sumxy/(len(x))

x=[12.1, 15.3, 18.6, 21.7, 26.1, 32.1] #temparatur 
y=[45, 520, 2864, 6874, 25487, 102870] #Beer sale
print(round(covar(x,y),2))