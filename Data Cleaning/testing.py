import pandas as pd
import os

df = pd.read_csv("../CSVFiles/FilteredListing+SaleData.csv")

print(df.columns)
print(len(df))

df["day_of_week_listed"] = pd.to_datetime(df["listing_date"]).dt.day_name()

SelectedCities = [
"jacksonville",
"orlando",
"los angeles",
"tampa",
"atlanta",
"baltimore",
"washington",
"aurora",
"denver",
"fort wayne",
"riverside"]

dfCities = df[df["City"].isin(SelectedCities)]
print(len(dfCities))
#dfCities.to_csv("../CSVFiles/FilteredListing+SaleData.csv", index = False)

dfEncoded = pd.get_dummies(data=dfCities, columns=["City", "State", "day_of_week_listed"])
dfEncoded = dfEncoded.drop(columns=["Address", "sale_price", "sale_date", "listing_date", "day_of_week"])

dfEncoded.to_csv("../CSVFiles/EncodedSalesListing.csv", index=False)

print(len(dfEncoded[dfEncoded["Days on Market"] == 180]))
print(dfEncoded["Days on Market"].describe())

dfEncoded.corr()["Days on Market"].to_csv("EncodedCorrelations.csv")