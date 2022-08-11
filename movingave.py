import pandas_datareader.data as pdr
df = pdr.DataReader("PFE.US","stooq").sort_index()
data = df.loc['2021-3-22':'2021-08-11', 'Close' ].tolist()

def movingave(data,periods):
    n = len(data)
    ave = [0]*(n - periods+1)
    for i in range(n - periods+1):
        t = data[i:i+periods]
        sumt = 0
        for j in t:
            sumt += j
        ave[i] = round(sumt/periods,2)
    return ave
    
print(movingave(data,5))

