import pandas as pd
from HelperFunctions import lowerCaseAllColumns, convertAddresses, convertsqft, convertLotSize
import os

TruliaInterestingColumns = ["Crawl Timestamp","Sqr Ft","Longitude","Latitude","Lot Size","Beds","Bath","Year Built","City","State","Address", "Days On Trulia","Zipcode"]
dfTrulia = pd.read_csv(os.path.join('..', 'CSVFiles', 'trulia_data.csv'))[TruliaInterestingColumns]
def prepareTruliaData(df):
    df = df.dropna()
    df = lowerCaseAllColumns(df)
    df = convertAddresses(df)
    df = convertsqft(df, 'Sqr Ft')
    df = convertLotSize(df)
    df['crawl_date'] = pd.to_datetime(df['Crawl Timestamp']).dt.date
    df['listing_date'] = df['crawl_date'] - pd.to_timedelta(df['Days On Trulia'], unit='d')
    df['State'] = df['State'].astype('str')
    df['City'] = df['City'].astype('str')
    df['Address'] = df['Address'].astype('str')
    return df


df = prepareTruliaData(dfTrulia)
print(df.head())
df.to_csv("../CSVFiles/FilteredTruliaData.csv", index = False)