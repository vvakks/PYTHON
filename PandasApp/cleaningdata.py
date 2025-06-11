#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import statistics
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv('/Users/varke/Downloads/csv file/Bankloan_Cleanedv1.csv')
#print(df.describe())
df['age']=df['age'].fillna(df['age'].mean())
scaler = StandardScaler()
st_df=scaler.fit_transform(df)
df['income']= df['income'].fillna(df['income'].median())
df['ed']= df['ed'].fillna(df['ed'].median())
def find_anomalies(data):
    anomalies = []
    random_data_std= statistics.stdev(data)
    random_data_mean=statistics.mean(data)

    anomaly_cut_off= random_data_std*3
    lower_limit= random_data_mean- anomaly_cut_off
    upper_limit= random_data_mean+ anomaly_cut_off

    
    for outlier in data:
        if outlier > upper_limit or outlier< lower_limit:
            anomalies.append(outlier)
    return anomalies


for columns in df.columns:
    print(len(find_anomalies(df[columns])), columns)
for column in df.columns:
    anomalies = find_anomalies(df[column])
    random_data_std= statistics.stdev(df[column])
    random_data_mean=statistics.mean(df[column])

    anomaly_cut_off= random_data_std*3
    lower_limit= random_data_mean- anomaly_cut_off
    upper_limit= random_data_mean+ anomaly_cut_off
    
    df[column] = df[column].apply(lambda x: lower_limit if x<lower_limit or x>upper_limit else x)
print("After removing outliers")
for columns in df.columns:
    print(len(find_anomalies(df[columns])), columns)
#numerical_cols = df.select_dtypes(include=np.number).columns.tolist()

#%%
