#%%
import numpy as np
import matplotlib.pyplot as plt
import statistics
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv('/Users/varke/Downloads/csv file/Bankloan_Cleanedv1.csv')
new_df= pd.DataFrame(df,columns=['age', 'debtinc'])


#function to detect outlier
def find_anomalies(data):
    anomalies = []
    random_data_std= statistics.stdev(data)
    random_data_mean=statistics.mean(data)

    anomaly_cut_off= random_data_std*3
    lower_limit= random_data_mean- anomaly_cut_off
    upper_limit= random_data_mean+ anomaly_cut_off

    #Generate Outliers
    for outlier in data:
        if outlier > upper_limit or outlier< lower_limit:
            anomalies.append(outlier)
    return anomalies
#list_1=find_anomalies(new_df['age'].tolist())
newer_df=new_df
newer_df['age']= newer_df['age'].fillna(new_df['age'].median())
list1= find_anomalies(newer_df['debtinc'])
print(list1)
print(len(new_df))
print(new_df.age.skew())


import seaborn as sns

new_df['debtinc_transformed']=np.log(new_df.debtinc)
new_df.debtinc_transformed.skew()

list_2= find_anomalies(new_df.debtinc_transformed)
print(len(list_2))
print(sns.kdeplot(new_df.debtinc_transformed))
#print(len(list_1))




# %%
