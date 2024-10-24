import pandas as pd
df = pd.read_csv('ch2_co2_levels.csv')
print(df)
df.columns
print("head:")
print(df.head(n=5))
print("tail:")
print(df.tail(n=5))
print("Datatypes")
print(df.dtypes)
df['datestamp'] = pd.to_datetime(df['datestamp'], dayfirst=False)
print(df.dtypes)

#look in Matplotlib.py for the rest of the Exercise