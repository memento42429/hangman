def inner_product(x,y):#関数の定義、内積を求める
    sum = 0
    for i in range (0,len(x)):#このときxyは同じ次元
        sum += x[i]*y[i]
    return sum

print(inner_product((2,3),(4,5)))