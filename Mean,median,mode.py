'mean,median,mode'

import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)

import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].median()
df.fillna({"Calories": x}, inplace=True)

import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mode()
df.fillna({"Calories": x}, inplace=True)