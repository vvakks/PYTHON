#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

base_data = pd.read_csv('/Users/varke/Downloads/ligma1.csv')

#for i, predictor in enumerate(base_data.drop(columns=['Exited'])):
   # plt.figure()
   # sns.countplot(data=base_data, x=predictor, hue='Exited')
#sns.histplot(x='Gender', hue= 'Geography', data=base_data, stat="count", multiple= "dodge")
new_data=base_data.loc[base_data['Exited']==1]
#new_data.info()
#print(len(new_data))
#sns.histplot(x= 'Gender' , hue = 'Geography', data=new_data, stat= "count", multiple="dodge")
#base_data.drop(columns=['Gender', 'Geography']).corr()
#df = pd.read_csv('/Users/varke/Downloads/csv file/Bankloan_Cleanedv1.csv')
#df.info()
#df.corr()
#plt.figure(figsize=(20,8))
#df.corr()['income'].sort_values(ascending=False).plot(kind= 'bar')
#plt.figure(figsize=(12,12))
#sns.heatmap(df.corr(), cmap="Paired")
#df['age'].value_counts().sort_index(ascending=True).plot()
Tot= sns.kdeplot(base_data.Age[(base_data["Exited"]==0)], color= "Red", fill=True)
Tot= sns.kdeplot(base_data.Age[(base_data["Exited"]==1)], color="Blue", fill=True)
Tot.legend(["No Churn", "Churn"], loc='upper right')
Tot.set_ylabel('Density')
Tot.set_xlabel('Age')
Tot.set_title('Age by churn')
# %%
