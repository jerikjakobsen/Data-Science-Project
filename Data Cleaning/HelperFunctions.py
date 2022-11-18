import pandas as pd

def lowerCaseAllColumns(df):
    stringColumns = [ col  for col, dt in df.dtypes.items() if dt == object]
    for column in stringColumns:
        df[column] = df[column].str.lower()
    return df

def convertAddresses(df):
    def stripAddress(row):
        row['Address'] = row['Address'].replace(str(row["State"]), "")
        row['Address'] = row['Address'].replace(str(row['City']), "")
        row['Address'] = row['Address'].replace(str(int(row['Zipcode'])), "")
        row['Address'] = row['Address'].replace(" , ", "")
        row['Address'] = row['Address'].strip()
        return row
    df = df.apply(stripAddress, axis = 1)
    return df