import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

data = {'A': [45,37,42,35,39],
        'B': [38,31,26,28,33],
        'C': [10,15,17,21,12]
        }
df2 = pd.DataFrame(data,columns=['A','B','C'])
print (df2)
corrMatrix = df2.corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()

print (corrMatrix)
