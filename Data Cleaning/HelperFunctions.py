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

def stripsqft(row, columnName):
        row[columnName] = row[columnName].replace('sqft',"").replace(",","").strip()
        return row

def convertsqft(df, columnName):
    df = df.apply(stripsqft, columnName = columnName, axis = 1)
    df[columnName] = df[columnName].astype('str').astype('int')
    return df

def convertLotSize(df):
    def stripConvLotSize(row):
        lotSize = str(row['Lot Size'])
        if 'acres' in lotSize or 'acre' in lotSize:
            lotSize = lotSize.replace('acres',"").replace('acre','').replace(",","").strip()
            lotSize = float(lotSize) * 43560
            row['Lot Size'] = str(lotSize)
            return row
        else:
            return stripsqft(row, 'Lot Size')
    df = df.apply(stripConvLotSize, axis = 1)
    df['Lot Size'] = df['Lot Size'].astype('float')
    return df