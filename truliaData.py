import pandas as pd

def lowerCaseAllColumns(df):
    stringColumns = [ col  for col, dt in df.dtypes.items() if dt == object]
    for column in stringColumns:
        df[column] = df[column].str.lower()
    return df

def stripAddress(row):
    row['Address'] = row['Address'].replace(str(row["State"]), "")
    row['Address'] = row['Address'].replace(str(row['City']), "")
    row['Address'] = row['Address'].replace(str(int(row['Zipcode'])), "")
    row['Address'] = row['Address'].replace(" , ", "")
    row['Address'] = row['Address'].strip()
    return row

def convertAddresses(df):
    df = df.apply(stripAddress, axis = 1)
    return df

TexasInterestingColumns = ["state","property_street_address","property_city","sale_datetime","sale_price"]
dfTexas = pd.read_csv("texasRecords.csv", encoding='UTF-16')[TexasInterestingColumns]
def prepareTexasData(df):
    df = df.dropna(subset=['state', "property_street_address", "property_city", "sale_datetime"])
    df = lowerCaseAllColumns(df)
    df = df.rename(columns={'state':'State', 'property_street_address': 'Address', 'property_city':'City'})
    df['sale_date'] = pd.to_datetime(df['sale_datetime']).dt.date
    return df

TruliaInterestingColumns = ["Uniq Id","Crawl Timestamp","Sqr Ft","Longitude","Latitude","Lot Size","Beds","Bath","Year Built","City","State","Address", "Days On Trulia","Zipcode", "Home Id"]
dfTrulia = pd.read_csv("trulia_data.csv")[TruliaInterestingColumns]
def prepareTruliaData(df):
    df = df.dropna()
    df = lowerCaseAllColumns(df)
    df = convertAddresses(df)
    df['crawl_date'] = pd.to_datetime(df['Crawl Timestamp']).dt.date
    df['listing_date'] = df['crawl_date'] - pd.to_timedelta(df['Days On Trulia'], unit='d')
    return df

dfTexas = prepareTexasData(dfTexas)
dfTrulia = prepareTruliaData(dfTrulia)

print(f'Trulia Summary:\n{dfTrulia.describe()}\nTexas Summary:\n{dfTexas.describe()}')

print(dfTexas.columns)
print(dfTrulia.columns)

def mergeSaleAndTruliaData(sales, trulia):
    dfJoined = sales.merge(trulia, on=["Address", "City", "State"])
    dfFiltered = dfJoined[dfJoined["listing_date"] < dfJoined["sale_date"]]
    dfFiltered = dfFiltered.sort_values('sale_date').drop_duplicates(["Address", "City", "State"], keep='first')
    return dfFiltered
dfFiltered = mergeSaleAndTruliaData(dfTexas, dfTrulia)
dfFiltered.to_csv('FilteredListingSaleData.csv')
print(len(dfFiltered))
print(dfFiltered.head(20))
print(dfFiltered["Address"].value_counts())