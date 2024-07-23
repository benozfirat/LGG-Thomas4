import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from catboost import CatBoostRegressor
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error

#Function to p
def remove_outliers(col):
    Q1 = col.quantile(0.15)
    Q3 = col.quantile(0.85)
    IQR = Q3 - Q1
    lower_boundary = Q1 - 1.5 * IQR
    upper_boundary = Q3 + 1.5 * IQR
    return lower_boundary, upper_boundary

df = pd.read_csv("datasett.csv")

# Create a dictionnary with the square meter price per district
pricesqm = {'Tournai':1799, 'Brugge':3670, 'Veurne':3349, 'Mechelen':2620, 'Antwerp':2614, 
        'Ieper':2188, 'Mons':1536, 'Philippeville':1549, 'Brussels':3305, 'Soignies':1812, 
        'Charleroi':1507, 'Leuven':2906, 'Liège':1969, 'Aalst':2151, 'Sint-Niklaas':2342, 
        'Verviers':1917, 'Marche-en-Famenne':1816, 'Kortrijk':2204, 'Gent':2909, 'Eeklo':2197, 
        'Hasselt':2197, 'Nivelles':2716, 'Diksmuide':2100, 'Dendermonde':2267, 'Huy':1842, 
        'Tongeren':2142, 'Dinant':1835, 'Neufchâteau':1725, 'Halle-Vilvoorde':2735, 'Tielt':2188, 
        'Roeselare':2063, 'Namur':2136, 'Oostend':2661, 'Oudenaarde':2099, 'Thuin':1540, 
        'Arlon':2375, 'Turnhout':2200, 'Ath':1834, 'Maaseik':2163, 'Virton':1917, 
        'Bastogne':1814, 'Mouscron':1799, 'Waremme':1905}

#Add dictionnary to the DF
pricesqm_series = pd.Series(pricesqm)
df['price_sqm'] = df['District'].map(pricesqm_series)

#Transform the value of TypeOfProperty to 0 and 1 and limit number of facades to 5
df['TypeOfProperty'] = df['TypeOfProperty'].map({1: 0, 2: 1})
df['NumberOfFacades'] = df['NumberOfFacades'].apply(lambda x: 4 if x >= 4 else x)

# Drop columns that will not be useful and the rows containing missing values in columns Region and Province 
df = df.drop(["Url","ConstructionYear","Country","Furnished","Fireplace","PropertyId","MonthlyCharges","RoomCount","Locality"], axis=1)
df = df.dropna(subset=['Region','Province','District'])

#Drop the useless values in TypeOfSale
df = df.loc[(df['TypeOfSale'] != "annuity_monthly_amount") & 
            (df['TypeOfSale'] != "annuity_without_lump_sum") & 
            (df['TypeOfSale'] != "annuity_lump_sum")]

#Drop the useless values in PEB
df = df.loc[(df['PEB'] != "F_D") & 
            (df['PEB'] != "E_C") & 
            (df['PEB'] != "F_C") & 
            (df['PEB'] != "A_A+")&
            (df['PEB'] != "G_F")&
            (df['PEB'] != "G_C")&
            (df['PEB'] != "B_A")&
            (df['PEB'] != "E_D")&
            (df['PEB'] != "F_E")]

# Complete the value in GardenArea if it's missing and if SurfaceOfPlot > LivingArea by GardenArea = Surface - Living 
for i, row in df.iterrows():
    if pd.isna(row['GardenArea']):
        if row['SurfaceOfPlot'] > row['LivingArea']:  
            df.at[i,'GardenArea'] = row['SurfaceOfPlot'] - row['LivingArea']

# Complete the value in Garden and GardenArea if value is missing in GardenArea or not
for i, row in df.iterrows():
    if pd.isna(row['GardenArea']):
        df.at[i,'Garden'] = 0
        df.at[i,'GardenArea'] = 0
    else:
        df.at[i,'Garden'] = 1

#Remove outliers with the function from above
columns_with_outliers = df[['BathroomCount','BedroomCount','GardenArea','LivingArea','NumberOfFacades','Price','SurfaceOfPlot','ToiletCount',]]
for col in columns_with_outliers:
    lower_boundary, upper_boundary = remove_outliers(df[col])
    df = df[~((df[col] < (lower_boundary)) |(df[col] > (upper_boundary)))]

#Use KNN to replace missing values by the 5 closest neighbours in attributes
imputed_data_knn = ['BathroomCount', 'LivingArea', 'NumberOfFacades', 'ToiletCount', 'SurfaceOfPlot', 'ShowerCount']
imputer = KNNImputer(n_neighbors=5)
df[imputed_data_knn] = imputer.fit_transform(df[imputed_data_knn])

#Fill missing values with 0
df['SwimmingPool'] = df['SwimmingPool'].fillna(0)
df['Terrace'] = df['Terrace'].fillna(0)

# Use OneHotEncoder to create boolean columns of categorical columns
ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform="pandas")
ohetransform = ohe.fit_transform(df[['District','FloodingZone','PEB','StateOfBuilding','Kitchen', 'Region','SubtypeOfProperty','Province', 'TypeOfSale']])
df = pd.concat([df,ohetransform],axis=1).drop(columns=['District','FloodingZone','PEB','StateOfBuilding','Kitchen', 'Region','SubtypeOfProperty','Province', 'TypeOfSale'])

#Return cleaned dataset
df.to_csv('clean_dataset.csv', index=False)

