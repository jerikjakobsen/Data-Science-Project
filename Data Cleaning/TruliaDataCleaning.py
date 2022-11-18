import pandas as pd
from HelperFunctions import lowerCaseAllColumns, convertAddresses
import os

TruliaInterestingColumns = ["Uniq Id","Crawl Timestamp","Sqr Ft","Longitude","Latitude","Lot Size","Beds","Bath","Year Built","City","State","Address", "Days On Trulia","Zipcode", "Home Id"]
dfTrulia = pd.read_csv(os.path.join('..', 'CSVFiles', 'trulia_data.csv'))[TruliaInterestingColumns]
def prepareTruliaData(df):
    df = df.dropna()
    df = lowerCaseAllColumns(df)
    df = convertAddresses(df)
    df['crawl_date'] = pd.to_datetime(df['Crawl Timestamp']).dt.date
    df['listing_date'] = df['crawl_date'] - pd.to_timedelta(df['Days On Trulia'], unit='d')
    return df

prepareTruliaData(dfTrulia).to_csv("FilteredTruliaData.csv")