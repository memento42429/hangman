import pandas_datareader.data as pdr
df = pdr.DataReader("PFE.US","stooq").sort_index()
data = df.loc['2021-3-22':'2021-08-11', 'Close' ].tolist()

data