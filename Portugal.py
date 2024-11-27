import pandas as pd
from pandas import DataFrame
import os

directory = '/Users/cleopypavlou/Desktop/DataProject'
os.makedirs(directory, exist_ok=True)  # Create directory if it doesn't exist

pd.set_option('future.no_silent_downcasting', True)

df: DataFrame = pd.read_csv('/Users/cleopypavlou/PycharmProjects/Portugal/portugal_housing.csv', low_memory=False)
print(df.info())
print(df.describe())
print(df.head())
print(df.isnull().sum())

missing_per = (df.isnull().sum() / len(df)) * 100
print(missing_per)
columns_to_drop = missing_per[missing_per > 50].index
print('column to drop:', columns_to_drop)
df.drop(columns = columns_to_drop, inplace=True)
print('Remaining Coloumns:', df.columns)  #Data is Clean.
print (df.sample(10) )

numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns]= df[numeric_columns].fillna(df[numeric_columns].mean())
print("Numeric Columns:",numeric_columns )
categorical_columns = df.select_dtypes(include=['object']).columns
for column in categorical_columns:
    mode_value = df[column].mode()[0]
    df[column] = df[column].fillna(mode_value)
    df[column] = df[column].astype(object)
print('categorical_columns:',categorical_columns)
print("Missing values in categorical column filles.")

df.to_csv('/Users/cleopypavlou/Desktop/DataProject/cleaned_portugal_housing.csv', index= False)





