import pandas as pd
import numpy as np

#laoding data
xl_08_df=pd.read_csv('all_alpha_08.csv')
#df.head()
xl_18_df=pd.read_csv('all_alpha_18.csv')
#df1.head()
#ASSESSING THE DATA

#finding count of samples of each data set
xl_08_df.count()
xl_18_df.count()

# number of columns in each dataset
len(xl_08_df.columns)
len(xl_18_df.columns)

#finding duplicated rows in 2008 data set
xl_08_df.groupby(xl_08_df.columns.tolist(),as_index=False).size()
xl_18_df.groupby(xl_18_df.columns.tolist(),as_index=False).size()

#datatypes of columns in each set
print(xl_08_df.dtypes)
print(xl_08_df.dtypes)


#find number of rows with missing values in dataset of 2008
xl_08_df.isnull().sum()
xl_18_df.isnull().sum()

#display number of non null unique values of Smartway 2008, smartway2018, Sales Area, Cert Region, Trans

xl_08_df.SmartWay.unique()
xl_18_df.SmartWay.unique()
#save files with new name

xl_08_df.to_csv('data_08.csv', index=False)
xl_18_df.to_csv('data_18.csv', index=False)

df_08=pd.read_csv('data_08.csv')
df_18=pd.read_csv('data_18.csv')

#CLEANING THE DATA

# drop columns from 2008 dataset
df_08.drop(['Stnd', 'Underhood ID', ], axis=1, inplace=True)
del df_18['Stnd']
del df_18['Stnd Description']
del df_18['Underhood ID']
del df_18['Comb CO2']
del df_08['unadj_cmb_mpg']
del df_08['fe_calc_appr']

# rename Sales Area to Cert Region

df_08 = df_08.rename(columns={'Sales Area': 'Cert Region'})

# replace spaces with underscores and lowercase labels for 2018 dataset
df_08.rename(columns=lambda x:x.strip().lower().replace(" ","_"),inplace=True)
# replace spaces with underscores and lowercase labels for 2018 dataset
df_18.rename(columns=lambda x:x.strip().lower().replace(" ","_"),inplace=True)
#confirm changes
# make sure they're all identical like this
(df_08.columns == df_18.columns).all()

#FILTER DROP NULL DEDUPE

#shape of the stored datasets
xl_08_df.shape()
xl_18_df.shape()

#filter data set with column cert refion for california
df_08 = df_18.loc[df_08['cert_region']=='CA']
df_18 = df_18.loc[df_18['cert_region']=='CA']
# confirm only certification region is California
df_08['cert_region'].unique()
# confirm only certification region is California
df_18['cert_region'].unique()

# drop certification region columns form both datasets
del df_08['cert_region']
del df_18['cert_region']
#confirm the number of columns after dropping by using size function
df_18.shape

#DROP ROWS WITH MISSING VALUES
# view missing value count for each feature in 2008
df_08.info()
# view missing value count for each feature in 2018
df_18.info()
# checks if any of columns in 2008 have null values - should return True if nulls are present
df_08.isnull().sum().any()
# checks if any of columns in 2018 have null values - should return True if nulls are present 
df_18.isnull().sum().any()
# drop rows with any null values in both datasets
df_08=df_08.dropna('index','any')
df_18=df_18.dropna('index','any')
# checks if any of columns in 2008 have null values - should print False
df_08.isnull().sum().any()
# checks if any of columns in 2018 have null values - should print False
df_18.isnull().sum().any()

#DEDUPLICATING

# print number of duplicates in 2008 and 2018 datasets
df_08.groupby(df_08.columns.tolist(),as_index=False).size()
df_18.groupby(df_18.columns.tolist(),as_index=False).size()

#drop all duplicates in 2008, 2018 datasets
df_08.drop_duplicates(keep='first')
df_18.drop_duplicates(keep='first')

#check if they are removed # df_08.duplicated()
df_18.duplicated()