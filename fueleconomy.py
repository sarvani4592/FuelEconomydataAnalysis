import pandas as pd
import numpy as np

#laoding data
df=pd.read_csv('all_alpha_08.csv')
#df.head()
df1=pd.read_csv('all_alpha_18.csv')
#df1.head()

#finding count of samples of each data set
df.count()
df1.count()

#finding duplicated rows in 2008 data set
df.groupby(df.columns.tolist(),as_index=False).size()

#find number of rows with missing values in dataset of 2008
df.isnull().sum()
df1.isnull().sum()

#display unique values of Smartway 2008, smartway2018, Sales Area, Cert Region, Trans

df.SmartWay.unique()
df1.SmartWay.unique()

#Cleaning Column Labels
#pandas drop function to drop extraneous columns
df.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1)
df1.drop(['Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'],axis=1)

#rename Sales Area to Sales_Area and replace all the upper case letters with lower
# replace spaces with underscores and lowercase labels for 2008 dataset
df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# confirm changes
df.head(1)

# replace spaces with underscores and lowercase labels for 2018 dataset
df1.rename(columns=lambda x:x.strip().lower().replace(" ","_"),inplace=True)

# confirm changes
df1.head(1)


# save new datasets for next section
df.to_csv('data_08.csv', index=False)
df1.to_csv('data_18.csv', index=False)

#Filter, Drop Nulls, Dedupe
#shape of the stored datasets
df.shape()
df1.shape()
#filter data set with column cert refion for california
df.loc[df['cert_region'] == 'CA']

# print number of duplicates in 2008 and 2018 datasets
df.groupby(df.columns.tolist(),as_index=False).size()
df1.groupby(df1.columns.tolist(),as_index=False).size()