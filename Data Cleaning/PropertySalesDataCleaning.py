import pandas as pd
from HelperFunctions import lowerCaseAllColumns
import os

SalesInterestingColumns = ["state","property_street_address","property_city","sale_datetime","sale_price"]
salesDataDF = pd.read_csv("/../CSVFiles/AllSalesData.csv", encoding='UTF-16')[SalesInterestingColumns]
def prepareSalesData(df):
    df = df.dropna(subset=['state', "property_street_address", "property_city", "sale_datetime"])
    df = lowerCaseAllColumns(df)
    df = df.rename(columns={'state':'State', 'property_street_address': 'Address', 'property_city':'City'})
    df['sale_date'] = pd.to_datetime(df['sale_datetime']).dt.date
    df = df.drop(columns='sale_datetime')
    df['State'] = df['State'].astype('str')
    df['City'] = df['City'].astype('str')
    df['Address'] = df['Address'].astype('str')
    return df

df = prepareSalesData(salesDataDF)
print(df.dtypes)
df.to_csv("../CSVFiles/FilteredSalesData.csv", index = False)