#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
df= pd.read_csv('/Users/varke/Downloads/Churn_Modelling.csv')
df.drop(columns=["CustomerId", "RowNumber", "Surname"], axis=1, inplace=True)

#Label Encoding
le = preprocessing.LabelEncoder()

df['Gender_label']= le.fit_transform(df.Gender.values)
df.Gender_label.value_counts()
#df.info()
#df.head(5)

df['Geography_Label']= le.fit_transform(df.Geography.values)
df.Geography_Label.value_counts()

#One-Hot encoder
one_hot= pd.get_dummies(df['Geography'])
one_hot.info()
df_dummies= pd.get_dummies(df)
#df_dummies.head(5)

df_dummies=pd.get_dummies(df,drop_first=True)
df_dummies.head(5)
from category_encoders import TargetEncoder
encoder= TargetEncoder()
df1=pd.read_csv('/Users/varke/Downloads/Churn_Modelling.csv')
df1.drop(columns= ["CustomerId", "RowNumber", "Surname"], axis=1, inplace=True)
df1['Gender Encoded']= encoder.fit_transform(df1['Gender'], df1['Exited'])
df1['Gender Encoded'].value_counts()
from category_encoders import HashingEncoder
x= df.Gender
y=df.Exited
ce_hash= HashingEncoder(cols = ['Gender'])
ce_hash.fit_transform(x,y)

X=df.Geography
ce_hash2= HashingEncoder(n_components=16,cols= ['Geography'])
ce_hash2.fit_transform(X,y)

# %%
