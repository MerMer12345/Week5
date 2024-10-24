import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ch1_discoveries.csv')
plt.style.use('ggplot')
df['date'] = pd.to_datetime(df['date'], dayfirst=False)
#print(df.dtypes)
df = df.set_index('date')

df_subset = df['01-01-1860': '01-01-1885']



ax = df_subset.plot(color='blue', fontsize=12, linestyle='--')

ax.axhline(y = 4, color = 'g', linestyle = '-')

ax.axhline(y = 6, color = 'r', linestyle = '-', linewidth = 4)

ax.set_title('Time series')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Discoveries')
plt.show()

#print(df_subset)