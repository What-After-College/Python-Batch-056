import pandas as pd

d = pd.read_csv('train.csv')

topData = d.head(10)
print(topData)

