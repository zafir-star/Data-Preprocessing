import pandas as pd
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)

'Replace NULL values with the number 130