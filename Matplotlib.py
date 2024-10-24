import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('ch2_co2_levels.csv')

df['datestamp'] = pd.to_datetime(df['datestamp'], dayfirst=False)

df = df.set_index('datestamp')
#plt.style.use('fivethirtyeight') <- works, but ugly
#plt.style.use('ggplot')
#ax = df.plot(color='red')
ax = df.plot(figsize=(20, 5), fontsize=12, linewidth=2, linestyle='--')
ax.set_xlabel('Date', fontsize=12, weight='bold', color='black')
ax.set_ylabel('CO2 Level')
ax.set_title('CO2 Level vs Date')
#df.plot()

plt.show()