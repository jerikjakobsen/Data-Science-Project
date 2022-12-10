import pandas as pd
import os

filteredTruliaDF = pd.read_csv('/../CSVFiles/FilteredTruliaData.csv')
filteredSalesDF = pd.read_csv('/../CSVFiles/FilteredSalesData.csv')

def mergeSaleAndTruliaData(sales, trulia):
    dfJoined = sales.merge(trulia, on=["Address", "City", "State"])
    dfFiltered = dfJoined[dfJoined["listing_date"] < dfJoined["sale_date"]]
    dfFiltered = dfFiltered.sort_values('sale_date').drop_duplicates(["Address", "City", "State"], keep='first')
    dfFiltered["Days on Market"] = (pd.to_datetime(dfFiltered['sale_date']).dt.date- pd.to_datetime(dfFiltered['listing_date']).dt.date).dt.days
    return dfFiltered
dfFiltered = mergeSaleAndTruliaData(filteredSalesDF, filteredTruliaDF)
dfFiltered.to_csv('../CSVFiles/FilteredListing+SaleData.csv', index = False)