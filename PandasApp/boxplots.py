#%%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('/Users/varke/Downloads/csv file/Bankloan_Cleanedv1.csv')
sns.boxplot(data=data)
df= pd.DataFrame(data)
df.describe()

list1= [87, 12, 45, 3, 76, 29, 64, 91, 58, 33, 7, 100, 41, 27, 18, 69, 84, 53, 9, 36]
import statistics
mean=statistics.mean(list1)
sorted_list1=sorted(list1)
print(sorted_list1)

# %%
