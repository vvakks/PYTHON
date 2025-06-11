#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns
df= pd.read_csv('/Users/varke/Downloads/Churn_Modelling.csv')
df['Exited'].value_counts()/len(df)*100
new_df=df.copy()
labels = ["{0}- {1}".format(i,i+10) for i in range(10,90,10)]
print (labels)
new_df["age_group"]=pd.cut(new_df.Age, range(10,91,10), right=False, labels=labels)
new_df["age_group"].value_counts()
new_df = new_df.dropna(subset=["age_group"])
new_df.drop(columns=['CustomerId', 'Age'], axis=1, inplace=True)


new_df.info()
# %%

#4:28 on the video
