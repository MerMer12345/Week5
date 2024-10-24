import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('ch2_co2_levels.csv')

df['datestamp'] = pd.to_datetime(df['datestamp'], dayfirst=False)

df = df.set_index('datestamp')

df.plot()

plt.show()