import pandas as pd
import sys
import os
filePath = "../CSVFiles/FilteredListing+SaleData.csv"
data = pd.read_csv(filePath, sep=",")
data = data[data['sale_price'] > 0]
data = data.drop(['Address', "State", "City", "crawl_date", "listing_date"], axis = 1)
data.corr()[['Days On Trulia', 'sale_price']].to_csv("correlations.csv")
