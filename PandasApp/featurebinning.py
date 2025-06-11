#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
df = pd.read_csv('/Users/varke/Downloads/ligma1.csv')
print(df.head(5))
df.info()
print(df.Age.min())
print(df.Age.max())
labels = [ '0-20','21-40','41-60', 'more than 60' ]
bins = [0,20,40,60,100]
df['Age_bins']= pd.cut(df.Age,bins, labels= labels, include_lowest=True)
print(df.head(5))
print(df.Age_bins.value_counts())
plt.bar(labels, df.Age_bins.value_counts())

def add_labels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])
plt.bar(labels, df.Age_bins.value_counts())
add_labels(labels, df.Age_bins.value_counts())
plt.title('Age Count')
plt.xlabel('Age Bins')
plt.ylabel('Age Count')
plt.show()

# %%
