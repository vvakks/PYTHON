import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv('/Users/varke/Downloads/csv file/Bankloan_Cleanedv1.csv')


#Replacing null values

updated_df=df
updated_df['age'] = df['age'].bfill()

#print(updated_df['creddebt'].mean())
updated_df.describe().round(2)
#print(updated_df.head(5))
new_df= pd.DataFrame(updated_df,columns=['age', 'debtinc'])
#print(new_df.head(5))
#new_df.info()


scaler = MinMaxScaler()
normalized_df=scaler.fit_transform(new_df)
print(normalized_df)

x_array=np.array([[2],[3],[5],[6],[6]])

normalized_arr = scaler.fit_transform(x_array)
print(normalized_arr)

scaler_Standard=StandardScaler()
standardized_scaler= scaler_Standard.fit_transform(new_df)
print (standardized_scaler)


standardized_Arrscaler= scaler_Standard.fit_transform(x_array)
print (standardized_Arrscaler)


