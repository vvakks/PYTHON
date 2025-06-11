#%%
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

telco_base_data = pd.read_csv('/Users/varke/Downloads/csv file/Bankloan_Cleanedv1.csv')
head_5=telco_base_data.head(5)
telco_new= telco_base_data[['employ','income','age']]
for i, predictor in enumerate(telco_new.drop(columns= ['income'])):
    plt.figure()
    sns.countplot(data=telco_new, x=predictor, hue='income')


# %%
